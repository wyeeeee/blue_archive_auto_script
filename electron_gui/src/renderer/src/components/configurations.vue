<script setup>
import axios from 'axios';
import {ref} from 'vue';
const switchConfig = ref(null);
axios.post('http://127.0.0.1:8000/get-config/default_config/switch')
      .then(response => (switchConfig.value = response))
      .catch(function (error) {
        console.log(error);
      });
console.log(switchConfig.value)
</script>

<template>
    <v-expansion-panels v-if="switchConfig!=null">
        <v-expansion-panel>
        
        <v-expansion-panel-title>thik<br>sd</v-expansion-panel-title>
        <v-expansion-panel-text>sadwsadasdads</v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
</template>