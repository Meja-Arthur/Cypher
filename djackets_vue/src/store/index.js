import { createStore } from 'vuex'

export default createStore({

  state: { // ils the variable information

    cart: {
      items: [],
    },

    isAuthenticated: false,
    token: '',
    isLoading: false

  },


  getters: {
  },
  mutations: { // sycronise mutation to the state 

    initializeStore(state) {

      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))/**getting the object cart if it exist in the local storage */
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
      
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }

    },


    addToCart(state, item) {
      /*Here we check the item we are trying to add in the cart if it exist in the cart  */
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)/*this line checks if the product exist in the cart */
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }else{
        state.cart.items.push(item)
      }      

      localStorage.setItem('cart', JSON.stringify(state.cart)) /**here we update the localstorage in cart */
     
    },

    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, status) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    }
  },


  actions: {
  },
  modules: {
  }
})
