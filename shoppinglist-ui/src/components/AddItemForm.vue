<template>
  <v-form @submit.prevent="submit">
    <v-text-field
        v-model="newItem"
        label="Add a new item"
        outlined
        dense
    ></v-text-field>
    <v-btn type="submit" color="primary">Add</v-btn>
  </v-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const newItem = ref('');
const emit = defineEmits(['item-added']);

const submit = () => {
  if (newItem.value.trim()) {
    emit('item-added', newItem.value);
    newItem.value = '';
  }
};
</script>
