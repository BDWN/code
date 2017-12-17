<template>
  <div class="network">
    <f7-block>
      <f7-button class="brown-button" @click.stop="refresh" fill>Refresh</f7-button>
    </f7-block>
    <card v-for="(item, index) in timeline" :key="item.id" :data="item"></card>  
  </div>
</template>

<script>
  import axios from 'axios'
  import authService from '../services/authservice';
  import configService from '../services/configservice';
  import card from '../components/card.vue'

  export default {
    data() {
      this.refresh()

      return {
        timeline: []
      }
    },
    methods: {
      refresh() {
        const userId = authService.getUserId()
        if (userId) {
          const self = this;
          const baseUrl = configService.getBaseUrl()
          axios.get(`${baseUrl}api/user/${userId}/posts`).then(response => {
            self.timeline = response.data
          })
        }
      }      
    },
    components: {
      card
    } 
  }
</script>