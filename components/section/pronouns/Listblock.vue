<template>
  <li class="
    drop-shadow-md frosted-glass rounded-lg 
    border-white border-solid border-2
  ">
    <div class="px-3 max-sm:px-2.5 py-2 max-sm:py-1.5 border-b border-white border-solid bg-periwinkle">
      <span class="font-bold">{{heading}}:</span>
    </div>
    <ul class="list-disc list-inside py-1.5">
      <li
        v-for="(item, index) in items"
        :key="index"
        class="px-5  py-1 -my-1 pink-hover pointer-events-none transition-colors"
      >
        <span class="cursor-pointer pointer-events-auto max-sm:-mx-1">{{item}}</span>
      </li>
    </ul>
  </li>
</template>

<script lang="ts" setup>
  const props = defineProps(["items", "heading"]);
  const { items, heading } = props;

</script>



<style>

</style>
