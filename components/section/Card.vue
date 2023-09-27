<template>
  <div class="
      max-md:w-11/12 md:w-5/6 lg:w-2/3 h-fit
      flex flex-col
      rounded-lg frosted-glass shadow-xl
      border-purple-100 border
  ">
    <div class="
      flex flex-row gap-4
      pl-4 pr-10
      bg-periwinkle

      border-b border-solid border-purple-100
    ">
      <div class="
        aspect-square 
        pt-1 pb-2 pr-4 
        border-r border-solid border-purple-100
      ">
        <Icon :name="props.CardIcon ? props.CardIcon:''"></Icon>
      </div>
      <div 
        name="title" 
        class="
          pt-1.5 flex-grow"
      >
        {{props.CardTitle}}
      </div>
      <button 
        @click=toggleMinimized
      
        name="minimize"
        class="
        transition-all
        thulian-button
        
        rounded-b-md
        
        px-4 pb-1 mb-1.5
        border border-t-0  border-solid border-purple-100
        "
      >
        <Icon class="text-white" :name="!minimized?'ph:caret-up-bold':'ph:caret-down-bold'"></Icon>
      </button>
    
    </div>
    <div 
      class="
        py-1.5 
        overflow-y-hidden
        
        transition-all ease-in-out duration-500
      " 
      ref="content"
    >
      <slot />
    </div>
  </div>
</template>

<script setup>
  const props = defineProps(["CardIcon", "CardTitle"]);
  const minimized = ref(false);
  const content = ref(null);
  
  onMounted(() => {
    nextTick(() => {
      unsetMaxHeight();
    });
  });
  
  nextTick()

  const toggleMinimized = ()=>{
    minimized.value =!minimized.value;
    
    if (!content.value) { return; }
    
    
    if (!minimized.value) {
      // animate to max height
      content.value.style.maxHeight = "0px";
      
      setTimeout(() => {
        resetMaxCalculatedHeight()
      }, 1);
      
      setTimeout(unsetMaxHeight, 500);

    }else {
      // animate to 0 height
      resetMaxCalculatedHeight();
      
      setTimeout(() => {
        content.value.style.maxHeight = "0px";
      }, 1);
      
      
    }
  };
  
  const resetMaxCalculatedHeight = () => {
    let maxHeight = Math.min(
      content.value.scrollHeight,
      window.innerHeight + 50
    );
  
    content.value.style.maxHeight = maxHeight + "px";
  }
  
  const unsetMaxHeight = () => {
    content.value.style.maxHeight = "";
    
  }
  
</script>



<style>


</style>
