// External imports
import Vue from 'vue'
import Framework7 from 'framework7'
import Framework7Vue from 'framework7-vue'
import Framework7Theme from 'framework7/dist/css/framework7.ios.min.css'
import Framework7ThemeColors from 'framework7/dist/css/framework7.ios.colors.min.css'

// Internal imports
import authService from './services/authservice';
import Routes from './routes.js'
import App from './app'

// Imports assets
import './assets/css/app.css'
import './assets/fonts/icofont.css'

// Register plugins
Vue.use(Framework7Vue)

// Initialize
let isAuthenticating = false
const app = new Vue({
  el: '#app',
  template: '<app/>',
  framework7: {
    root: '#app',
    routes: Routes,
    onPageInit: function (app, page) {
      const parser = document.createElement('a')
      parser.href = app.root[0].baseURI

      if (parser.pathname === '/callback' && !isAuthenticating) {
        isAuthenticating = true
        
        app.popup('#loadingPopup')
        localStorage.setItem('isAuthenticating', 'yes')
        authService.handleAuthentication()
      } else if (parser.pathname !== '/callback' && localStorage.getItem('isAuthenticating') === 'yes') {
        localStorage.setItem('isAuthenticating', 'no')
        app.popup('#setupPopup')
      }
    }    
  },
  components: {
    app: App
  }
})

export default app