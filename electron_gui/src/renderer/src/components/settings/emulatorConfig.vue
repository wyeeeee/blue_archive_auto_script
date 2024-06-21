<script setup>
    import { ref, watch } from 'vue'
    import { useConfigStore } from '@renderer/stores/config'
    const configStore = useConfigStore();
    configStore.getAllConfigs().then();
        </script>
    
    
        
        <template>
        </template>