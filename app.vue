<template>
  <div>
    <AppNavbar />
    
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script lang="ts" setup>
  useHead({
    title: "😽Pow's Card"
  })
</script>