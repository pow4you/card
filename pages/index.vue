<template>

	<SectionCard CardIcon="ph:house-bold" CardTitle="Home" id="Home">
    <div class="p-4">
      <section>
        <h1 class="text-center"><Icon name="ph:sparkle"></Icon>Hi_ I'm Pow<Icon name="ph:sparkle"></Icon> </h1>
        <p class="p-4 sm:px-12 md:px-24"><Icon name="ph:caret-double-right-bold"></Icon>Full-Stack Developer / Quantum Engineer  </p>
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
        
        <section class="col-span-5 col-start-1 max-sm:col-span-12 transition-all py-4">
          <h1 class="text-center">Socials</h1>
          <p class="text-justify  sm:pr-2">
            This is my list of social media links. Basically everywhere I have an account that may be active or inactive, as well as Project pages I've been working on. So like basically my life lol.
          </p>
        </section>
        
        <section class="col-span-7 col-start-6 max-sm:col-span-12 max-sm:col-start-1 transition-all py-2">
          <div 
          v-for="(section, name) in links"
          :key="name"
          
          class="
            
            flex flex-col gap-2 py-2
          ">
            
            <h2 class="text-center">{{ useCapitalize(name) }}</h2>
            
            <SectionSocialSmall
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
      <div class="p-4 gap-2 grid grid-cols-12 auto-rows-auto">
        <section class="col-span-5 col-start-1 max-md:col-span-12 transition-all"></section>
        <section class="col-span-7 col-start-6 max-md:col-span-12 max-sm:col-start-1 transition-all pb-4">
          <h2 class="text-center">Names</h2>
          
          <ul class="grid grid-cols-3 max-sm:grid-cols-1 gap-2.5 text-sm max-sm:text-xs px-1.5">
            <li class="
              p-2
              drop-shadow-md frosted-glass rounded-lg 
              border-white border-solid border-2
            ">
              Main:
              <ul class="list-disc ml-4">
                <li>Pow/Powowo</li>
                <li>Nasa</li>
                <li>Danger</li>
              </ul>
            </li>
            
            <li class="
              p-2
              drop-shadow-md frosted-glass rounded-lg 
              border-white border-solid border-2
            ">
              Fun:
              <ul class="list-disc ml-4">
                <li>Cat</li>
                <li>Ze</li>
                <li>Nghariad</li>
              </ul>
              
            </li>
            
            <li class="
              p-2
              drop-shadow-md frosted-glass rounded-lg 
              border-white border-solid border-2
            ">
              Aliases:
              <ul class="list-disc ml-4">
                <li>Powo</li>
                <li>PowowoCat</li>
                <li>PowCat</li>
              </ul>
            </li>
          </ul>
          
          <h2 class="text-center p-0">Pronouns</h2>
        
        </section>
      </div>
    </SectionCard>
    
    
</template>

<script lang="ts" setup>
  const appConfig = useAppConfig();
  const links = appConfig.links;
  
  const showcase = useSampleSize(links.showcase,2)
  const other = useSlice(links,1)
</script>



<style>



</style>
