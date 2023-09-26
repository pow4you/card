<template>
  <li
    class="
      grid grid-rows-[0.5fr_auto] grid-cols-[auto_1fr] auto-cols-min
      w-full h-full 
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        p-2 row-span-2 row-start-1 col-span-1 col-start-1 
        grid justify-center content-center
        
        aspect-square
        h-full w-full
        border-r border-white border-solid '>
      <nuxt-img 
        v-if="img"
        :src=img 
        :alt="platform+' profile picture'"
        class=" overflow-hidden text-center align-middle max-h-24 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
      />
      <Icon
        v-else
        class="h-full w-full p-4 max-h-24 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
        size="5rem"
        :name=icon
        />
      
    </div>
    <NuxtLink :to="link" class="
      row-span-1 row-start-1 col-span-1 col-start-2
      px-4 py-1 
      
      cursor-pointer
      transition duration-300 ease-in-out 
      pink-hover
      border-solid border-b border-white
    ">
      <span class="text-lg font-bold">
        <Icon class="aspect-square vertical-align-middle" 
            :name=icon
        /> {{ name }}
      </span> <br />
      <span class="text-sm">
        @{{ user }}
      </span>
    </NuxtLink>
    <div class="row-span-1 row-start-2 col-span-1 col-start-2 text-xs p-4">
      {{ description }}
    </div>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["link", "img", "user", "name", "platform", "icon", "description"]);
  const { link, img, user, name, platform, icon, description } = props;
</script>



<style></style>
