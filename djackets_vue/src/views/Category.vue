<template>
    <div class="page-category">

        <div class="columns is-multiline">

            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>

        <!--
        The real deal is here now with us which is probably the code that is re-used 
        <div class="column is-3" v-for="product in category.products" v-bind:key="product.id">
          <div class="box">

            <figure class="image mb-4">
              <img v-bind:src="product.get_thumbnail">
            </figure>
            
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">Ksh{{ product.price  }}</p>
            
             <router-link v-bind:to="product.get_absolute_url" 
                class="button is-dark mt-4">view details</router-link>

          </div>
        </div>

      -->

            <ProductBox

                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product"  
             />

        </div> 
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox'



export default {
    name: 'Category',

    components: {
        ProductBox
    },
    data() {
        return{
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
         /**this allow the switching of the two category automatically when called upon
          * so we need to watch for changes in the route whenever a change occour's in the url's
          */
       $route(to, from) {
           if (to.name === 'Category') {
               this.getCategory()
           }
       }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + '| Djackets'
                })
                .catch(error => {
                    console.log(error)

                    toast({  /*This is how we make a notification  */

                            message: 'Something went wrong please try again',
                            type: 'is-danger',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'top-center',

                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    } 

}
</script>

<style>

</style>