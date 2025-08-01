<script lang="ts">
	import StageColumn from '$lib/components/StageColumn.svelte';
  
	const timeSlots = ['Breakfast', 'Lunch', 'Dinner'];
	let { breakfasts, lunches, dinners, handleCardClick } = $props();
  const timeSlotData = {
		Breakfast: breakfasts,
		Lunch: lunches,
		Dinner: dinners,
	};
</script>

<input class="mx-5" type="date" />

<section class="grid-col-1 md:grid grid-cols-3">
	{#each timeSlots as timeSlot}
		<StageColumn title={timeSlot} meals={timeSlotData[timeSlot]} {handleCardClick}/>
	{/each}
</section>
