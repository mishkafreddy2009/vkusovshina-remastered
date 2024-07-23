// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2024-04-03',
    devtools: { enabled: true },
    routeRules : {
        '/docs': {
            proxy: "http://localhost:8001/docs",
        },
    }
})
