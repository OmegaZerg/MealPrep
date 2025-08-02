<script lang="ts">
	import StageColumn from '$lib/components/StageColumn.svelte';
<<<<<<< HEAD

=======
  
>>>>>>> jon
	const timeSlots = ['Breakfast', 'Lunch', 'Dinner'];
	let { breakfasts, lunches, dinners, handleCardClick } = $props();
  const timeSlotData = {
		Breakfast: breakfasts,
		Lunch: lunches,
		Dinner: dinners,
	};
</script>

<input class="mx-5" type="date" />

<<<<<<< HEAD
<section class="grid-col-1 md:grid grid-cols-3">
=======
<section class="grid-col-1 lg:grid grid-cols-3 xl: px-4">
>>>>>>> jon
	{#each timeSlots as timeSlot}
		<StageColumn title={timeSlot} meals={timeSlotData[timeSlot]} {handleCardClick}/>
	{/each}
</section>
