<template>
  <li class="
    drop-shadow-md frosted-glass rounded-lg 
    border-white border-solid border-2
  ">
    <div class="px-3 py-2 border-b border-white border-solid">
      <span class="font-bold">{{heading}}:</span>
    </div>
    <ul class="list-disc list-inside py-1">
      <li
        v-for="(item, index) in items"
        :key="index"
        class="px-5 py-1 -my-1 pink-hover pointer-events-none transition-colors"
      >
        <span class="cursor-pointer pointer-events-auto">{{item}}</span>
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
