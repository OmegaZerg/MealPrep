<script lang="ts">
  let data = $props();
</script>

<article class="flex w-full flex-col shadow-lg aspect-[1.4] p-5">
  <h2>{data.name}</h2>
  {#if data.type === "food"}
    
  {:else if data.type === "meal"}
  {:else}
    <p>{data.name} is not valid</p>
  {/if}
</article>