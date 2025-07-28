<script lang="ts">
	interface CardData {
		name: string;
		description: string;
		quantity: number;
		unit: string;
		type: 'food' | 'meal';
		tag?: 'breakfast' | 'lunch' | 'dinner';
		ingredients?: string[];
		calories: number;
		carbs: number;
		fat: number;
		protein: number;
	}

	type Props = {
		data: CardData;
		onAddToStage(meal: CardData): (item: CardData) => void;
	};
	let { data, onAddToStage } = $props();
</script>

<!-- svelte-ignore a11y_no_noninteractive_element_to_interactive_role -->
<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<article
	class="flex aspect-[1.33] w-80 cursor-pointer flex-col p-5 shadow-lg transition hover:scale-[1.02]"
	onclick={() => onAddToStage(data)}
	onkeydown={(e: KeyboardEvent) => {
		if (e.key === 'Enter' || e.key === ' ') {
			e.preventDefault();
			onAddToStage(data);
		}
	}}
	tabindex="0"
>
	<h4 class="text-base">{data.name}</h4>
	{#if data.type === 'food'}
		<p class="text-sm">Description: {data.description}</p>
		<p class="text-sm">Amount: {data.quantity} {data.unit ? data.unit : ''}</p>
	{:else if data.type === 'meal'}
		<p class="text-sm">Description: {data.description}</p>
		<p class="text-sm">Ingredients: {data.ingredients}</p>
	{:else}
		<p class="text-sm">{data.name} is not valid</p>
	{/if}
	<h5 class="text-base">Macros:</h5>
	<p class="text-sm">Calories: {data.calories}</p>
	<p class="text-sm">Carbs: {data.carbs}</p>
	<p class="text-sm">Fat: {data.fat}</p>
	<p class="text-sm">Protein: {data.protein}</p>
</article>
