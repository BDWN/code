<template>
    <div class="account-view">
        <f7-list class="user-profile">
            <f7-list-item :media="avatar">
                <div slot="inner-start" class="detail">
                    <div class="name">{{userProfile.name}}</div>
                    <div class="location">
                        <span>Amsterdam, Netherlands</span>
                    </div>
                </div>
                <f7-button class="brown-button" @click.stop="logout" fill>Logout</f7-button>
            </f7-list-item>
        </f7-list>
        <div class="content-block inset">
            <div class="content-block-inner">
                <div style="text-align: center; margin-bottom: 1.0rem">
                    You can earn experience points by creating posts and providing feedback to comments!<br/>
                    <div style="padding-top: .5rem">
                        Creating new post: <strong>50XP</strong><br/>
                        Providing feedback: <strong>100XP</strong>
                    </div>
                </div>
                <f7-progressbar ref="XpProgress" :progress="47" color="green" style="height: 2.0rem;"></f7-progressbar>
                <div style="text-align: center; margin-top: .5rem">
                    Your XP: <strong>{{ this.xp }}/5000</strong>
                </div>
                <f7-block style="margin: 1rem 3rem .25rem 3rem;">
                    <f7-button class="brown-button" @click.stop="incrementXp(50)" fill>Increment XP</f7-button>
                </f7-block>
            </div>
        </div>
        <f7-list>
            <f7-list-item title="Language" link="#" @click.stop="nope" media="<i class='icofont icofont-chat'></i>"></f7-list-item>
            <f7-list-item title="Feedback" link="#" @click.stop="nope" media="<i class='icofont icofont-megaphone-alt'></i>"></f7-list-item>
        </f7-list>
        <f7-block>
            <f7-button class="brown-button" @click.stop="user" fill>User</f7-button>
        </f7-block>
        <f7-block>
            <f7-button class="brown-button" @click.stop="tokens" fill>Tokens</f7-button>
        </f7-block>
    </div>
</template>

<style>
    .location{
        color: #858585;
        font-size: 15px;
        margin-top: 5px;
    }
</style>

<script>
    import authService from '../services/authservice';
    import stateService from '../services/stateservice';

    export default {
        data() {
            const authenticated = authService.authenticated
            const userProfile = authService.getUserProfile()       

            return {
                authenticated: authenticated,
                userProfile: userProfile,
                avatar: `<img class='avatar' src=${userProfile.picture} />`,
            }
        },
        methods: {
            incrementXp(val) {
                if (stateService.getXp() < 5000) {
                    stateService.setXp(stateService.getXp() + val);
                    this.$emit("xp");
                }
            },
            logout() {
                authService.logout();
            },
            nope() {
                window.f7.alert("This isn't feature you're looking for..", 'NOPE!')
            },
            tokens() {
                this.$f7.alert(authService.getAccessToken(), 'Access Token')
                this.$f7.alert(authService.getIdToken(), 'ID Token')
            },
            user() {
                this.$f7.alert(JSON.stringify(authService.getUserProfile()), 'User Profile')
                this.$f7.alert(JSON.stringify(authService.getUserId()), 'User ID')
            }
        },
        props: [
            'xp',
        ],
        watch: {
            xp: function() {
                this.$refs.XpProgress.set((stateService.getXp() / 5000) * 100, 500);
            }
        }
    }
</script>
