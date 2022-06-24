<template>
  <v-app>
    <v-dialog v-model="buyCoffee" @click:outside="toggleBuyMeACoffee" :max-width="Width" :eager="true">
      <v-card>
        <v-img src="https://bytedancer.cc/static/pay.png" width="1118px"></v-img>
      </v-card>
    </v-dialog>
    <v-dialog :max-width="Width" v-model="info" @click:outside="toggleInfo">
      <v-card loading elevation="24">
        <v-card class="mx-auto" max-width="400">
          <v-list-item two-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5">
                A-SOUL Archive
              </v-list-item-title>
              <v-list-item-subtitle>Just for A-SOUL ♡</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-card-text>
            <v-row class="justify-space-around">
              <v-col disabled align="center" cols="6">
                <v-icon size="64">mdi-eye</v-icon>
              </v-col>
              <v-col disabled v-model="websiteInfo" align="center" class="text-h2" cols="6">
               {{ websiteInfo.visitors }}
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-text>
            <v-row class="justify-space-around">
              <v-col disabled align="center" cols="6">
                <v-icon size="64">mdi-chip</v-icon>
              </v-col>
              <v-col disabled v-model="websiteInfo" align="center" class="text-h2" cols="6">
                {{ websiteInfo.cpu_usage }}%
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-text>
            <v-row class="justify-space-around">
              <v-col disabled align="center" cols="6">
                <v-icon size="64">mdi-memory</v-icon>
              </v-col>
              <v-col disabled v-model="websiteInfo" align="center" class="text-h2" cols="6">
                {{ websiteInfo.memory_usage }}%
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-text>
            <v-row class="justify-space-around">
              <v-col disabled align="center" cols="6">
                <v-icon size="64">mdi-swap-horizontal-variant</v-icon>
              </v-col>
              <v-col disabled v-model="websiteInfo" align="center" class="text-h2" cols="6">
                {{ websiteInfo.swap_usage }}%
              </v-col>
            </v-row>
          </v-card-text>
          <!-- <v-slider v-model="time" :max="6" :tick-labels="labels" class="mx-4" ticks></v-slider> -->
        </v-card>
      </v-card>
    </v-dialog>
    <v-app-bar app>
      <div class="dark--text text-h4">
        <b>A-SOUL</b>
      </div>
      <v-spacer></v-spacer>
      <!-- <v-btn color="info" dark @click="toggleBuyMeACoffee">
        Buy me a coffee
        <v-icon right dark>
          mdi-coffee
        </v-icon>
      </v-btn> -->
      <v-btn class="ma-2" color="info" dark href="https://github.com/ElieenAndBella/A-SOUL-Archive/issues"
        target="_blank">
        Bug Report
        <v-icon right dark>
          mdi-bug
        </v-icon>
      </v-btn>
      <v-btn color="info" @click="toggleDarkTheme">
        <v-icon>
          mdi-white-balance-sunny
        </v-icon>
      </v-btn>
      <v-btn color="info" class="ma-2" @click="toggleInfo">
        <v-icon>mdi-run</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>


<script>
import { createSocket } from './plugins/websocket';


export default {
  name: 'App',

  data() {
    return {
      labels: ['SU', 'MO', 'TU', 'WED', 'TH', 'FR', 'SA'],
      time: 0,
      Width: 400,
      // buyCoffee: false,
      info: false,
      getsocketData: null,
      websiteInfo: {}
    }
  },

  mounted() {
    this.wsInit()
  },

  methods: {
    wsInit() {
      createSocket("wss://asoul.bytedancer.cc/websocket")
      // 接收消息
      this.getsocketData = e => {  // 创建接收消息函数
        console.log(e && e.detail.data)
        this.websiteInfo = JSON.parse(e.detail.data)
      }
      // 注册监听事件
      window.addEventListener('onmessageWS', this.getsocketData)
    },
    toggleDarkTheme() {
      this.$vuetify.theme.isDark = !this.$vuetify.theme.isDark
    },
    // toggleBuyMeACoffee() {
    //   this.buyCoffee = !this.buyCoffee
    // },
    toggleInfo() {
      this.info = !this.info
    }
  },

  destroyed() {
    // 在需要的时候卸载监听事件，比如离开页面
    window.removeEventListener('onmessageWS', this.getsocketData)
  }
};
</script>
