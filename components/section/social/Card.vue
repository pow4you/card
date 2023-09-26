<template>
  <li
    class="
      grid grid-rows-[min-content_2fr] grid-cols-5
      w-full h-full 
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        p-2 row-span-2 row-start-1 col-span-2 col-start-1 
        grid justify-center content-center
        
        h-full
        border-r border-white border-solid '>
      <img :src=social.profilePic :alt="social.shortName+' profile picture'"
        class="max-h-28 aspect-square frosted-glass self-center rounded-full border-2 border-white" />
    </div>
    <NuxtLink :to="social.url" class="
      row-span-1 row-start-1 col-span-3 col-start-3
      px-4 py-1 
      
      cursor-pointer
      transition duration-300 ease-in-out 
      bg-transparent bg-opacity-0 hover:bg-pink-700 hover:bg-opacity-10 
      border-solid border-b border-white
    ">
      <span class="text-lg font-bold">
        <Icon class="aspect-square vertical-align-middle" 
            :name=social.icon
        /> {{ social.longName }}
      </span> <br />
      <span class="text-sm">
        @{{ social.userName }}
      </span>
    </NuxtLink>
    <div class="row-span-1 row-start-2 col-span-3 col-start-3 text-xs p-4">
      {{ social.description }}
    </div>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["social"]);
  const social = props.social;
</script>



<style></style>
