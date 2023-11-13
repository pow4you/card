<template>
  <AppBonusbar class="mt-3" :links='[
    {name: "Introduction", icon:"ph:shooting-star", url: "/about/"},
    {name: "Interests", icon:"ph:potted-plant", url: "/about/#Interests"},
    {name: "Skills", icon:"ph:planet", url: "/about/#Skills"},
    {name: "Projects", icon:"ph:rocket-launch", url: "/about/#Projects"},
    {name: "Contact", icon:"ph:seal-check", url: "/about/#Contact"},
  ]' />
  
  <SectionCard CardIcon="ph:shooting-star-bold" CardTitle="Introduction" id="Introduction">
    <div class="p-4">
      <section>
        <h1 class="text-center pb-4">
          <Icon class="mx-.5" name="ph:sparkle"></Icon>
          Who is Pow?
          <Icon class="mx-.5" name="ph:sparkle"></Icon> 
        </h1>
        <p class="py-1">I'm Pow, a curious and dedicated web developer from Vienna. I love turning complex problems into beautiful, simple solutions that work for everyone.</p>
        <h2 class="text-center pt-3">What Drives Me?</h2>
        <p class="py-1">Driven by curiosity, I use this website to document my journey, share my creations, and connect with like-minded individuals and potential collaborators.</p>
      </section>
    </div>
      
  </SectionCard>
  
  <SectionCard CardIcon="ph:potted-plant-bold" CardTitle="Interests" id="Interests">
    <div class="p-4">
      <section>
        <h1 class="pt-3">Dev Diaries</h1>
        <p class="py-1">Web dev is my battleground and my playground. I take those cryptic lines of code and bend them to my will (usually). Sometimes it's a smooth sail; other times, it's like herding cats in a code editor. But the thrill of making something out of nothing? Absolutely worth it!</p>

        <h2 class="pt-1">Quantum Quirks</h2>
        <p class="py-1">Quantum tech is like the rebellious teen of the tech world - unpredictable but fascinating. Tinkering with quantum algorithms is like solving a puzzle designed by a mad scientist. It's tough, but hey, I eat tough for breakfast (with a side of quantum entanglement).</p>
        
        
        <h1 class="mt-6">Cosplay Chronicles</h1>
        <p class="py-1">Let's talk about my cosplay triad - Angel Devil, Makima, and Vriska. Each one is a labor of love and a dash of chaos. Angel Devil has me sprouting wings and attitude, while Makima brings out a fierce leader vibe. And Vriska? She's my starry-eyed, mischievous side taking the stage.</p>
        <p class="py-1">In the cosplay universe, I'm a shape-shifter. With every stitch and swipe of eyeliner, I'm not just putting on a costume; I'm embodying a story. It's not just dress-up; it's about breathing life into characters, and let's be real – it’s an excuse to use my coding skills for cool LED effects in my outfits!</p>
        <p class="py-1">Conventions are my catwalks, where I strut my stuff and meet my tribe. It's a world where we celebrate the odd, the fantastic, and the fandom. The energy is electric, the creativity is off the charts, and the support is heartwarming. We're all a bit bonkers here, and it's beautiful.</p>

        <h2 class="pt-3">Vrizzy</h2>
        <p class="py-1">Homestuck? More like Home-love! I'm all about those quirky characters and wild plot twists. It's a world where I can be as weird as I want, and nobody bats an eye. Plus, who doesn't love a good meme-fest wrapped in an epic saga?</p>
        
      </section>
    </div>
      
  </SectionCard>
  
  <SectionCard CardIcon="ph:planet-bold" CardTitle="Skills" id="Skills">
    <div class="p-4">
      <section>
        <h2 class="">Technical Expertise</h2>
        <p class="">From Java to Python, VUE to React, I've got a wide range of skills to build robust and user-friendly web applications. I'm also adept at navigating databases with SQL and crafting RESTful services.</p>
        <h2 class="">Continuous Learner</h2>
        <p class="">I believe in lifelong learning and am always updating my skill set to stay ahead in the fast-paced world of tech.</p>
      </section>
    </div>
      
  </SectionCard>
  
  <SectionCard CardIcon="ph:rocket-launch-bold" CardTitle="Projects" id="Projects">
    <div class="p-4">
      <section>
        <h2 class="">What I'm Working On</h2>
        <p class="">Currently, I'm refining a 'Coming Soon' page that hints at the future of my online presence, and developing an innovative 'Animal Certificate Dev Page' as part of a dynamic university project.</p>
      </section>
    </div>
      
  </SectionCard>
  
  <SectionCard CardIcon="ph:seal-check-bold" CardTitle="Get in Touch?" id="Contact">
    <div class="p-4">
      <section>
        <p class="">Got questions or want to collaborate? Reach out at [contact@pow.gay]. Let's create something amazing together!</p>
      </section>
    </div>
      
  </SectionCard>
</template>

<script lang="ts" setup>
  
  
</script>



<style scoped lang="postcss">
*{
    @apply scroll-smooth scroll-mt-24
}
</style>
