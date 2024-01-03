<template>

    <div class="p-4 w-full ">

        <div class="text-center">
            <div v-show="isCompleted" class="p-4 mt-20 mb-4 text-xl text-green-900 rounded-lg bg-green-100">{{ popupMessage
            }}</div>
            <div v-show="isFailed" class="p-4 mt-20 mb-4 text-xl text-red-900 rounded-lg bg-red-100">{{ popupMessage }}
            </div>
            <p behavior="" v-show="!isCompleted && !isFailed">
            <h2 style="color: green;" class="blink p-2 mt-20 text-2xl">
                Please do not refresh or close this page until the progress
                is completed !!
            </h2>
            </p>
        </div>

        <div class="mt-5 p-4">
            <div class=" h-auto border-2 shadow-md sm:rounded-lg">
                <div class="px-5 pb-5" v-show="!isCompleted">
                    <div class="text-center">
                        <h1
                            class="p-2 text-gray-300 font-bold text-2xl uppercase  bg-gray-50 dark:bg-gray-800">
                            Rules Are Applying .....</h1>

                        <h2 class="p-4">Rules Status</h2>
                    </div>

                    <div class="progress-container">
                        <div class="completion-container" id="completion-container">

                            <!-- <div class="loader" id="loader" v-show="!isCompleted"></div> -->
                            <div class="text-center mb-5">
                                <div role="status" v-show="!isCompleted && !isFailed">
                                    <svg aria-hidden="true"
                                        class="inline w-10 h-10 text-purple-500 animate-spin dark:text-gray-200 fill-green-400"
                                        viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                                            fill="currentColor" />
                                        <path
                                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                                            fill="currentFill" />
                                    </svg>
                                    <span class="sr-only">Loading...</span>

                                </div>
                                <div class="mt-3">
                                    <div class="center-content success-mark" id="success-mark" v-show="isCompleted">&#10004;
                                    </div>
                                    <div class="center-content failure-mark text-2xl" id="failure-mark" v-show="isFailed">
                                    </div>
                                    <div class="completion-status text-2xl" id="completion-status" v-text="completionText"
                                        :style="{ color: completionColor }"></div>
                                </div>
                            </div>


                            <div class="w-full bg-gray-200 rounded-full dark:bg-gray-200">
                                <div class="loader bg-purple-700 text-xs font-medium text-white text-center p-0.5 leading-none rounded-full"
                                    id="loader" :style="{ width: progress }">{{ progress }}</div>
                            </div>


                            <div v-for="(status, index) in latestPipelineStatus" :key="index">
                                <p id="latest-pipeline-status" class="pipeline-status">{{
                                    status }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-show="isCompleted">
                    <div class="p-4 text-center">
                        <ul v-if="showcred">
                            <h2 class="text-blue-900 p-2 mt-20 text-2xl">
                                We are redirecting you to the rules list page. If you are not redirected,
                                <a @click.prevent="RedirectclusterPage" class="text-blue-400"> click here</a>
                            </h2>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from "axios";
import leftSidebar from '@/components/leftSidebar.vue'

export default {
    components: {
        leftSidebar,
    },


    data() {

        return {
            isDropdownOpen: false,
            ProjectToggle: false,
            UserToggle: false,
            Username: '',
            user_id: null,
            projects: [],
            selectedProject: "",
            clusters: [],
            isCompleted: false,
            isFailed: false,
            completionText: 'Loading...',
            completionColor: '',
            averageProgress: 0,
            latestPipelineStatus: '',
            extractedArtifacts: [],
            stopFetching: false,
            isPopupVisible: false,
            popupMessage: "", showcred: false,

        };
    },

    methods: {
        RedirectclusterPage() {
            this.$router.push("/overview");
        },
        logout() {
            console.log("logout");
            sessionStorage.removeItem('user_id');
            sessionStorage.removeItem('username');
            sessionStorage.removeItem('project_id');
            sessionStorage.removeItem('project_name');
            window.location.reload()
        },
        getFirstLetter(username) {
            return username.charAt(0, 1).toUpperCase();
        },
        toggleDarkMode() {
            this.toggleDark();
        },

        toggleDropdown() {

            this.isDropdownOpen = !this.isDropdownOpen
        },

        userToggle() {
            this.UserToggle = !this.UserToggle;
        },

        async updateLatestPipelineStatusAndArtifacts() {
            if (this.stopFetching) {
                return;
            }
            const url = 'http://127.0.0.1:8000/api/v2/get_pipeline_status/';

            try {
                const response = await axios.get(url);
                const data = response.data;

                // Update the component's data properties based on the received data
                this.averageProgress = this.calculateAverageProgress(data.pipelines);

                this.isCompleted = this.averageProgress === 100;
                this.isFailed = this.averageProgress === 99;
                this.completionText = this.isCompleted ? 'Completed' : (this.isFailed ? 'Failed' : 'Loading...');
                this.completionColor = this.isCompleted ? 'green' : (this.isFailed ? 'red' : '');

                this.latestPipelineStatus = data.pipelines.map(pipeline => `Rule Applying Status : ${pipeline.status}`);
                this.artifacts = this.extractArtifacts(data.pipelines);
            } catch (error) {
                console.error('Error fetching data:', error);
            }

            if (this.isCompleted) {
                console.log("Success");
                this.showSuccessPopup();
            } else if (this.isFailed) {
                console.log("Failed");
                this.showFailedPopup();
            }

            setTimeout(this.updateLatestPipelineStatusAndArtifacts, 5000);
        },
        calculateAverageProgress(pipelines) {
            let totalProgress = 0;
            let numPipelines = pipelines.length;

            pipelines.forEach(pipeline => {
                switch (pipeline.status) {
                    case 'created':
                        totalProgress += 10;
                        break;
                    case 'pending':
                        totalProgress += 25;
                        break;
                    case 'running':
                        totalProgress += 50;
                        break;
                    case 'success':
                        totalProgress += 100;
                        break;
                    case 'failed':
                        // Handle 'failed' status separately (you can adjust the value as needed)
                        totalProgress += 99.9;
                        break;
                    default:
                        // Handle other statuses if needed
                        break;
                }
            });

            // Calculate the average progress
            let averageProgress = Math.floor(totalProgress / numPipelines);

            return averageProgress;
        },

       
        showSuccessPopup() {
            this.popupMessage = "Selected rules applied successfully!";

            this.showcred = true
            setTimeout(() => {

                // Redirect to the overview page here
                this.$router.push("/rules");
            }, 10000);
        },

        showFailedPopup() {
            console.log("faild");
            this.popupMessage = "Failed to apply rules. Please try again.";

            this.showcred = true
            setTimeout(() => {

                // Redirect to the overview page here
                this.$router.push("/rules");
            }, 10000);
        },
        addLineBreaks(text) {
            // Replace '\n' with '<br>' for rendering line breaks in HTML
            return text.replace(/\n/g, '<br>');
        },


    },

    created() {
        this.Username = sessionStorage.getItem('username');
    },

    computed: {
        progress() {
            return this.averageProgress + '%'
        }
    },
    // beforeMount(){
    //     window.location.reload()
    // },
    mounted() {
        setTimeout(() => {
            console.log("after 10sec. mount mtd run");
            this.updateLatestPipelineStatusAndArtifacts();
        }, 10000);

        // setInterval(this.updateLatestPipelineStatusAndArtifacts, 5000);
    },
    unmounted() {
        console.log("unmount");
        this.popupMessage = '',
        // window.location.reload()
        this.stopFetching = true;
    },
    beforeUnmount() {
        this.stopFetching = true
        this.popupMessage = '',
        console.log("before-unmount");
        window.location.reload();
        // this.stopFetching = true

    }

};
</script>

<style scoped>
.blink {
    animation:
        blinker 1.5s linear infinite;
    color:
        red;
    font-family:
        sans-serif;
}

@keyframes blinker {
    50% {
        opacity:
            0;
    }
}
</style>
  
  