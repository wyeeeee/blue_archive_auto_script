<script setup>
    import { ref } from 'vue'
    const includeFiles = ref([])
const props = defineProps({
    switchConfig: Object
})
    </script>
    
    <template>
      <v-sheet class="d-inline-flex align-center">
        <v-switch color="primary" class="d-flex"></v-switch>
        <div>是否使用加速券</div>
      </v-sheet>
    </template>