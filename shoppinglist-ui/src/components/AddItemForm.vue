<template>
  <v-form class="d-flex flex-row" @submit.prevent="submit">
    <v-text-field
      class="flex-grow-1"
        v-model="newItem"
        label="Add a new item"
        outlined
        dense
    ></v-text-field>
    <v-text-field
      class="mx-5 flex-grow-0"
      label="Quantity"
      type="number"
      v-model="quantity"
    ></v-text-field>
    <v-btn type="submit" color="primary" :disabled="newItem.length < 1  || quantity < 1">Add</v-btn>
  </v-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';




const newItem = ref('');
const quantity = ref(0)
const emit = defineEmits(['item-added']);

const submit = () => {
  if (newItem.value.trim() && quantity.value > 0) {
    emit('item-added', {name: newItem.value, quantity: quantity.value});
    newItem.value = '';
    quantity.value = 0;
  }
};
</script>
