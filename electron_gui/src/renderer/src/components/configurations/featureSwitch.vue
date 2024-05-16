<script setup>
import {ref} from 'vue'
const selected = ref(null)
const props = defineProps({
    event: Object,
    switchConfig: Object
})
for(var i in props.event){
    if(typeof(props.event[i].next_tick)=='number'){    
        var date = new Date(props.event[i].next_tick * 1000);  // 参数需要毫秒数，所以这里将秒数乘于 1000
        props.event[i].next_tick=(date.getFullYear() + '-'+ (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-'+date.getDate() + ' '+date.getHours() + ':'+date.getMinutes() + ':'+date.getSeconds());
}
}
const headers = [
  { title: '事件', value: "event_name"},
  {title: '下次刷新时间', key: "next_tick" },
]
</script>

<template>
    <v-data-table-virtual
    v-model="selected"
    show-select 
    :headers="headers"
    :items="props.event"
    height="400"
    item-value="event_name"></v-data-table-virtual>
</template>