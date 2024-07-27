<template>
    <div class="dashboard">
        <StorageCreate />
        <StoragesList />
    </div>
</template>

<script>
// @ is an alias to /src
import StorageCreate from "@/components/StorageCreate.vue"
import StoragesList from "@/components/StoragesList.vue"

export default {
  name: "DashboardView",
  components: {
      StoragesList,
      StorageCreate,
  }
}
</script>

<style scoped>
.dashboard {
    margin: 1rem;
}
</style>
