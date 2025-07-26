<script lang="ts">
	import Card from '$lib/components/Card.svelte';

	let { title, meals } = $props();
  let mealsWithTypes = $derived(
		meals.map((meal) => ({ ...meal, type: 'meal' as const }))
	);
</script>

<div class="flex h-full flex-col rounded-lg bg-slate-100 p-4">
	<div>
		{title}
	</div>
	<div>
		{#if mealsWithTypes.length < 1}
			<p>Add a meal to {title}</p>
		{:else}
			{#each mealsWithTypes as data (data.id)}
				<Card {data} />
			{/each}
		{/if}
	</div>
</div>
