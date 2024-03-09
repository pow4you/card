<template>
  <li
    class="
      flex items-stretch
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        p-1 
        grid place-content-center
        
        min-w-16 w-16
        min-h-full

        border-r border-white border-solid '>
      <nuxt-img 
        v-if="img"
        :src=img 
        :alt="platform+' profile picture'"
        class="overflow-hidden text-center
        aspect-square frosted-glass self-center rounded-full border-2 border-white" 
      />
      <Icon
        v-else
        class="overflow-visible h-full w-full p-1.5 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
        size="5rem"
        :name=icon
        />
    </div>
    <NuxtLink :to="link" class="
      flex-grow
      py-2
      
      cursor-pointer
      transition duration-300 ease-in-out 
      pink-hover
      
      flex flex-col gap-1
    ">
      <header class="
        px-3
        text-md font-bold tracking-wide
      ">
        <Icon class="h-2/3 -mt-1" 
            :name=icon
        /> {{ name }}
      </header>
      <p class="
        px-6
        text-xs justify-self-center grow tracking-wide
      ">
        {{ user }}
      </p>
    </NuxtLink>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["link", "img", "user", "name", "platform", "icon"]);
  const { link, img, user, name, platform, icon } = props;
  
</script>



<style></style>
