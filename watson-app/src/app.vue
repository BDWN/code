<template>
    <div id="app">

        <f7-statusbar></f7-statusbar>

        <f7-views>
            <f7-view id="main-view" navbar-through :dynamic-navbar="true" main>
                <f7-navbar>
                    <f7-nav-center sliding>SmartGuide (PoC)</f7-nav-center>
                </f7-navbar>

                <f7-pages>
                    <f7-page toolbar-fixed navbar-fixed>
                        <f7-toolbar tabbar labels>
                            <f7-link icon="icofont icofont-ui-home" text="Home" tab-link="#home" active></f7-link>
                            <f7-link icon="icofont icofont-ui-social-link" v-if="authenticated" text="Posts" tab-link="#network"></f7-link>
                            <f7-link icon="icofont icofont-ui-image" v-if="authenticated" text="Capture" tab-link="#capture"></f7-link>
                            <f7-link icon="icofont icofont-ui-user" v-if="authenticated" text="Account" tab-link="#account"></f7-link>
                            <f7-progressbar ref="XpProgress" :progress="47" v-if="authenticated" color="green" style="height: 1.0rem; margin-right: .5rem;"></f7-progressbar>
                        </f7-toolbar>
                        <f7-tabs>
                            <f7-tab id="home" active @tab:show="tabChanged('home')">
                                <home v-on:xp="updateXp"></home>
                            </f7-tab>
                            <f7-tab v-if="authenticated" id="network" @tab:show="tabChanged('network')">
                                <network></network>
                            </f7-tab>
                            <f7-tab v-if="authenticated" id="capture" @tab:show="tabChanged('capture')">
                                <capture></capture>
                            </f7-tab>
                            <f7-tab v-if="authenticated" id="account" @tab:show="tabChanged('account')">
                                <account :xp="this.xp" v-on:xp="updateXp"></account>
                            </f7-tab>
                        </f7-tabs>
                    </f7-page>
                </f7-pages>
            </f7-view>
        </f7-views>

        <comments :postId="activePostId"></comments>
        <setup></setup>
        <loading></loading>
    </div>
</template>

<script>
    import authService from './services/authservice';
    import stateService from './services/stateservice';

    import home from './pages/home';
    import network from './pages/network';
    import capture from './pages/capture';
    import account from './pages/account';
    import comments from './popups/comments';
    import setup from './popups/setup';
    import loading from './popups/loading';

    export default {
        data() {
            const authenticated = authService.authenticated
            const activePostId = stateService.getActivePost()

            stateService.subscribe(() => {
                this.activePostId = stateService.getActivePost()
            })

            return {
                authenticated,
                activePostId,
                activeTab: 'home',
                xp: 2350,
            }
        },
        methods: {
            tabChanged(tab) {
                this.activeTab = tab
            },
            updateXp() {
                this.xp = stateService.getXp();
                this.$refs.XpProgress.set((this.xp / 5000) * 100, 500);
            }
        },
        components: {
            home,
            network,
            capture,
            account,
            comments,
            setup,
            loading
        },
    }
</script>
