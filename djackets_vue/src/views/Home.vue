<template>

  <div class="home">

     <section class="hero is-small is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Djacket
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
     </section>

     <div class="columns is-multiline">
      <div class="column is-12">
         <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <!--
        The real deal is here now with us 
        
        <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
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
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"  
      />


     </div>

  </div>

</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },

  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = ' Homepage| Djackets'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios 
        .get('/api/v1/latest-products/')
        .then(response => {
           this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
        this.$store.commit('setIsLoading', false)  
    }
  }
}
</script>

