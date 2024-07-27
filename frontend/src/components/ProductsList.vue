<template>
    <section class="products">
        <div class="product-cart" v-for="product in products" v-bind:key="product.id">
            <img class="product-cart__image" :src="product.image_url" alt="">
            <div class="product-cart__description">
                <a :href="`/products/${product.id}`" class="product-cart__title">{{ product.name }}</a>
                <p class="product-cart__weight">{{ product.weight }} г</p>
            </div>
            <a href="#" class="product-cart__button">
                {{ product.price }} Р
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                    <path fill-rule="evenodd" d="M12 3.75a.75.75 0 0 1 .75.75v6.75h6.75a.75.75 0 0 1 0 1.5h-6.75v6.75a.75.75 0 0 1-1.5 0v-6.75H4.5a.75.75 0 0 1 0-1.5h6.75V4.5a.75.75 0 0 1 .75-.75Z" clip-rule="evenodd" />
                </svg>
            </a>
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
        }
    },
    methods: {
        getProducts() {
            axios.get("api/products/")
                .then(response => {
                    this.products = response.data.map(product => ({
                        ...product,
                        image_url: null,
                    }));
                    this.getProductImages();
                })
                .catch(error => {
                    console.error(error);
                });
        },
        getProductImages() {
            this.products.forEach(product => {
                this.getProductImage(product.id)
                    .then(imageUrl => {
                        product.image_url = imageUrl;
                    })
                    .catch(error => {
                        console.error(error);
                    });
            });
        },
        getProductImage(productId) {
            return axios.get(`api/products/${productId}/images`)
                .then(response => {
                    return `http://127.0.0.1:8001/static/${response.data.url}`;
                })
                .catch(error => {
                    console.error(error);
                    return null;
                });
        }
    },
    created() {
        this.getProducts();
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

.product-cart {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.product-cart .product-cart__image {
    border-radius: 1rem;
}

.product-cart .product-cart__title {
    font-weight: 700;
}

.product-cart .product-cart__button {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 700;
    max-width: 7rem;
    padding: 0.5rem 1rem;
    background-color: #f1f1f1;
    border-radius: 1rem;
}

.product-cart .product-cart__button svg {
    max-width: 2rem;
}
</style>
