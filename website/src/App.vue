<template>
  <v-app>
    <v-dialog v-model="buyCoffee" @click:outside="toggleBuyMeACoffee" :max-width="coffeeWidth" :eager="true">
      <v-card>
        <v-img src="https://bytedancer.cc/static/pay.png" width="1118px"></v-img>
      </v-card>
    </v-dialog>
    <v-app-bar app>
      <div class="dark--text text-h4">
        <b>A-SOUL</b>
      </div>
      <v-spacer></v-spacer>
      <v-btn color="info" dark @click="toggleBuyMeACoffee">
        Buy me a coffee
        <v-icon right dark>
          mdi-coffee
        </v-icon>
      </v-btn>
      <v-btn class="ma-2" color="info" dark href="https://github.com/ElieenAndBella/A-SOUL-Archive/issues"
        target="_blank">
        Bug Report
        <v-icon right dark>
          mdi-wrench
        </v-icon>
      </v-btn>
      <v-btn color="info" @click="toggleDarkTheme">
        <v-icon>
          mdi-white-balance-sunny
        </v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>


<script>
export default {
  name: 'App',

  data() {
    return {
      coffeeWidth: 400,
      buyCoffee: false
    }
  },

  methods: {
    toggleDarkTheme() {
      this.$vuetify.theme.isDark = !this.$vuetify.theme.isDark
    },
    toggleBuyMeACoffee() {
      this.buyCoffee = !this.buyCoffee
    }
  }
};
</script>
