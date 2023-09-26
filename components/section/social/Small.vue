<template>
  <li
    class="
      flex items-stretch
      
      drop-shadow-md frosted-glass rounded-lg 
      border-white border-solid border-2
    ">
    <div
      class='
        p-0.5 
        grid justify-center content-center
        
        
        border-r border-white border-solid '>
      <nuxt-img 
        v-if="img"
        :src=img 
        :alt="platform+' profile picture'"
        class="overflow-hidden text-center align-middle max-h-16
        aspect-square frosted-glass self-center rounded-full border-2 border-white" 
      />
      <Icon
        v-else
        class="overflow-visible h-full w-full p-1.5 max-h-16 aspect-square frosted-glass self-center rounded-full border-2 border-white" 
        size="5rem"
        :name=icon
        />
    </div>
    <NuxtLink :to="link" class="
      flex-grow
      px-4 py-1 
      
      cursor-pointer
      transition duration-300 ease-in-out 
      pink-hover
    ">
      <span class="text-md font-bold">
        <Icon class="aspect-square vertical-align-middle" 
            :name=icon
        /> {{ name }}
      </span> <br />
      <span class="text-xs">
        @{{ user }}
      </span>
    </NuxtLink>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["link", "img", "user", "name", "platform", "icon"]);
  const { link, img, user, name, platform, icon } = props;
  
</script>



<style></style>
