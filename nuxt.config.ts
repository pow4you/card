// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-icon',
    '@nuxt/image',
    "nuxt-lodash",
    "@nuxtjs/device",
    "nuxt-umami"
  ],
  
  devtools: { enabled: true }
})