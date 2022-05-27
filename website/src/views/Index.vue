<template>
  <div>
    <v-dialog
        v-model="playerDialog"
        @click:outside="closeDialog"
        :max-width="playerWidth"
        :eager="true"
    >
      <v-card>
        <video-player class="video-player-box"
                      ref="videoPlayer"
                      :options="playerOptions"
                      :playsinline="true"
        >
        </video-player>
      </v-card>
    </v-dialog>

    <v-container>
      <v-row
          justify="center"
          no-gutters
      >
        <v-combobox
            v-model="searchMembers"
            :items="memberItems"
            multiple
            style="max-width: 450px;"
            @change="searchChange"
        >
          <template v-slot:selection="{index, item}">
            <div v-if="getCPName() !== ''">
              <v-chip
                  v-if="index === 1"
                  label
              >
                {{ getCPName() }}
              </v-chip>
            </div>
            <v-chip
                v-else
                label
            >
              {{ item.text }}
            </v-chip>
          </template>

          <template v-slot:item="{ index, item }">
            <v-avatar size="35" class="mr-3">
              <v-img :src="members[item.value].avatar_url"></v-img>
            </v-avatar>
            <span>{{ item.text }}</span>
          </template>
        </v-combobox>
      </v-row>
    </v-container>


    <v-container>
      <v-row dense>
        <v-col
            v-for="(v, index) in videos"
            :key="v.id"
            :xl="3"
            :lg="3"
            :md="3"
            :sm="12"
        >
          <v-card>
            <v-img
                :ref="`cover-${index}`"
                :src="v.dynamic_cover_urls[0]"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="480px"
            >
              <v-card-title v-text="v.description"></v-card-title>
              <v-row class="pl-7 pb-5 pt-1">
                <v-icon color="red lighten-2" dense>mdi-heart</v-icon>
                <span class="white--text mr-2">{{ v.statistic.digg }}</span>

                <v-icon color="white">mdi-share</v-icon>
                <span class="white--text mr-2"> {{ v.statistic.share }}</span>

                <v-icon color="white" small>mdi-comment</v-icon>
                <span class="white--text"> {{ v.statistic.comment }}</span>
              </v-row>
            </v-img>

            <v-card-actions>
              <v-avatar size="36px">
                <img :src="v.author.avatar_url" :alt="v.author.name"/>
              </v-avatar>
              <v-spacer></v-spacer>
              <span class="grey--text text--darken-1">{{ new Date(v.created_at * 1000).toLocaleString().replace(/:\d{1,2}$/,' ') }}</span>
              <v-spacer></v-spacer>
              <v-btn icon @click="playVideo(v)">
                <v-icon>mdi-play</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon @click="downloadVideo(v)">mdi-download</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col
            :xl="3"
            :lg="3"
            :md="3"
            :sm="12"
        >
          <v-skeleton-loader
              v-if="isLoading"
              class="mx-auto"
              type="card"
          ></v-skeleton-loader>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
import 'video.js/dist/video-js.css'
import {videoPlayer, videojs} from 'vue-video-player'

window.videojs = videojs
require("video.js/dist/lang/zh-CN")
window.videojs.addLanguage('zh-CN', {
      "The media could not be loaded, either because the server or network failed or because the format is not supported.":
          '小伙伴你好，该视频被羊驼删除了 ✋🏻 小伙伴看看别的视频吧~'
    }
);

export default {
  name: "Index",

  data() {
    return {
      isLoading: true,
      isEnd: false,
      currentPage: 1,
      playerDialog: false,
      playerWidth: 360,
      playerOptions: {
        loop: true,
        fluid: true,
        autoplay: true,
        muted: false,
        playbackRates: [0.5, 1.0, 1.5, 2.0],
        sources: [{
          type: "video/mp4",
          src: ''
        }],
        lang: 'zh-CN',
      },
      videos: [],

      searchString: '',
      searchMembers: [],
      members: {},
      memberItems: [
        {
          text: '向晚 Ava',
          value: '2497695890809629',
          key: 1 << 0
        },
        {
          text: '贝拉 Bella',
          value: '1389388146161774',
          key: 1 << 1
        },
        {
          text: '珈乐 Carol',
          value: '3570819240827502',
          key: 1 << 2
        },
        {
          text: '嘉然 Diana',
          value: '756069459828192',
          key: 1 << 3
        },
        {
          text: '乃琳 Eileen',
          value: '4485612889456440',
          key: 1 << 4
        },
        {
          text: 'A-SOUL Official',
          value: '1002373479924424',
          key: 1 << 5
        },
      ]
    }
  },

  mounted() {
    this.getMembers()
    this.getVideos()
    this.onScroll()
  },

  methods: {
    getVideos() {
      return new Promise((resolve, reject) => {
        if (this.isEnd) {
          resolve()
          return
        }
        this.isLoading = true

        let uids = []
        console.log(this.searchMembers)
        this.searchMembers.forEach((item) => {
          uids.push(item.value)
        })

        axios.get('https://douyin.bytedancer.cc/api/videos', {
          params: {
            page: this.currentPage,
            keyword: this.searchString,
            uid: uids,
          },
          paramsSerializer: params => {
            return qs.stringify(params, {indices: false})
          }
        }).then(res => {
          if (res.data.data.length === 0) {
            this.isEnd = true
          }

          this.videos = this.videos.concat(res.data.data)
          this.isLoading = false
          resolve()
        }).catch(err => {
          this.isLoading = false
          reject(err)
        })
      })
    },

    getMembers() {
      return new Promise((resolve, reject) => {
        axios.get('https://douyin.bytedancer.cc/api/members').then(res => {
          res.data.data.forEach((value) => {
            this.members[value.uid] = value
          })
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },

    playVideo(v) {
      if (v.video_width == 2160) {
        this.playerWidth = v.video_width / 6
      } else if (v.video_height > v.video_width) {
        this.playerWidth = v.video_width / 3
      } else {
        this.playerWidth = v.video_width / 6 * 2
      }

      this.playerDialog = true
      this.playerOptions.sources[0].src = `https://aweme.snssdk.com/aweme/v1/play/?video_id=${v.vid}&ratio=720p&line=0`
      this.playerOptions.sources[0].poster = v.dynamic_cover_urls[0]
      if (this.$refs.videoPlayer !== undefined) {
        this.$refs.videoPlayer.player.play()
      }
    },

    closeDialog() {
      this.$refs.videoPlayer.player.pause()
    },

    downloadVideo(v) {
      window.open(`https://aweme.snssdk.com/aweme/v1/play/?video_id=${v.vid}&ratio=720p&line=0`)
    },

    onScroll() {
      let isLoading = false
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.offsetHeight - document.documentElement.scrollTop - window.innerHeight <= 200
        if (bottomOfWindow && isLoading === false) {
          isLoading = true
          this.currentPage++
          this.getVideos().then(() => {
            isLoading = false
          }).catch(() => {
            isLoading = false
          })
        }
      }
    },

    searchChange() {
      this.isEnd = false
      this.videos = []
      this.currentPage = 1
      this.getVideos()
    },

    resetSearch() {
      this.searchString = ''
    },

    getCPName() {
      let index = 0
      this.searchMembers.forEach((item) => {
        index += item.key
      })

      // 向晚 000001
      // 贝拉 000010
      // 珈乐 000100
      // 嘉然 001000
      // 乃琳 010000
      // 阿草 100000
      const cp = [
        '', // 0
        '', // 1 向晚
        '', // 2 贝拉
        '憨次方', // 3 向晚 贝拉
        '', // 4 珈乐
        '萤火虫', // 5 向晚 珈乐
        '贝贝珈', // 6 贝拉 珈乐
        '', // 7 向晚 贝拉 珈乐
        '', // 8 嘉然
        '嘉晚饭', // 9 向晚 嘉然
        '超级嘉贝', // 10 贝拉 嘉然
        '', // 11 向晚 贝拉 嘉然
        'C++', // 12 珈乐 嘉然
        '', // 13 向晚 珈乐 嘉然
        '', // 14 贝拉 珈乐 嘉然
        '', // 15 向晚 贝拉 珈乐 嘉然
        '', // 16 乃琳
        '果丹皮', // 17 向晚 乃琳
        '乃贝', // 18 贝拉 乃琳
        '', // 19 向晚 贝拉 乃琳
        '珈特琳', // 20 珈乐 乃琳
        '', // 21 向晚 珈乐 乃琳
        '', // 22 贝拉 珈乐 乃琳
        '', // 23 向晚 贝拉 珈乐 乃琳
        '琳嘉女孩', // 24 嘉然 乃琳
        '', // 25 向晚 嘉然 乃琳
        '', // 26 贝拉 嘉然 乃琳
        '', // 27 向晚 贝拉 嘉然 乃琳
        '', // 28 珈乐 嘉然 乃琳
        '', // 29 向晚 珈乐 嘉然 乃琳
        '', // 30 贝拉 珈乐 嘉然 乃琳
        'A-SOUL 全员', // 31 向晚 贝拉 珈乐 嘉然 乃琳
      ]
      return cp[index] ?? ''
    }
  },

  components: {
    videoPlayer
  }
}
</script>

<style scoped>

</style>
