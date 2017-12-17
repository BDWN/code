
class ConfigService {
    getBaseUrl() {
        //return 'http://localhost:5000/'
        return 'https://watson-service.eu-gb.mybluemix.net/'
    }

    getRedirectUri() {
        //return 'http://localhost:8081/callback'
        return 'https://watson-app-dev.eu-gb.mybluemix.net/callback'        
    }
}

export default new ConfigService();