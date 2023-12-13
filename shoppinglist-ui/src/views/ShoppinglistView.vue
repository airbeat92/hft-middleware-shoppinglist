<template>
  <v-container>
    <add-item-form @item-added="addItem" />
    <shopping-list :items="items" @remove-item="removeItem" />
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ShoppingList from '@/components/Shoppinglist.vue';
import AddItemForm from '@/components/AddItemForm.vue';

const items = ref<string[]>([]);

const addItem = (item: string) => {
  items.value.push(item);
};

const removeItem = (index: number) => {
  items.value.splice(index, 1);
};
</script>
