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
  const prepared_title = useSample(emj_list)+ " Pow's Card";
  useHead({
    title: prepared_title
  })
</script>