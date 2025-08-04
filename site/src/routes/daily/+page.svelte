<script lang="ts">
	import Stage from '$lib/components/Stage.svelte';
	import type { CardData } from '$lib/types';
	import { MOCK_DATA } from '$lib/tests';
	let mealsToShow = $state(MOCK_DATA);
	let breakfasts: CardData[] = mealsToShow.filter((meal) => meal.tag === 'breakfast');
	let lunches: CardData[] = mealsToShow.filter((meal) => meal.tag === 'lunch');
	let dinners: CardData[] = mealsToShow.filter((meal) => meal.tag === 'dinner');
</script>
<input class="mx-5" type="date" />
<Stage {breakfasts} {lunches} {dinners} handleCardClick={() => {}} />
