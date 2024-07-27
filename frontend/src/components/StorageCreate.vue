<template>
    <section class="storage-create">
        <button class="button add-button" @click="showForm = true">добавить склад</button>
            <form class="form" v-if="showForm" @submit.prevent="createStorage">
                <div class="form__item">
                    <label for="name">название</label>
                    <input type="text" name="name" v-model="name">
                </div>
                <div class="form__item">
                    <label for="description">описание</label>
                    <input type="text" name="description" v-model="description">
                </div>
                <div class="form__item">
                    <label for="address">адрес</label>
                    <input type="text" name="address" v-model="address">
                </div>
                <div class="form__item">
                    <label for="phone-number">номер телефона</label>
                    <input type="text" name="phone-number" v-model="phone_number">
                </div>
                <div class="form__item">
                    <label for="capacity">вместимость</label>
                    <input type="text" name="capacity" v-model="capacity">
                </div>
                <div class="form__item">
                    <label for="current-stock">текущая заполненность</label>
                    <input type="text" name="current-stock" v-model="current_stoc">
                </div>
                <div class="buttons">
                    <button class="button" type="submit">добавить</button>
                    <button class="button negative-empty-button" type="button" @click="showForm = false">отменить</button>
                </div>
            </form>
    </section>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            showForm: false,
            name: "",
            description: "",
            address: "",
            phone_number: "",
            capacity: 0,
            current_stock: 0,
        };
    },
    methods: {
        async createStorage() {
            try {
                const response = await axios.post("/api/storages/", {
                    name: this.name,
                    description: this.description,
                    address: this.address,
                    phone_number: this.phone_number,
                    capacity: this.capacity,
                    current_stock: this.current_stock,
                })
                console.log("storage created:", response.data)
                this.showForm = false
                this.name = ""
            } catch (error) {
                console.error("error:", error.response.data)
            }
        }
    }
}
</script>

<style scoped>
</style>
