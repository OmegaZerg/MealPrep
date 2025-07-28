<script lang="ts">
	import Card from '$lib/components/Card.svelte';

	let { title, meals, handleCardClick } = $props();
	let mealsWithTypes = $derived(meals.map((meal) => ({ ...meal, type: 'meal' as const })));
</script>

<div class="mx-1 flex h-full flex-col rounded-lg bg-slate-200 p-4">
	<div class="text-semibold text-3xl text-gray-500">
		{title}
	</div>
	<div>
		{#if mealsWithTypes.length < 1}
			<p>Add a meal to {title}</p>
		{:else}
			{#each mealsWithTypes as data (data.id)}
				<Card {data} onAddToStage={handleCardClick} />
			{/each}
		{/if}
	</div>
</div>
