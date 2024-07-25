<template>
    <div class="dashboard">
        <!-- <StorageCreateView /> -->
        <StoragesList />
    </div>
</template>

<script>
// @ is an alias to /src
import StoragesList from '@/components/StoragesList.vue'

export default {
  name: 'DashboardView',
  components: {
      StoragesList,
  }
}
</script>

<style scoped>
.dashboard {
    margin: 1rem;
}
</style>
