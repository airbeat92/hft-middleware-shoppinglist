<template>
  <v-container>
    <add-item-form class="mb-5" @item-added="addItem" />
    <shopping-list :items="items" @remove-item="removeItem" @update-item="updateItem" />
  </v-container>
</template>





<script setup lang="ts">
import { ref } from 'vue';
import ShoppingList from '@/components/Shoppinglist.vue';
import AddItemForm from '@/components/AddItemForm.vue';
import { Api, ItemCreate, ItemRead, ItemUpdate } from "@/api/api";

const api = new Api({ baseUrl: import.meta.env.VITE_API_URL});
const items = ref<ItemRead[]>([]);

const loadItems = async () => {
  const response = await api.items.readItemsItemsGet();
  items.value = response.data;
};

const addItem = async (item: ItemCreate) => {
  await api.items.createItemRouteItemsPost(item);
  await loadItems()
};

const removeItem = async (id: number) => {
  const item = items.value.find(item => item.id = id);
  if(item){
    await api.items.deleteItemRouteItemsItemIdDelete(item.id);
    await loadItems()
  }
};

const updateItem = async (item: ItemUpdate) => {
  if (item.id) {
    await api.items.updateItemRouteItemsItemIdPut(item.id, item)
    await loadItems()
  }
}


loadItems();
</script>
