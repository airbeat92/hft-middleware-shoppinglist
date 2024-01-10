<!--<template>-->
<!--  <v-data-table-->
<!--    :headers="headers"-->
<!--    :items="items"-->
<!--    class="elevation-1"-->
<!--  >-->
<!--    <template v-slot:item.action="{ item }">-->
<!--      <v-btn icon @click="editItem()">-->
<!--        <v-icon>mdi-pencil</v-icon>-->
<!--      </v-btn>-->
<!--      <v-btn icon color="red" @click="removeItem(item.id)">-->
<!--        <v-icon>mdi-delete</v-icon>-->
<!--      </v-btn>-->
<!--    </template>-->
<!--  </v-data-table>-->
<!--</template>-->

<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :sort-by="[{ key: 'calories', order: 'asc' }]"
  >
    <template v-slot:top>
        <v-dialog
          v-model="editDialog"
          max-width="500px"
        >
          <v-card>
            <v-card-title>
              <span class="text-h5">Edit Item</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.quantity"
                      label="Quantity"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >

                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="() => {editDialog = false}"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="editItem"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        size="small"
        class="me-2"
        @click="openEditItemDialog(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        size="small"
        @click="removeItem(item.id)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>



<script setup lang="ts">
import type { ItemRead, ItemUpdate } from "@/api/api";
import { ref } from "vue";

let editDialog = ref(false)
let editedItem = {name: "", quantity: 0 } as ItemUpdate

const props = defineProps({
  items: {
    type: Array as () => ItemRead[],
    required: true
  }
});
const headers = [
  { text: 'Name', value: 'name' },
  { text: 'Menge', value: 'quantity' },
  { text: 'Aktionen', value: 'actions', sortable: false }
];

const emit = defineEmits(['remove-item', 'update-item']);

const removeItem = (id: number) => {
  emit('remove-item', id);
};

const editItem = () => {
  console.log(editedItem)
  emit ('update-item', editedItem)
  editDialog.value = false
}

const openEditItemDialog = (item: ItemRead) => {
  editDialog.value = true
  editedItem = JSON.parse(JSON.stringify(item));
};
</script>
