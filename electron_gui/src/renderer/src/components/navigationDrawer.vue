<template>
    <v-navigation-drawer
        expand-on-hover
        rail
        width="200"
        :mobile="false"
        :permanent="true"
      >

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-home" title="home" value="home" color="blue" :active="drawer === 0" @click="emitDrawer(0)"></v-list-item>
          <v-list-item prepend-icon="mdi-file-cog" title="configurations" value="configurations" color="blue" :active="drawer === 1"  @click="emitDrawer(1)"></v-list-item>
          <v-list-item prepend-icon="mdi-cog" title="settings" value="settings" color="blue" :active="drawer === 2"  @click="emitDrawer(2)"></v-list-item>
        </v-list>
        <template v-slot:append>
            <v-list density="compact" nav>
                <v-list-item prepend-icon="mdi-help-box-multiple-outline" title="help" value="help" color="blue" :active="drawer === 3"  @click="emitDrawer(3)"></v-list-item>
                <v-list-item prepend-icon="mdi-information-outline" title="about" value="about" color="blue" :active="drawer === 4"  @click="emitDrawer(4)"></v-list-item>
              </v-list>
          </template>
      </v-navigation-drawer>
</template>

<script setup>
  import { ref} from 'vue'
  const emit = defineEmits(['changeDrawer'])
  const drawers={
        0: 'home',
        1: 'configurations',
        2: 'settings',
        3: 'help',
        4: 'about'
  }
  const drawer = ref(0)

  function emitDrawer(id) {
      drawer.value = id
      emit('changeDrawer',drawers[id])
  }
</script>