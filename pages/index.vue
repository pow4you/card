<template>

	<SectionCard CardIcon="ph:house-bold" CardTitle="Home" id="Home">
    <div class="p-4">
      <section>
        <h1 class="text-center pb-4">
          <Icon class="mx-.5" name="ph:sparkle"></Icon>
          Hi_ I'm Pow
          <Icon class="mx-.5" name="ph:sparkle"></Icon>         
        </h1>
        <p class="text-center text-lg max-sm:text-base"><Icon name="ph:caret-double-right-bold"></Icon> Full-Stack Developer / Quantum Engineer</p>
        <p class="text-center text-lg max-sm:text-base"><Icon name="ph:caret-double-right-bold"></Icon> Vue <Icon name="file-icons:vue"></Icon>, React <Icon name="simple-icons:react"></Icon>, Tailwind <Icon name="simple-icons:tailwindcss"></Icon>, Qiskit <Icon name="simple-icons:qiskit"></Icon></p>

      </section>
    </div>
      
  </SectionCard>
  
  <SectionCard CardIcon="ph:sparkle-bold" CardTitle="Pronounce" id="Pronouns">
      <div class="p-4 gap-2 grid grid-cols-12 auto-rows-auto ">
        
        <section 
          class="flex flex-col col-span-4 transition-all gap-1 max-sm:hidden "
        >
          <h1 class="text-center">What's a Pow?</h1>
          
          <nuxt-img src="/assets/images/tis_a_pow.webp" alt="this ia a pow">
            <SectionPronounsPrideflag
              class="h-5"
              flag="lesbian"
            ></SectionPronounsPrideflag>          
          </nuxt-img>
          
          <p class="text-justify  sm:pr-2">
            
          </p>
          
          <SectionPronounsPrideflag
            class="h-5"
            flag="trans"
          ></SectionPronounsPrideflag>
          
        </section>
        <section class="col-span-8 transition-all pb-4 max-sm:col-span-12">
          <div
            v-for="(section, i) in pronouns"
            :key="i"
            class="
              flex flex-col gap-2 max-sm:gap-1 py-2
            "
          >
          
            <h2 class="text-center">
              <Icon class="-mt-1 mr-1" :name="section.icon"></Icon>{{ useCapitalize(section.name) }}
            </h2>
            
            <ul class="grid auto-cols-auto grid-flow-row-dense max-lg:grid-cols-2 grid-cols-3 gap-2.5 max-sm:gap-1.5 text-sm max-sm:text-xs px-1.5">
              <SectionPronounsListblock
                v-for="(items, heading) in section.items"
                :key="heading"
                :heading="heading"
                :items="items"
              ></SectionPronounsListblock>
            </ul>
          </div>
        </section>
      </div>
    </SectionCard>

  <SectionCard CardIcon="ph:heart-bold" CardTitle="Socials and Links" id="Socials">
      <div class="p-4 gap-2 grid grid-cols-12 auto-rows-auto max-sm:gap-1">
        <ClientOnly>
          <SectionSocialLarge
            class="max-md:col-span-12 col-span-6 max-md:[&:not(:first-of-type)]:hidden"
            
            v-for="(showcase, index) in useSampleSize(showcaseList,2)"
            :key="index"
            
            :link="showcase.link"
            :img="showcase.img"
            :user="showcase.user"
            :name="showcase.name"
            :platform="showcase.platform"
            :icon="showcase.icon"
            :description="showcase.description"
          ></SectionSocialLarge>
        </ClientOnly>
        <section class="col-span-4 col-start-1 max-sm:col-span-12 transition-all py-4 max-sm:py-2 max-sm:pb-0">
          <h1 class="text-center">Socials</h1>
          <p class="text-justify  sm:pr-2">
            This is my list of social media links. Basically everywhere I have an account that may be active or inactive, as well as Project pages I've been working on. 
          </p>
          <br />
          
          
        
          
          
          <div class="
            max-sm:hidden
            grid place-items-stretch gap-2
            overflow-hidden 
            mb-4
          ">
            <h2 class="text-center ">Spotlight</h2>
            I'd really appreciate you supporting my FFS Fund. Every bit counts :)
            <NuxtLink 
              class="
              text-center
                p-2 font-extrabold cursor-pointer
                transition duration-300 ease-in-out 
                pink-hover
                border-white border-solid border-2 rounded-lg" 
              to="https://gofund.me/d53ecd05"
            > 
              <Icon class="-mt-1" name="uil:medical" />  
              FFS Fund
            </NuxtLink>


            <AppLinkCard CardLink="" CardTitle="Cosplay" CardIcon="game-icons:crystal-growth" >
              <NuxtImg 
                src="/assets/images/cosplay/Reki_1.jpg"
              ></NuxtImg>
            </AppLinkCard >
          </div>

          
            

        </section>
        
        <section class="col-span-8 col-start-5 max-sm:col-span-12 max-sm:col-start-1 transition-all py-2 max-sm:py-0 max-sm:-mt-5">
          <div 
          v-for="(section, i) in links"
          :key="i"
          
          class="
            
            flex flex-col gap-2 py-2 xl:grid xl:grid-cols-2 max-sm:py-2
          ">
            <h2 class="text-center col-span-2"> 
              <Icon class="-mt-1 mr-1" :name="section.icon"></Icon>{{ useCapitalize(section.name) }}
            </h2>
            
            <SectionSocialSmall
              class="xl:even:last-of-type:col-span-2"
            
              v-for="(data, i) in section.items"
              :key="i"
              
              :link="data.link"
              :img="data.img"
              :user="data.user? data.user : data.description"
              :name="data.name"
              :platform="data.platform"
              :icon="data.icon"
              
            >
            </SectionSocialSmall>
            
          </div>
        </section>
      </div>
      
    </SectionCard>
    
    
    
    
</template>

<script lang="ts" setup>


  const appConfig = useAppConfig();
  const {links, pronouns} = appConfig;
  
  const showcaseList = links.flatMap(section => section.items).filter(item => item.spotlight);
  
</script>



<style>



</style>
