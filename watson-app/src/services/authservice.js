import auth0 from 'auth0-js'
import axios from 'axios'
import configService from './configservice'

class AuthService {
    authenticated = this.isAuthenticated()

    constructor() {
        this.login = this.login.bind(this)
        this.setSession = this.setSession.bind(this)
        this.logout = this.logout.bind(this)
        this.isAuthenticated = this.isAuthenticated.bind(this)

        const redirectUri = configService.getRedirectUri()

        this.auth0 = new auth0.WebAuth({
            domain: 'watson-login.eu.auth0.com',
            clientID: 'idmn23Z2eXUomMLY1AwgDrhLe7DfzAJO',
            redirectUri: redirectUri,
            //audience: 'https://watson-login.eu.auth0.com/userinfo',
            audience: 'https://watson-service.eu-gb.mybluemix.net',
            responseType: 'token id_token',
            scope: 'openid profile'
        })
    }

    login () {
        this.auth0.authorize()
    }

    handleAuthentication() {
        this.auth0.parseHash((err, authResult) => {
            if (authResult && authResult.accessToken && authResult.idToken) {
                this.setSession(authResult)
            } else if (err) {
                console.log(err)
            }
        })
    }

    getUserProfile() {
        const userProfile = JSON.parse(localStorage.getItem('user_profile'))
        const userId = this.getUserId();
        
        if (userId === 1) {
            userProfile.name = 'DEMO User 1'
            userProfile.picture = require('../assets/img/user1.png')
        }
        if (userId === 2) {
            userProfile.name = 'DEMO User 2'
            userProfile.picture = require('../assets/img/user1.png')
        }     

        return userProfile;
    }

    getUserId() {
        return JSON.parse(localStorage.getItem('user_id'))
    }

    getAccessToken() {
        return localStorage.getItem('access_token')
    }

    getIdToken() {
        return localStorage.getItem('id_token')
    }

    isDemo() {
        const userId = this.getUserId()
        return (userId === 1 || userId === 2) 
    }

    setSession(authResult) {
        const expiresAt = JSON.stringify(authResult.expiresIn * 1000 + new Date().getTime())

        localStorage.setItem('access_token', authResult.accessToken)
        localStorage.setItem('id_token', authResult.idToken)
        localStorage.setItem('expires_at', expiresAt)

        Promise.all([
            this._retreiveUserProfile(),
            this._retreiveUserId()
        ]).then(() => { window.location = '/' })
    }

    _retreiveUserProfile() {
        const accessToken = this.getAccessToken()
        if (!accessToken) {
            return null
        }

        const self = this
        const promise = new Promise((resolve, reject) => {
            this.auth0.client.userInfo(accessToken, (err, userProfile) => {
                if (userProfile) {
                    localStorage.setItem('user_profile', JSON.stringify(userProfile))
                    resolve(userProfile)
                } else {
                    console.error(err)
                    reject(err)
                }
            })
        })

        return promise
    }

    _retreiveUserId() {
        const accessToken = this.getAccessToken()
        if (!accessToken) {
            return null
        }

        const self = this
        const promise = new Promise((resolve, reject) => {

            const config = {
                headers: {
                    'authorization': `Bearer ${accessToken}`
                }
            }

            const baseUrl = configService.getBaseUrl()
            axios.get(baseUrl + 'api/user/current', config).then(response => {
                localStorage.setItem('user_id', response.data.id)
                resolve(response.data.id)
            })
        })

        return promise
    }

    logout () {
        localStorage.removeItem('access_token')
        localStorage.removeItem('id_token')
        localStorage.removeItem('expires_at')
        localStorage.removeItem('user_profile')
        localStorage.removeItem('user_id')

        window.location = '/'
    }

    isAuthenticated () {
        const expiresAt = JSON.parse(localStorage.getItem('expires_at'))
        return new Date().getTime() < expiresAt
    }
}

export default new AuthService();
