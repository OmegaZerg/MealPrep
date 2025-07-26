<script lang="ts">
	import StageColumn from "$lib/components/StageColumn.svelte";

  const timeSlots = ["Breakfast", "Lunch, Dinner"];
</script>

<input type="date">

<section>
  {#each timeSlots as timeSlot}
    <StageColumn  title={timeSlot}, meals={[]}/>
  {/each}
</section>