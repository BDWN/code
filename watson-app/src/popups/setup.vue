<template>
    <f7-popup id="setupPopup">
        <f7-page navbar-fixed>
            <f7-navbar>
                <f7-nav-left>
                    <f7-link text="Close" close-popup></f7-link>
                </f7-nav-left>
                <f7-nav-center title="Profile Setup"></f7-nav-center>
                <f7-nav-right>
                </f7-nav-right>
            </f7-navbar>

            <div class="content-block inset"style="margin-top: 1rem; margin-bottom: 0;'">
                <div class="content-block-inner">
                    <p>For each of the paintings below, please select what you would be interested in finding out more about.</p>                 
                </div>
                <div class="content-block" v-if="isDemo">
                    <p><strong>NOTE:</strong> you are logged in as a DEMO user, so this predefined and read-only.</p>
                </div>
            </div>

            <f7-block style="margin-top: 1rem;">
                <img :src="samplePaintings[0]" style="display: block; margin: 0 auto;" width="100%">
                <div class="list-block" style="margin: 1rem 0;">
                    <ul>
                        <li>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Clothing" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Clothing</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Zeitgeist" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Zeitgeist</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Value" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Value</div></div></label>
                        </li>
                    </ul>
                </div>
                <img :src="samplePaintings[1]" style="display: block; margin: 0 auto;" width="100%">
                    <div class="list-block" style="margin: 1rem 0;">
                    <ul>
                        <li>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="People" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">People</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Profession" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Profession</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Date" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Date</div></div></label>
                        </li>
                    </ul>
                </div>
                <img :src="samplePaintings[2]" style="display: block; margin: 0 auto;" width="100%">
                    <div class="list-block" style="margin: 1rem 0;">
                    <ul>
                        <li>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Animals" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Animals</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Story" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Story</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Technique" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Technique</div></div></label>
                        </li>
                    </ul>
                </div>
                <img :src="samplePaintings[3]" style="display: block; margin: 0 auto;" width="100%">
                <div class="list-block" style="margin: 1rem 0;">
                    <ul>
                        <li>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Location" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Location</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Architecture" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Architecture</div></div></label>
                            <label class="label-checkbox item-content"><input :disabled="isDemo" type="checkbox" name="my-checkbox" value="Date" v-model="selected"><div class="item-media"><i class="icon icon-form-checkbox"></i></div><div class="item-inner"><div class="item-title">Date</div></div></label>
                        </li>
                    </ul>
                </div>
                <f7-button class="brown-button" style="margin-top: 2rem" @click.stop="saveProfile" fill>Save</f7-button>
            </f7-block>

        </f7-page>
    </f7-popup>
</template>

<script>
    import authService from '../services/authservice'
    import stateService from '../services/stateservice'
    import configService from '../services/configservice';
    import axios from 'axios'

    export default {

        computed: {

            currentItem: function()  {

                return this.setup[this.current];
            }
        },
        data() {
            let selection = []
            if (authService.isDemo()) {
                if (authService.getUserId() === 1) {
                    selection = ['Clothing', 'People', 'Animals', 'Location']
                }
                else {
                    selection = ['Value', 'Date', 'Technique', 'Date']
                }                
            }

            return {
                isDemo: authService.isDemo(),

                current: 0,

                selected: selection,

                samplePaintings: [
                    require('../assets/img/setup-paintings/1.jpg'),
                    require('../assets/img/setup-paintings/2.jpg'),
                    require('../assets/img/setup-paintings/3.jpg'),
                    require('../assets/img/setup-paintings/4.jpg'),
                ],

            }
        },
        methods: {
            saveProfile() {
                this.$f7.popup('#loadingPopup');
                const baseUrl = configService.getBaseUrl()

                const url = baseUrl + 'api/profile';
                const accessToken = authService.getAccessToken();

                const formData = new FormData();

                // We will never speak of this again
                let formattedSelection = {
                    "date": this.selected.includes("Date"),
                    "location": this.selected.includes("Location"),
                    "profession": this.selected.includes("Profession"),
                    "people": this.selected.includes("People"),
                    "technique": this.selected.includes("Technique"),
                    "story": this.selected.includes("Story"),
                    "value": this.selected.includes("Value"),
                    "zeitgeist": this.selected.includes("Zeitgeist"),
                    "animals": this.selected.includes("Animals"),
                    "architecture": this.selected.includes("Architecture"),
                    "clothing": this.selected.includes("Clothing")
                };

                formData.append('user', authService.getUserId());
                formData.append('concepts', JSON.stringify(formattedSelection));

                const config = {
                    headers: {
                        'content-type': 'application/x-www-form-urlencoded',
                        'authorization': `Bearer ${accessToken}`
                    }
                };

                axios.post(url, formData, config).then(response => {
                    this.$f7.closeModal('#loadingPopup');
                    this.$f7.closeModal('#setupPopup');
                    this.$f7.alert('You have successfully saved your preference profile', 'Saved profile')
                })
            },
        },
    }
</script>