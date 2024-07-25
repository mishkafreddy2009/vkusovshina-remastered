<template>
    <div class="card">
        <!-- {{ products }} -->
        <!-- <img class="card__image" :src="`${ product_image }`" alt=""> -->
            <!-- <img src="" alt=""> -->
        <!-- <div class="card__description"> -->
        <!--     <a href="#" class="card__title">Нектарины Вкусовщина</a> -->
        <!--     <div class="card__metadata"> -->
        <!--         500 г -->
        <!--     </div> -->
        <!-- </div> -->
        <!-- <a href="#" class="card__button"> -->
        <!--     99 Р -->
        <!-- </a> -->
    </div>
</template>

<script>
import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
    name: "BaseProduct",
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
})
</script>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    max-width: 200px;
}

.card__image {
    border-radius: 1rem;
}

.card__description {
    margin: 0.25rem 0 0.5rem 0;
}

.card__description .card__title {
    font-weight: 700;
}

.card__description .card__metadata {
    font-weight: 600;
    color: #9f9f9f;
}

.card__button {
    font-weight: 700;
    text-decoration: none;
    padding: 0.1rem 0.75rem;
    border-radius: 1rem;
    background-color: #f4f4f4;
    max-width: fit-content;
    color: #19A219;
    transition: background-color 0.5s;
}

.card__button::after {
    margin-left: 0.1rem;
    font-weight: 400;
    content: "+";
    font-size: 2rem;
}

.card__button:hover {
    background-color: #e4e4e4;
}
</style>
