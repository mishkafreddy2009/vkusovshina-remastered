<template>
    <section class="storages">
        <div class="storage" v-for="storage in storages" v-bind:key="storage.id">
            <a :href="`dasboard/${storage.name}`" class="storage__title">{{ storage.name }}</a>
            <div class="storage__infos">
                <div class="storage__info">
                    <p class="info__title">вместимость</p>
                    <p>{{ storage.capacity }}</p>
                </div>
            </div>
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
            })
            .catch(error => {
                console.error(error);
            })
    },
}
</script>

<style scoped>
.storages {
    display: flex;
    gap: 2rem;
}

.storage {
    min-width: 300px;
    border: 1px solid #19a219;
    border-radius: 1rem;
    padding: 1rem;
}

.storage .storage__title {
    font-size: 1.375rem;
    font-weight: 700;
}


.storage .storage__infos {
    margin: 1rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.storage__infos .storage__info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.storage__info .info__title {
    font-weight: 700;
}
</style>
