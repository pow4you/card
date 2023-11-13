<template>
  <li
    class="
      flex items-stretch
      w-full h-full 
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        grid justify-center content-center
        max-h-40
        min-w-fit
        aspect-square
        flex-shrink
        p-2
        
        
        border-r border-white border-solid '>
      <nuxt-img 
        v-if="img"
        :src=img 
        :alt="platform+' profile picture'"
        class=" overflow-hidden text-center align-middle max-h-24 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
      />
      <Icon
        v-else
        class="overflow-visible h-full w-full p-4 max-h-24 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
        size="5rem"
        :name=icon
        />
      
    </div>
    <div class="flex-grow flex flex-col items-stretch">
      <NuxtLink :to="link" class="
        px-4 py-1 
        
        cursor-pointer
        transition duration-300 ease-in-out 
        pink-hover
        border-solid border-b border-white
      ">
        <header class="text-lg font-bold tracking-wide">
          <Icon class="aspect-square vertical-align-middle" 
              :name=icon
          /> {{ name }}
        </header>
        <p class="text-sm tracking-wide">
          {{ user ? user : link }}
        </p>
      </NuxtLink>
      
      <p class="flex-grow text-xs tracking-normal p-4">
        {{ description }}
      </p>
    </div>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["link", "img", "user", "name", "platform", "icon", "description"]);
  const { link, img, user, name, platform, icon, description } = props;
</script>



<style></style>
