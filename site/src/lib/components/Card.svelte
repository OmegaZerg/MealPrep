<script lang="ts">
	import type { CardData } from '$lib/types';

	type Props = {
		data: CardData;
		onAddToStage(meal: CardData): (item: CardData) => void;
	};
	let { data, onAddToStage } = $props();

	console.log(data);
</script>

<button
	class="!block !w-full !border-none !bg-transparent !text-left transition !outline-none hover:scale-[1.05]"
	onclick={() => onAddToStage(data)}
>
	<article
		class="flex aspect-[1.33] h-full flex-col !gap-0 overflow-hidden rounded-lg p-3 shadow-lg"
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
