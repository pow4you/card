<template>
  <script defer src="https://analytics.eu.umami.is/script.js" data-website-id="ac7ddfba-a589-404b-90d8-5fbd0974be03"></script>
  <div>
    <AppNavbar />
    
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script lang="ts" setup>
  const emj_list = ["😽","😽","😽","😽", "🥰", "😸", "😻", "🙉", "🐴", "🐻", "🪻", "🦜", "🦈"];
  const prepared_title = "Pow's Card " + useSample(emj_list);
  useHead({
    title: prepared_title
  })
</script>