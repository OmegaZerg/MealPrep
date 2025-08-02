import type { CardData } from '$lib/types'; // Assuming your types are in src/lib/types.ts

export const MOCK_DATA: CardData[] = [
	// --- BREAKFAST MEALS ---
	{
		id: 1,
		type: 'meal',
		name: 'Classic Scrambled Eggs',
		description: 'A simple, protein-packed start to the day. Fluffy eggs cooked to perfection.',
		ingredients: ['2 large eggs', '1 tbsp milk', '1 tsp butter', 'Salt & pepper'],
		tag: 'breakfast',
		calories: 250,
		carbs: 2,
		fat: 18,
		protein: 15
	},
	{
		id: 2,
		type: 'meal',
		name: 'Oatmeal with Berries',
		description:
			'Heart-healthy rolled oats topped with fresh mixed berries and a hint of cinnamon.',
		ingredients: ['1/2 cup rolled oats', '1 cup water', '1/2 cup mixed berries', 'Cinnamon'],
		tag: 'breakfast',
		calories: 300,
		carbs: 55,
		fat: 5,
		protein: 10
	},
	{
		id: 3,
		type: 'meal',
		name: 'Avocado Toast',
		description: 'Toasted sourdough bread with mashed avocado, lemon juice, and red pepper flakes.',
		ingredients: ['1 slice sourdough bread', '1/2 avocado', 'Lemon juice', 'Red pepper flakes'],
		tag: 'breakfast',
		calories: 280,
		carbs: 30,
		fat: 15,
		protein: 8
	},

	// --- LUNCH MEALS ---
	{
		id: 4,
		type: 'meal',
		name: 'Grilled Chicken Salad',
		description:
			'A light yet filling salad with grilled chicken breast, mixed greens, cherry tomatoes, and a light vinaigrette.',
		ingredients: [
			'4oz chicken breast',
			'2 cups mixed greens',
			'1/2 cup cherry tomatoes',
			'2 tbsp vinaigrette'
		],
		tag: 'lunch',
		calories: 450,
		carbs: 10,
		fat: 25,
		protein: 40
	},
	{
		id: 5,
		type: 'meal',
		name: 'Quinoa Power Bowl',
		description:
			'A vibrant bowl of quinoa, black beans, corn, avocado, and a lime-cilantro dressing. This is a very long description to test how the card handles text overflow and wrapping within its container.',
		ingredients: [
			'1 cup cooked quinoa',
			'1/2 cup black beans',
			'1/2 cup corn',
			'1/4 avocado',
			'Lime-cilantro dressing'
		],
		tag: 'lunch',
		calories: 550,
		carbs: 70,
		fat: 20,
		protein: 25
	},
	{
		id: 6,
		type: 'meal',
		name: 'Turkey Club Sandwich',
		description: 'Classic triple-decker sandwich with turkey, bacon, lettuce, and tomato.',
		ingredients: [
			'3 slices of bread',
			'4oz turkey breast',
			'2 strips bacon',
			'Lettuce',
			'Tomato',
			'Mayonnaise'
		],
		tag: 'lunch',
		calories: 600,
		carbs: 45,
		fat: 30,
		protein: 35
	},

	// --- DINNER MEALS ---
	{
		id: 7,
		type: 'meal',
		name: 'Salmon with Asparagus',
		description: 'Pan-seared salmon fillet served with roasted asparagus and a lemon wedge.',
		ingredients: ['6oz salmon fillet', '1 bunch asparagus', '1 tbsp olive oil', 'Lemon'],
		tag: 'dinner',
		calories: 500,
		carbs: 8,
		fat: 30,
		protein: 45
	},
	{
		id: 8,
		type: 'meal',
		name: 'Spaghetti Bolognese',
		description: 'A hearty and traditional Italian meat sauce served over spaghetti pasta.',
		ingredients: [
			'4oz ground beef',
			'1/2 cup tomato sauce',
			'1 cup spaghetti pasta',
			'Onion',
			'Garlic'
		],
		tag: 'dinner',
		calories: 650,
		carbs: 75,
		fat: 25,
		protein: 30
	},
	{
		id: 9,
		type: 'meal',
		name: 'Vegetable Stir-fry with Tofu',
		description:
			'A quick and healthy stir-fry with a variety of colorful vegetables and firm tofu in a savory soy-ginger sauce.',
		ingredients: [
			'1 block firm tofu',
			'Broccoli florets',
			'Bell peppers',
			'Carrots',
			'Snap peas',
			'Soy sauce',
			'Ginger'
		],
		tag: 'dinner',
		calories: 400,
		carbs: 35,
		fat: 18,
		protein: 22
	},

	// --- INDIVIDUAL FOOD ITEMS ---
	{
		id: 101,
		type: 'food',
		name: 'Apple',
		description: 'A crisp, sweet fruit.',
		quantity: 1,
		unit: 'medium',
		calories: 95,
		carbs: 25,
		fat: 0.3,
		protein: 0.5
	},
	{
		id: 102,
		type: 'food',
		name: 'Almonds',
		description: 'A handful of raw, unsalted almonds.',
		quantity: 1,
		unit: 'oz (about 23 nuts)',
		calories: 164,
		carbs: 6,
		fat: 14,
		protein: 6
	},
	{
		id: 103,
		type: 'food',
		name: 'Greek Yogurt',
		description: 'Plain, non-fat Greek yogurt.',
		quantity: 1,
		unit: 'cup',
		calories: 100,
		carbs: 6,
		fat: 0,
		protein: 17
	},
	{
		id: 104,
		type: 'food',
		name: 'Peanut Butter',
		description: 'Natural, unsweetened peanut butter.',
		quantity: 2,
		unit: 'tbsp',
		calories: 190,
		carbs: 7,
		fat: 16,
		protein: 8
	},
	{
		id: 105,
		type: 'food',
		name: 'Whole Wheat Bread',
		description: 'A single slice of whole wheat bread.',
		quantity: 1,
		unit: 'slice',
		calories: 80,
		carbs: 14,
		fat: 1,
		protein: 4
	},
	{
		id: 106,
		type: 'food',
		name: 'Olive Oil',
		description: 'Extra virgin olive oil.',
		quantity: 1,
		unit: 'tbsp',
		calories: 120,
		carbs: 0,
		fat: 14,
		protein: 0
	}
];
