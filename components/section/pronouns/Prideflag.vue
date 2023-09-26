<template>
  <div
    :class="
      orientation?orientation:'horizontal'
    "
  >
    <div id="flag" :class="'h-full w-full ' + flag"></div>
    
  </div>
</template>

<script lang="ts" setup>
  const props = defineProps<{
    flag: 
      "lgbt" | 
      
      "gay" | "gay-7bars" | 
      "lesbian" | "lesbian-7bars" | 
      "bi" | "pan" | 
      "ace" | "asexual" | "aro" | "aromantic" | "demi" | "demisexual" |
      
      "trans" | "transgender" | "enby" | "non-binary"
    ;
    orientation?: "horizontal" | "vertical";
  }>();

  const { flag, orientation } = props;
</script>



<style>
:root {
  --orientation: 0turn;
}


.horizontal {
  --orientation: 0.25turn
}

.vertical {
  --orientation: 0turn;
}

.lgbt {
	background: linear-gradient(
	  var(--orientation),
	  #e00 16.66%,
		#f80 16.66%, 33.33%,
		#fe0 33.33%, 50%,
		#082 50%, 66.66%,
		#05f 66.66%, 83.33%,
		#708 83.33%);
}

.gay {
	background: linear-gradient(
	  var(--orientation),
	  #097 20%,
		#aec 20%, 40%,
		#fff 40%, 60%,
		#7be 60%, 80%,
		#427 80%);
}

.gay-7bars {
	background: linear-gradient(
	  var(--orientation),
	  #097 14.29%,
		#2da 14.29%, 28.57%,
		#aec 28.57%, 42.86%,
		#fff 42.86%, 57.14%,
		#7be 57.14%, 71.43%,
		#54c 71.43%, 85.71%,
		#427 85.71%);
}

.lesbian {
	background: linear-gradient(
	  var(--orientation),
	  #d30 20%,
		#f95 20%, 40%,
		#fff 40%, 60%,
		#d6a 60%, 80%,
		#a06 80%);
}

.lesbian-7bars {
	background: linear-gradient(
	  var(--orientation),
	  #d30 14.29%,
		#e72 14.29%, 28.57%,
		#f95 28.57%, 42.86%,
		#fff 42.86%, 57.14%,
		#d6a 57.14%, 71.43%,
		#b59 71.43%, 85.71%,
		#a06 85.71%);
}

.bi, .bisexual {
	background: linear-gradient(
	  var(--orientation),
	  #d07 37.55%,
		#959 37.5%, 62.5%,
		#03a 62.5%);
}

.pan, .pansexual {
	background: linear-gradient(
	  var(--orientation),
	  #f28 33.33%,
		#fd0 33.33%, 66.66%,
		#2bf 66.66%);
}

.ace, .asexual {
	background: linear-gradient(
	  var(--orientation),
	  #000 25%,
		#aaa 25%, 50%,
		#fff 50%, 75%,
		#808 75%);
}

.aro, .aromantic {
	background: linear-gradient(
	  var(--orientation),
	  #3a4 20%,
		#ad7 20%, 40%,
		#fff 40%, 60%,
		#bbb 60%, 80%,
		#000 80%);
}


.trans, .transgender {
	background: linear-gradient(
	  var(--orientation),
	  #6cf 20%,
		#fab 20%, 40%,
		#fff 40%, 60%,
		#fab 60%, 80%,
		#6cf 80%);
}

.enby, .non-binary {
	background: linear-gradient(
	  var(--orientation),
	  #ff3 25%,
		#fff 25%, 50%,
		#95d 50%, 75%,
		#222 75%);
}

.demi, .demisexual {
    background: linear-gradient(
        var(--orientation),
        #000 20%,
        #fff 20%, 40%,
        #808 40%, 60%,
        #fff 60%, 80%,
        #000 80%
    );
}


</style>
