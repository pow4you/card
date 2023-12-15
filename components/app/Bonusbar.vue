<template>
  <div class="
    p-2
    flex align-middle justify-evenly flex-wrap
    gap-2
    top-11 z-50
    sticky
    max-md:w-full
    max-md:px-8
  ">
    <NuxtLink
      v-for="link of links"
      :key="link.name"
      :to="link.url"
      
      class="
        flex 
        
        border-purple-100 border

        
        py-1.5 px-2.5 text-center
        
        frosted-glass rounded  shadow backdrop-blur-lg
        
        transition-all duration-300 ease-in-out
        hover:bg-opacity-50 hover:shadow-lg hover:border-purple-300 hover:border-opacity-70
      "
      
    >
      <Icon class="mx-1" :name="link.icon" />
      <div 
        class="
          mx-1 grow text-sm
        "
      >{{ link.name }}</div>
    </NuxtLink>
    
  </div>
</template>

<script setup>
  const props = defineProps(["links"]);
  const { links } = props;</script>



<style>

</style>
