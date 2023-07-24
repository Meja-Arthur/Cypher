<template>
  <div id="wrapper">

    <nav class="navbar is-dark">

      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Djackets</strong></router-link>

               <!--Hamberger  this will happen when the screen is reduced to size
              data-target is the targeted codes that this effects should take place to them  -->
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span arial-hidden="true"></span>
          <span arial-hidden="true"></span>
          <span arial-hidden="true"></span>
        </a>

      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">

         <div class="navbar-start">
            <div class="navbar-item">
              <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" class="input" placeholder="what are you looking for?"
                     name="query">
                  </div>
                  <div class="control">
                    <button class="button is-success">
                      <span class="icon">
                        <i class="fas fa-search"></i>
                      </span>
                    </button>
                  </div>
                </div>
              </form>
            </div>
         </div>


        <div class="navbar-end">

          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
          

          <div class="navbar-item">

            <div class="buttons"><!--to get space between the buttons we add the class="buttons"-->
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>
               
              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
             

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>

            </div>

          </div>

        </div>
      </div>

    </nav>  

    <div class="is-loading-bar has-text-centered" 
    v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div><!--where we put the loading bar functionality -->
    </div>

    <section class="section">
    <!--this is the place where all the other router come in from the app
    so whatever is here in the app.vue appeares in other pages -->
      <router-view/>
    </section>

    <footer class="footer"><!--the following footer will display in every page -->
      <p class="has-text-centered">Copyright (c) 2023</p>
      <p class="has-text-centered">Arthurkings</p>
    </footer>

  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,

      cart: {
        items: []
      }

    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    /**this is where we put the store into action */
    /**commit is used to call the mutation's in the store indexs.js */
    
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
    

  }, 

  
  mounted() {
    this.cart = this.$store.state.cart
  },


  computed: {

    cartTotalLength() {

      let totalLength = 0
      for ( let i = 0; i < this.cart.items.length; i++){ 
        /**I don't understand the following line of code man  */
        totalLength += this.cart.items[i].quantity
      }
      return totalLength

    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
