<script lang="ts">
<<<<<<< HEAD
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
=======
	import type { CardData } from '$lib/types';
>>>>>>> jon

	type Props = {
		data: CardData;
		onAddToStage(meal: CardData): (item: CardData) => void;
	};
<<<<<<< HEAD
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
=======

	let { data, onAddToStage } = $props();

</script>

<button
	class="!block !w-full !border-none !bg-transparent !text-left transition !outline-none hover:scale-[1.05]"
	onclick={() => onAddToStage(data)}
>
	<article
		class="flex aspect-[1.33] h-full flex-col !gap-0 overflow-hidden rounded-lg p-3 shadow-lg !bg-blue-950"
	>
		<h2 class="text-center !text-xl font-bold">{data.name}</h2>
		<div class="flex flex-1 gap-4 overflow-hidden">
			<div class="info flex basis-[70%] flex-col !gap-0 overflow-y-auto pr-2">
				{#if data.type === 'food'}
					<p class="!text-xs">Description: {data.description}</p>
					<p class="!text-xs">
						Amount: {data.quantity}
						{data.unit ? data.unit : ''}
					</p>
				{:else if data.type === 'meal'}
					<p class="!text-xs">Description: {data.description}</p>
					<p class="!text-xs">Ingredients: {data.ingredients}</p>
				{:else}
					<p class="!text-xs">{data.name} is not valid</p>
				{/if}
			</div>
			<div class="macros basis-[30%] !gap-0 border-l border-slate-200 pl-4">
				<h2 class="!text-lg font-bold">Macros:</h2>
				<p class="!text-xs">
					Calories: {data.calories} kcal
				</p>
				<p class="!text-xs">
					Carbs: {data.carbs}g
				</p>
				<p class="!text-xs">
					Fat: {data.fat}g
				</p>
				<p class="!text-xs">
					Protein: {data.protein}g
				</p>
			</div>
		</div>
	</article>
</button>
>>>>>>> jon
