<template>
    <f7-page>
        <f7-block-title>Welcome</f7-block-title>
        <f7-block inner>
            <p>The Mauritshuis is an art museum in The Hague in the Netherlands. The museum houses the Royal Cabinet of Paintings which consists of 841 objects, mostly Dutch Golden Age paintings. The collections contains works by Johannes Vermeer, Rembrandt van Rijn, Jan Steen, Paulus Potter, Frans Hals, Jacob van Ruisdael, Hans Holbein the Younger, and others. Originally, the 17th century building was the residence of count John Maurice of Nassau. It is now the property of the government of the Netherlands and is listed in the top 100 Dutch heritage sites.</p>
            <p>The Mauritshuis was privatised in 1995. The foundation set up at that time took charge of both the building and the collection, which it was given on long-term loan. This building, which is the property of the state, is rented by the museum. In 2007, the museum announced its desire to expand. In 2010, the definitive design was presented. The museum would occupy a part of the nearby Sociëteit de Witte building. The two buildings would be connected via an underground tunnel, running underneath the Korte Vijverberg. The renovation started in 2012 and finished in 2014. During the renovation, about 100 of the museum's paintings were displayed in the Gemeentemuseum in the Highlights Mauritshuis exhibition. About 50 other paintings, including the Girl With the Pearl Earring, were on loan to exhibitions in the United States and Japan. The museum was reopened on 27 June 2014 by King Willem-Alexander.</p>
        </f7-block>

        <f7-block v-if="!authenticated">
            <f7-button class="brown-button" @click.stop="login" fill>Login</f7-button>
        </f7-block>

        <f7-block v-if="authenticated && !profiled">
            <f7-button class="brown-button" @click.stop="openSetupPopup" fill>Start MH profile setup</f7-button>
        </f7-block>
    </f7-page>
</template>

<script>
    import authService from '../services/authservice';
    import stateService from '../services/stateservice';

    export default {
        data() {
            const authenticated = authService.authenticated
            const profiled = authenticated.profiled || false

            return {
                authenticated,
                profiled
            }
        },
        methods: {
            login() {
                authService.login();
            },
            openSetupPopup() {
                this.$f7.popup('#setupPopup')
            },
        }
    }
</script>