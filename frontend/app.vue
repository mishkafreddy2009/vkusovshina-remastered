<script setup lang="ts">
const { data: storages } = useFetch("/api/v1/storages")
</script>

<template>
  <div>
    <NuxtRouteAnnouncer />
    <!-- <NuxtWelcome /> -->
    <NuxtPage />
    <p>storages: {{ storages }}</p>
  </div>
</template>
