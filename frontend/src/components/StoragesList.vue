<template>
    <section class="storages">
        <div class="headers">
            <p>айди</p>
            <p>название</p>
            <p>заполнен</p>
            <p>вместимость</p>
            <p>текущая заполненность</p>
        </div>
        <div class="storage" v-for="storage in storages" v-bind:key="storage.id">
            <p>{{ storage.id }}</p>
            <a :href="`storages/${storage.name}`" class="storage__title">{{ storage.name }}</a>
            <p v-if="storage.is_full">да</p>
            <p v-else>нет</p>
            <p>{{ storage.capacity }}</p>
            <p>{{ storage.current_stock }}</p>
            <!-- <div class="storage__infos"> -->
            <!--     <div class="storage__info"> -->
            <!--         <p class="info__title">вместимость</p> -->
            <!--         <p>{{ storage.capacity }}</p> -->
            <!--     </div> -->
            <!--     <div class="storage__info"> -->
            <!--         <p class="info__title">текущая заполненность</p> -->
            <!--         <p>{{ storage.current_stock }}</p> -->
            <!--     </div> -->
            <!--     <div class="storage__info"> -->
            <!--         <p class="info__title">заполнен</p> -->
            <!--         <p>{{ storage.is_full }}</p> -->
            <!--     </div> -->
            <!-- </div> -->
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: "StoragesList",
    data() {
        return {
            storages: [],
            products: [],
            product_images: [],
            storage_products: [],
        }
    },
    mounted() {
        axios.get("api/storages/")
            .then(response => {
                this.storages = response.data;
                console.log(response.data[0].is_full);
            })
            .catch(error => {
                console.error(error);
            })
    },
}
</script>

<style scoped>
a {
    border-bottom: 1px solid #555;
    max-width: fit-content;
}
.headers {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    margin: 2rem 0;
}

.storage {
    display: grid;
    grid-template-columns: repeat(5, 1fr)
}

.storage + .storage {
    margin: 0.5rem 0;
}
</style>
