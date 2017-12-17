<template>
  <div class="card">
    <div class="card-header">
      <div class="avatar">
          <img class='avatar' :src="userProfile.picture" />
      </div>
      <div class="user flex-column">
        <div class="name">{{userProfile.name}}</div>
        <div class="time">{{formatTime(data.creation_timestamp)}}</div>
      </div>
    </div>
    <div class="card-content">
      <div class="text" v-html="highlightHashtags(data.description)"></div>
      <div class="image" @click.stop="openPhotoBrowser(getPhotoUrl(data.photo))">
          <img :src="getPhotoUrl(data.photo)" />
      </div>
    </div>
    <div class="card-footer flex-row">
      <f7-link class="tool tool-border flex-rest-width" @click.stop="openCommentsPopup">
        <span class="icofont icofont-comment"></span>
        <span class="text">Comments</span>
      </f7-link>
      <f7-link @click.stop="nope" class="tool tool-border flex-rest-width">
        <span class="icofont icofont-share"></span>
        <span class="text">Share on FB</span>
      </f7-link>      
    </div>
  </div>
</template>

<script>
import authService from '../services/authservice'
import stateService from '../services/stateservice'
import moment from 'moment'

export default {
  props: {
    data: {
      type: Object,
      default() {
        return {}
      }
    },
    enableToolbar: {
      type: Boolean,
      default: true
    }
  },
  data() {
      const userProfile = authService.getUserProfile()

      return {
        userProfile    
      }
  },
  methods: {
    contentClick(data) {
      this.$emit('card:content-click', data)
    },
    openPhotoBrowser(url) {
      let pb = this.$f7.photoBrowser({
        zoom: 400,
        theme: 'dark',
        toolbar: false,
        photos: [url]
      })
      pb.open()
    },
    openCommentsPopup() {
        stateService.setActivePost(this.data.id)
        this.$f7.popup('#commentsPopup')
    },     
    formatTime(time) {
      return moment(time.substring(0, time.lastIndexOf(' '))).fromNow()
    },
    highlightHashtags(description) {
      const x = description.lastIndexOf('#')
      if (x === -1) {
        return description
      }

      return `${description.substring(0, x)} <span class='hashtag'>${description.substring(x)}</span>`
    },
    getPhotoUrl(photo) {
      return `http://s3.eu-geo.objectstorage.softlayer.net/photos-bucket/${photo}`
    },
    nope() {
      window.f7.alert("This isn't feature you're looking for..", 'NOPE!')
    }        
  }
}
</script>