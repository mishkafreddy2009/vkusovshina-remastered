<template>
    <section class="products">
        <div v-for="product in products" v-bind:key="product.id">
            <div class="card">
                <div class="card__description">
                    <a href="#" class="card__title">{{ product.name }}</a>
                    <div class="card__metadata">
                        500 г
                    </div>
                </div>
                <a href="#" class="card__button">
                    99 Р
                </a>
            </div>
        </div>

    </section>
</template>

<script>
import axios from "axios";

export default {
    name: "ProductsList",
    data() {
        return {
            products: [],
            product_image: "",
        }
    },
    mounted() {
        axios.get("api/products/")
            .then(response => {
                this.products = response.data;
            })
            .catch(error => {
                console.error(error);
            })
        axios.get("api/products/3/images")
            .then(response => {
                this.product_image = "http://127.0.0.1:8001/static/" + encodeURIComponent(response.data[0].url);
            })
            .catch(error => {
                console.error(error);
            })
    }

}
</script>

<style scoped>
.products {
    margin: 2rem 0;
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 0.75rem;
}
</style>
