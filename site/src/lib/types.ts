export interface CardData {
  id?: number;
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
