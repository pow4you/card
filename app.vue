<template>
  <div>
    <AppNavbar />
    
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script lang="ts" setup>
  const emj_list = ["😽","😽","😽","😽", "🥰", "😸", "😻", "🙉"];
  const prepared_title = "Pow's Card " + useSample(emj_list);
  useHead({
    title: prepared_title
  })
</script>