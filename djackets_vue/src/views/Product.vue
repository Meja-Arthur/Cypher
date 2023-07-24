
<template>
    <div class="page-product">
        <div class="columns is-multiline">

            <div class="column is-9"><!--this allows the display screen to be on the left of screen -->
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>
                <p>{{ product.description }}</p>
            </div>

            <div class="column is-3"><!--column is-3 display's the information on the right side of the screen -->

                <h2 class="subtitle">Information</h2>
                <p><strong>Price: </strong>Ksh{{ product.price }}</p>

                <div class="field has-addons mt-6">
                    <!--has-addons which means the button and the input will be with each other -->
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
  
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast' /*Is the import for notification  */

export default {
    name: 'Product',
    data() {
        return{
            product: {},
            quantity:1

        }
    },
    mounted() { 
         /**to get the product form the server we use the axios hence the mounted lifecycle */
        this.getProduct()
    },
    methods: {

        async getProduct() {

            this.$store.commit('setIsLoading', true)
            /** This is where we try to make the loading bar function  */
           /** getting the category_slug and product_slug from the absolute_url we are on */
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
            
               .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + '| Djackets'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },

        addToCart() {
         
            /**This line of code checkes if this.quantity is a number or if this.quantity is less than 0
             * so if either of that is true it will assign this.quantity to 1 integer
              */
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                product: this.product,
                quantity: this.quantity     
            }
            this.$store.commit('addToCart', item)

            toast({  /*This is how we make a notification
                npm install bulma-toast  */
                message: 'Product added successfully',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'top-center',
            })
        }
    }

}
</script>

<style>

</style>
