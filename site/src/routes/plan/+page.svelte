<script lang="ts">
	import Stage from '$lib/components/Stage.svelte';
	import Card from '$lib/components/Card.svelte';
<<<<<<< HEAD

	interface CardData {
		name: string;
		description: string;
		quantity?: number;
		unit?: string;
		type: 'food' | 'meal';
		tag?: 'breakfast' | 'lunch' | 'dinner';
		ingredients?: string[];
		calories: number;
		carbs: number;
		fat: number;
		protein: number;
	}

	// Test data, would use fetch from db
	let mealsToShow: CardData[] = $state([
		{
			type: 'meal',
			name: 'breakfast',
			description: 'food',
			tag: 'breakfast',
			calories: 200,
			carbs: 40,
			fat: 10,
			protein: 10
		},
		{
			type: 'meal',
			name: 'lunch',
			description: 'food',
			tag: 'lunch',
			calories: 200,
			carbs: 40,
			fat: 10,
			protein: 10
		},
		{
			type: 'meal',
			name: 'dinner',
			description: 'food',
			tag: 'dinner',
			calories: 200,
			carbs: 40,
			fat: 10,
			protein: 10
		}
	]);
=======
	import type { CardData } from '$lib/types';
	import { MOCK_DATA } from '$lib/tests';

	// interface CardData {
	// 	name: string;
	// 	description: string;
	// 	quantity?: number;
	// 	unit?: string;
	// 	type: 'food' | 'meal';
	// 	tag?: 'breakfast' | 'lunch' | 'dinner';
	// 	ingredients?: string[];
	// 	calories: number;
	// 	carbs: number;
	// 	fat: number;
	// 	protein: number;
	// }

	// Test data, would use fetch from db
	let mealsToShow: CardData[] = $state(MOCK_DATA);
>>>>>>> jon

	let breakfasts = $state<CardData[]>([]);
	let lunches = $state<CardData[]>([]);
	let dinners = $state<CardData[]>([]);
	let mealsFilter = $state('all');
	let filteredMeals = $derived.by(() => {
		if (!Array.isArray(mealsToShow)) {
			return [];
		}
		let mealsInLoop = mealsToShow.filter((meal) =>
			[breakfasts, lunches, dinners].every((timeslot) => !timeslot.includes(meal))
		);

		if (mealsFilter === 'all') {
			return mealsInLoop;
		}
		return mealsInLoop.filter((meal) => meal.tag === mealsFilter);
	});

	function handleAddToStage(mealToAdd: CardData) {
		console.log('firing');
		switch (mealToAdd.tag) {
			case 'breakfast':
				breakfasts.push(mealToAdd);
				break;
			case 'lunch':
				lunches.push(mealToAdd);
				break;
			case 'dinner':
				dinners.push(mealToAdd);
				break;
		}
	}
</script>

<Stage {breakfasts} {lunches} {dinners} handleCardClick={handleAddToStage} />

<<<<<<< HEAD
<div class="mx-5 grid grid-cols-2 md:grid-cols-4">
=======
<div class="mx-5 grid grid-cols-1 md:grid-cols-4 lg:grid-cols-6">
>>>>>>> jon
	<button onclick={() => (mealsFilter = 'all')}>All</button>
	<button onclick={() => (mealsFilter = 'breakfast')}>Breakfast</button>
	<button onclick={() => (mealsFilter = 'lunch')}>Lunch</button>
	<button onclick={() => (mealsFilter = 'dinner')}>Dinner</button>
	<button
		onclick={() => {
			breakfasts.length = 0;
			lunches.length = 0;
			dinners.length = 0;
		}}>Reset Stage</button
	>
</div>

<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
<<<<<<< HEAD
	<div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] justify-start gap-6">
		{#each filteredMeals as meal}
			<Card data={meal} onAddToStage={handleAddToStage} />
=======
	<div class="[display:grid] grid-cols-1 justify-items-center gap-4 lg:grid-cols-2 xl:grid-cols-3">
		{#each filteredMeals as meal}
			<div class="w-96">
				<Card data={meal} onAddToStage={handleAddToStage} />
			</div>
>>>>>>> jon
		{/each}
	</div>
</div>
