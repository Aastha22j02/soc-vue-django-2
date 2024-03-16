<template>
    <navBar />
    <div class="flex fixed mt-16">
        <!-- leftsider bar -->
        <leftSidebar />
        <!-- <div :class="['h-screen p-5 pt-8 relative    bg-blue-800 ', store.open ? 'w-72' : 'w-20']"> -->
        <!-- center panel -->
        <div :class="['h-screen pb-5 flex-1 flex flex-col overflow-hidden', isOpen ? 'w-[1600px]' : 'w-[1800px]']">           
             <div class="flex-1 overflow-x-hidden overflow-y-auto p-7">
                <div v-show="loading" class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                    <div class="bg-white bg-transparent  p-8 rounded-lg flex items-center">
                        <div class="mr-4 animate-spin rounded-full h-12 w-12 border-t-4 border-green-500 border-solid">
                        </div>
                        <div class="text-gray-800">Onboarding is in process...</div>
                    </div>
                </div>

                <div v-show="!loading" class="p-4 w-full main_content" style="height: 100vh;">
                    <div class="p-4  rounded-lg dark:border-gray-700 mt-14">
                        <div class="p-5 lex items-center justify-center h-auto mb-4  rounded
                        bg-gray-50 dark:bg-gray-800">

                            <div v-if="errorMessage"
                                class="flex items-center p-4 mb-4 text-sm text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800"
                                role="alert">
                                <svg class="flex-shrink-0 inline w-4 h-4 me-3" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path
                                        d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                                </svg>
                                <span class="sr-only">Info</span>
                                <div>
                                    <span class="font-medium">{{ errorMessage }}</span>

                                </div>
                            </div>

                            <div v-if="successMessage"
                                class="flex items-center p-4 mb-4 text-sm text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800"
                                role="alert">
                                <svg class="flex-shrink-0 inline w-4 h-4 me-3" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path
                                        d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                                </svg>
                                <span class="sr-only">Info</span>
                                <div>
                                    <span class="font-medium">{{ successMessage }} </span>

                                </div>
                            </div>

                            <p  class="text-gray-800  dark:text-white">On Board Your Servers  </p> <br>

                            <div class="grid gap-6 mb-6 md:grid-cols-2">
                                <div>
                                    <label for="os" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                        OS Type</label>
                                    <select id="os" v-model="server_type"
                                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option value="Ubuntu">Ubuntu</option>
                                        <option value="Windows">Microsoft Windows</option>
                                        <option value="Redhat">Red Hat Enterprise</option>
                                        <option value="Oracle_Linux">Oracle Linux</option>
                                        <option value="CentOS">CentOS</option>
                                        <option value="Debian">Debian</option>
                                        <option value="HP_UX">HP-UX</option>

                                        <option value="Amazon_Linux">Amazon Linux</option>
                                        <option value="openSUSE">openSUSE</option>
                                        <option value="SUSE">SUSE</option>
                                        <option value="Alpine">Alpine</option>
                                        <option value="Fedora">Fedora</option>
                                        <option value="RaspbianOS">Raspbian OS</option>
                                        <option value="Solaris">Solaris</option>

                                    </select>
                                    <div v-if="errors.server_type" class="text-red-500 text-sm mt-1">
                                        {{ errors.server_type }}
                                    </div>
                                </div>
                            </div>
                            <div class="grid gap-6 mb-6 md:grid-cols-2">
                                <div>
                                    <label for="server_ip"
                                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Server
                                        IP:</label>
                                    <input type="text" id="server_ip" v-model="server_ip" @input="validateServerIpFormat"
                                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="0.0.0.0" required />
                                    <div v-if="errors.server_ip" class="text-red-500 text-sm mt-1">
                                        {{ errors.server_ip }}
                                    </div>
                                </div>
                            </div>

                            <div class="grid gap-6 mb-6 md:grid-cols-2">
                                <div>
                                    <label for="user"
                                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">User:
                                    </label>
                                    <input type="text" id="user" v-model="server_username"
                                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="Username" required>
                                    <div v-if="errors.server_username" class="text-red-500 text-sm mt-1">
                                        {{ errors.server_username }}
                                    </div>
                                </div>
                            </div>

                            <div class="grid gap-6 mb-6 md:grid-cols-2">
                                <div v-if="checkosType">
                                    <label for="server_password"
                                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                        Password</label>
                                    <input type="password" v-model="server_password"
                                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="*********" required>

                                    <div v-if="errors.server_password" class="text-red-500 text-sm mt-1">
                                        {{ errors.server_password }}
                                    </div>
                                </div>

                                <div v-else>
                                    <label for="private_key"
                                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                        Private Key (private key here):
                                    </label>
                                    <textarea id="private_key" v-model="private_key"
                                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 h-24 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="-----BEGIN RSA PRIVATE KEY-----
  ...
  -----END RSA PRIVATE KEY-----" required></textarea>
                                    <div v-if="errors.private_key" class="text-red-500 text-sm mt-1">
                                        {{ errors.private_key }}
                                    </div>
                                </div>
                            </div>


                            <button @click.prevent="onBoard"
                                class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-teal-300 to-lime-300 group-hover:from-teal-300 group-hover:to-lime-300 dark:text-white dark:hover:text-gray-900 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-lime-800">
                                <span
                                    class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                                    OnBoard Server
                                </span>
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
import leftSidebar from '@/components/leftSidebar.vue';
import navBar from '@/components/navBar.vue';
import { useSidebarStore } from '@/stores/sidebar';

export default {
    components: {
        leftSidebar, navBar
    },

    computed: {
        isOpen() {
            return useSidebarStore().open;
        },
        checkosType() {
            if (this.server_type == 'Ubuntu' || this.server_type == 'Windows') {
                return true
            } else {
                return false
            }
        }
    },
    data() {
        return {
            errors: {},
            loading: false,
            successMessage: '',
            errorMessage: '',
            server_ip: '',
            server_username: '',
            server_password: '',
            private_key: '',  // Add private_key to the data

            server_type: '',
        }
    },
    methods: {
    
        onBoard() {
            this.errors = {};
            if (!this.server_ip) {
                this.errors.server_ip = 'Server IP is required.';
                setTimeout(() => {
                    this.errors.server_ip = '';
                }, 5000);
            }

            if (!this.server_username) {
                this.errors.server_username = 'Username is required.';
                setTimeout(() => {
                    this.errors.server_username = '';
                }, 5000);

            }

            // if (!this.server_password) {
            //     this.errors.server_password = 'Password is required.';
            //     setTimeout(() => {
            //         this.errors.server_password = '';
            //     }, 5000);
            // }

            // Check if OS type is selected
            if (!this.osTypeSelected) {
                this.errors.server_type = 'Please select an OS type.';
                setTimeout(() => {
                    this.errors.server_type = '';
                }, 5000);
            }

            const fromData = {
                "ip_address": this.server_ip,
                "ssh_username": this.server_username,
                "ssh_password": this.server_password,
                "private_key": this.private_key,
                "os_type": this.server_type,
            };

            this.loading = true;
            if (this.server_type === 'Windows') {
                console.log("Window");
                axios.post("http://172.16.1.56:8000/api/v3/onboardWindow/", fromData)
                    .then(response => {
                        this.loading = false;
                        this.server_ip = '';
                        this.server_username = '';
                        this.private_key,
                            this.server_type = '';
                        this.successMessage = "Your Server is successfully Onboard";
                        setTimeout(() => {
                            this.successMessage = '';
                        }, 10000);
                        console.log(response.data);
                    })
                    .catch((error) => {
                        this.loading = false;
                        this.errorMessage = 'Error during server onboarding: ' + error.response.data.error;
                        setTimeout(() => {
                            this.errorMessage = '';
                        }, 10000);
                        console.error(error);
                    });
            }
            else {
                console.log("other os");
                axios.post("http://172.16.1.56:8000/api/v3/onboard/", fromData)
                    .then(response => {
                        this.loading = false;
                        this.server_ip = '';
                        this.server_username = '';
                        this.server_password = '';
                        this.server_type = '';
                        this.successMessage = "Your Server is successfully Onboard";
                        setTimeout(() => {
                            this.successMessage = '';
                        }, 10000);
                        console.log(response.data);
                    })
                    .catch((error) => {
                        this.loading = false;
                        this.errorMessage = 'Error during server onboarding: ' + error.response.data.error;
                        setTimeout(() => {
                            this.errorMessage = '';
                        }, 10000);
                        console.error(error);
                    });
            }


        },

        onOsTypeChange() {
            // Set the flag to true when an OS type is selected
            this.osTypeSelected = true;
            // Clear OS type error when an OS type is selected
            this.errors.server_type = '';
        },

        isValidServerIpFormat(ip) {
            // Regular expression for validating an IPv4 address
            const ipv4Regex =
                /^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$/;

            // Check if the provided IP matches the IPv4 format
            return ipv4Regex.test(ip);
        },

        validateServerIpFormat() {
            // Clear server IP error when input changes
            this.errors.server_ip = '';

            // Check and display error if the format is invalid
            if (!this.server_ip) {
                // Display "Server IP is required" error after 5 seconds
                setTimeout(() => {
                    this.errors.server_ip = 'Server IP is required.';
                }, 5000);
            } else if (!this.isValidServerIpFormat(this.server_ip)) {
                this.errors.server_ip = 'Invalid server IPv4 format.';
            }
        },

        clearError(field) {
            // Clear specific field error when input changes
            this.errors[field] = '';
        },
    },
};
</script>
    

<style scoped>
.inner_content {
    width: 70%;
    padding: 10px;
    background-color: #8167c9;
    /* background: linear-gradient(90deg, #8167c9 0%, #eeecee  100%); */
    border-radius: 34% 44% 24% 24% / 5% 21% 25% 4%;
}</style>