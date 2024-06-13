<script setup>
    import { ref, watch } from 'vue'
import { useConfigStore } from '@renderer/stores/config'
const configStore = useConfigStore();
configStore.getAllConfigs().then();
    </script>
    
    <template>
        <v-text-field label="悬赏委托扫荡" density='compact' variant="underlined"  max-width="600" class="pt-2"></v-text-field>
        <v-text-field label="学院交流会扫荡" density='compact' variant="underlined" max-width="600" class="pt-2"></v-text-field>
        <v-text-field label="活动关卡扫荡关卡" density='compact' variant="underlined" max-width="600" class="pt-2"></v-text-field>
        <v-text-field label="活动关卡扫荡次数" density='compact' variant="underlined" max-width="600" class="pt-2"></v-text-field>
        <v-text-field label="特殊委托扫荡" density='compact' variant="underlined" max-width="600" class="pt-2"></v-text-field>
        <v-select class="pt-2 pa-1" multiple variant="solo" :items="challenging" max-width="600" label="悬赏委托扫荡券购买次数"></v-select>
        <v-select class="pt-2 pa-1" multiple variant="solo" :items="challenging" max-width="600" label="日程券购买次数  "></v-select>
        <v-select class="pt-2 pa-1" multiple variant="solo" :items="challenging" max-width="600" label="学院交流会扫荡券购买次数"></v-select>
    </template>