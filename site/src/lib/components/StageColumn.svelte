<script lang="ts">
	import Card from '$lib/components/Card.svelte';
	import type { CardData } from '$lib/types';
	type Props = {
		Breakfast: CardData;
		Lunch: CardData;
		Dinner: CardData;
	};

	let { title, meals, handleCardClick } = $props();
	let mealsWithTypes = $derived(meals.map((meal: CardData) => ({ ...meal, type: 'meal' as const })));
</script>

<div class="mx-1 flex h-full flex-col rounded-lg bg-slate-200 p-4">
	<div class="text-semibold text-3xl text-gray-500">
		{title}
	</div>
	<div>
		{#if mealsWithTypes.length < 1}
			<p>Add to {title} by clicking on meal cards</p>
		{:else}
			{#each mealsWithTypes as data (data.id)}
				<Card {data} onAddToStage={handleCardClick} />
			{/each}
		{/if}
	</div>
</div>
