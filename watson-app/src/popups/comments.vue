<template>
  <f7-popup id="commentsPopup">
    <f7-page navbar-fixed>
      <f7-navbar>
        <f7-nav-left>
          <f7-link text="Close" close-popup></f7-link>
        </f7-nav-left>
        <f7-nav-center title="Comments"></f7-nav-center>
        <f7-nav-right>
        </f7-nav-right>
      </f7-navbar>

      <div v-for="comment in comments" class="card">
        <div class="card-header">
          <div class="avatar">
              <img class='avatar' :src="getPersonAvatar(comment.person.photo)" />
          </div>
          <div class="user flex-column">
            <div class="name">{{comment.person.name}}</div>
            <div class="time">a few seconds ago</div>
          </div>
        </div>
        <div class="card-content">
          <div class="text">
            <p>{{comment.description}}</p>
          </div>
        </div>
        <div class="card-footer flex-row">
          <f7-link class="tool tool-border flex-rest-width">
            <span class="icofont icofont-ui-rate-add"></span>
            <span class="text">Interresting!</span>
          </f7-link>
          <f7-link class="tool tool-border flex-rest-width">
            <span class="icofont icofont-ui-rate-remove"></span>
            <span class="text">Mhaww..</span>
          </f7-link>      
        </div>
      </div> 
      <f7-block>
        {{route}}
      </f7-block>
    </f7-page>
  </f7-popup>
</template>

<script>
  import axios from 'axios'
  import stateService from '../services/stateservice'
  import configService from '../services/configservice'
  import comment from '../components/comment'

  export default {
    props: [
      'postId'
    ],
    data() {
      return {
        comments: []
      }
    },
    computed: {
      route() {
        const self = this;

        if (this.postId > 0) {
          const baseUrl = configService.getBaseUrl()
          axios.get(`${baseUrl}api/post/${this.postId}/comments`).then(response => {
              self.comments = response.data;
          })
        }

        return `Dynamic route: post #${this.postId}`
      }
    },
    methods: {
      getPersonAvatar(photo) {
        return require('../assets/img/persons/' + photo);
      }
    },
    components: {
      comment
    }
  }
</script>