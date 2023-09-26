<template>

	<SectionCard CardIcon="ph:house-bold" CardTitle="Home" id="Home">
    <div class="p-4">
      <section>
        <h1 class="text-center pb-4"><Icon name="ph:sparkle"></Icon>Hi_ I'm Pow<Icon name="ph:sparkle"></Icon> </h1>
        <p class="text-center text-lg max-sm:text-base"><Icon name="ph:caret-double-right-bold"></Icon> Full-Stack Developer / Quantum Engineer</p>
        <p class="text-center text-lg max-sm:text-base"><Icon name="ph:caret-double-right-bold"></Icon> Vue <Icon name="file-icons:vue"></Icon>, React <Icon name="simple-icons:react"></Icon>, Tailwind <Icon name="simple-icons:tailwindcss"></Icon>, Qiskit <Icon name="simple-icons:qiskit"></Icon></p>

      </section>
    </div>
      
  </SectionCard>

  <SectionCard CardIcon="ph:heart-bold" CardTitle="Socials and Links" id="Socials">
      <div class="p-4 gap-2 grid grid-cols-12 auto-rows-auto">
        
        <SectionSocialLarge
          class="max-md:col-span-12 col-span-6"
          
          :link="showcase[0].link"
          :img="showcase[0].img"
          :user="showcase[0].user"
          :name="showcase[0].name"
          :platform="showcase[0].platform"
          :icon="showcase[0].icon"
          :description="showcase[0].description"
        ></SectionSocialLarge>
        <SectionSocialLarge
          class="max-md:hidden col-span-6"
          
          :link="showcase[1].link"
          :img="showcase[1].img"
          :user="showcase[1].user"
          :name="showcase[1].name"
          :platform="showcase[1].platform"
          :icon="showcase[1].icon"
          :description="showcase[1].description"
        ></SectionSocialLarge>
        
        <section class="col-span-4 col-start-1 max-sm:col-span-12 transition-all py-4">
          <h1 class="text-center">Socials</h1>
          <p class="text-justify  sm:pr-2">
            This is my list of social media links. Basically everywhere I have an account that may be active or inactive, as well as Project pages I've been working on. So like basically my life lol.
          </p>
          <br />
          
          <span class="max-sm:hidden">
          
            <h2 class="text-center">Spotlight</h2>
            <p class="text-justify  sm:pr-2">
              social-media post spotlight here.
            </p>
            
          </span>
        </section>
        
        <section class="col-span-8 col-start-5 max-sm:col-span-12 max-sm:col-start-1 transition-all py-2">
          <div 
          v-for="(section, name) in links"
          :key="name"
          
          class="
            
            flex flex-col gap-2 py-2 lg:grid lg:grid-cols-2
          ">
            <h2 v-if="name != 'showcase'" class="text-center col-span-2">{{ useCapitalize(name) }}</h2>
            
            <SectionSocialSmall
              v-if="name != 'showcase'"
              v-for="(data, i) in section"
              :key="i"
              
              :link="data.link"
              :img="data.img"
              :user="data.user"
              :name="data.name"
              :platform="data.platform"
              :icon="data.icon"
              
            >
            </SectionSocialSmall>
            
          </div>
        </section>
      </div>
      
    </SectionCard>
    
    <SectionCard CardIcon="ph:sparkle-bold" CardTitle="Pronounce" id="Pronouns">
      <div class="p-4 gap-2 grid grid-cols-12 auto-rows-auto ">
        <section class="flex flex-col col-span-4 max-sm:col-span-5 transition-all gap-2">
          <h1 class="text-center">Who's Pow?</h1>
          
          <SectionPronounsPrideflag
            class="h-5"
            flag="lesbian"
          ></SectionPronounsPrideflag>
          
          <p class="text-justify  sm:pr-2">
            Pow is a 21 year old transbian that lives in Austria. 
          </p>
          
          <SectionPronounsPrideflag
            class="h-5"
            flag="trans"
          ></SectionPronounsPrideflag>
          
          //Donate button//
          
        </section>
        <section class="col-span-8 max-sm:col-span-7 transition-all pb-4">
          <div
            v-for="(section, name) in pronouns"
            :key="name"
            class="
              flex flex-col gap-2 py-2
            "
          >
          
            <h2 class="text-center">{{useCapitalize(name)}}</h2>
            
            <ul class="grid grid-cols-3 max-sm:grid-cols-1 gap-2.5 text-sm max-sm:text-xs px-1.5">
              <SectionPronounsListblock
                v-for="(items, heading) in section"
                :key="heading"
                :heading="heading"
                :items="items"
              ></SectionPronounsListblock>
            </ul>
          </div>
        </section>
      </div>
    </SectionCard>
    
    
</template>

<script lang="ts" setup>
  const appConfig = useAppConfig();
  const {links, pronouns} = appConfig;
  
  const showcase = useSampleSize(links.showcase,2)
  
</script>



<style>



</style>
