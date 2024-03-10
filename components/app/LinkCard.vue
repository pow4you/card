<template>
  <div
    class="
      flex items-stretch
      w-full h-fit 
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        grid place-content-start
        h-full
        min-w-24 w-24
        p-2
        
        
        border-r border-white border-solid '>
      <Icon
        class="overflow-visible h-full w-full p-4 max-h-24 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
        size="5rem"
        :name=CardIcon
        />
      
    </div>
    <div class="flex-grow flex flex-col items-stretch">
      <NuxtLink :to="CardLink" class="
        px-4 py-1 
        
        cursor-pointer
        transition duration-300 ease-in-out 
        pink-hover
        border-solid border-b border-white
      ">
        <header class="text-lg font-bold tracking-wide">
          {{ CardTitle }}
        </header>
      </NuxtLink>
      
      <p class="flex-grow text-xs tracking-normal p-4">
        <slot />
      </p>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps(["CardLink", "CardTitle", "CardIcon"]);
  const { CardLink, CardTitle, CardIcon } = props;
</script>



<style></style>
