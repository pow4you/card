<template>
  <SectionCard CardIcon="ph:info" CardTitle="Announcement">
      <div class="p-4 gap-2 grid grid-cols-6 auto-rows-max">
        <SectionSocialCard 
          class="max-md:col-span-6 col-span-3"
          :social="socials[0]"
        ></SectionSocialCard>
        <SectionSocialCard 
          class="max-md:col-span-6 col-span-3"
          :social="socials[1]"
        ></SectionSocialCard>
      </div>
      
    </SectionCard>
    
</template>

<script lang="ts" setup>
  const appConfig = useAppConfig();
  const socials = appConfig.socials;
</script>



<style>

</style>
