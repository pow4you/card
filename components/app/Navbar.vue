<template>
  <div 
    class="
      fixed top-0 left-0 z-10
      w-full
      p-2
      
      max-sm:text-xs text-sm
      
      frosted-glass backdrop-blur-lg shadow-lg
      
      flex gap-4 place-content-center
      max-sm:gap-2
    "
  >
    
    <NuxtLink
      v-for="link of navigation"
      :key="link.path"
      :to="link.path"
      :active-class="$route.fullPath == link.path ? 'font-bold' : '' "
      class="
        row-start-1 row-span-1
        col-start-auto col-span-1
        
        flex gap-1 vertical-align-middle
        
        px-3 max-sm:px-2 py-1 frosted-glass rounded shadow-sm
        
        border-purple-100 border
        
        transition-all duration-300 ease-in-out
        hover:bg-opacity-50 hover:shadow-lg hover:border-purple-300 hover:border-opacity-70
      "
    >
      
      <Icon class="aspect-square vertical-align-middle h-full"  
        :name="$route.fullPath == link.path ? link.active_icon : link.icon"
      /> {{ link.title }}
    </NuxtLink>
  </div>
</template>

<script setup>
  
  const appConfig = useAppConfig();
  const navigation = appConfig.navigation;
  
</script>



<style>

</style>
