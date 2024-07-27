<template>
    <div class="storage">
        <StorageBase />
    </div>
</template>

<script>
import StorageBase from "@/components/StorageBase.vue"

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
