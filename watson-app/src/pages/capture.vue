<template>
  <f7-page>
    <div class="editor-container">
      <textarea type="textarea" placeholder="What do you like about the painting in front of you?" v-model="description" value="text"></textarea>
      <ul class="tools flex-row">
        <f7-link @click.stop="changePhoto" class="tool tool-border flex-rest-width">
          <span class="icofont icofont-ui-camera"></span>
          <span class="text">{{changePhotoText}}</span>
        </f7-link>
        <f7-link :disabled="!photoSelected" @click.stop="savePost" class="tool tool-border flex-rest-width">
          <span class="icofont icofont-save"></span>
          <span class="text">Save</span>
        </f7-link>
      </ul>
    </div>

    <f7-block>
      <picture-input
          ref="pictureInput"
          @change="onChange"
          width="250"
          height="250"
          :plain="true"
          margin="16"
          accept="image/jpeg,image/png"
          size="10"
          buttonClass="hide"
          :customStrings="{
            upload: '<h1>Bummer!</h1>',
            drag: ''
          }">
        </picture-input>
    </f7-block>
  </f7-page>
</template>

<script>
  import PictureInput from 'vue-picture-input'
  import axios from 'axios'
  import authService from '../services/authservice'
  import configService from '../services/configservice'

  export default {
    data () {
      return {
        description: '',
        photoSelected: false
      }
    },
    computed: {
      changePhotoText() {
        if (this.photoSelected) {
          return 'Change photo'
        }

        return 'Add photo'
      }
    },
    components: {
      PictureInput
    },
    methods: {
      onChange () {
        if (this.$refs.pictureInput.image) {
          this.photoSelected = true
        } else {
          this.photoSelected = false
        }
      },
      changePhoto() {
        this.$refs.pictureInput.resizeCanvas()
        this.$refs.pictureInput.selectImage()
      },
        savePost: function() {
            this.$f7.popup('#loadingPopup')
            const baseUrl = configService.getBaseUrl()
    
            const file = this.$refs.pictureInput.file
            const url = baseUrl + 'api/post'
            const accessToken = authService.getAccessToken()

            const formData = new FormData()
            formData.append('description', this.description)
            formData.append('photo', file)

            const config = {
                headers: {
                    'content-type': 'multipart/form-data',
                    'authorization': `Bearer ${accessToken}`
                }
            }

            axios.post(url, formData, config).then(response => {
                this.$refs.pictureInput.removeImage()
                this.photoSelected = false
                this.description = ''

                this.$f7.closeModal('#loadingPopup')
                this.$f7.alert('You have created a new post!', 'Post Created')
            })
        }
    }
  }
</script>