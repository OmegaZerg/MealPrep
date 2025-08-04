<script lang="ts">
	import StageColumn from '$lib/components/StageColumn.svelte';
	import type { CardData } from '$lib/types';
	type Props = {
		breakfasts: CardData[];
		lunches: CardData[];
		dinners: CardData[];
	};
  type timeSlotKey = 'Breakfast' | 'Lunch' | 'Dinner';
  type timeSlotData = Record<timeSlotKey, CardData[]>;

	const timeSlots: timeSlotKey[] = ['Breakfast', 'Lunch', 'Dinner'];
	let { breakfasts, lunches, dinners, handleCardClick } = $props();
	const timeSlotData: timeSlotData = {
		Breakfast: breakfasts,
		Lunch: lunches,
		Dinner: dinners
	};
</script>

<section class="grid-col-1 xl: grid-cols-3 px-4 lg:grid">
	{#each timeSlots as timeSlot}
		<StageColumn title={timeSlot} meals={timeSlotData[timeSlot]} {handleCardClick} />
	{/each}
</section>
