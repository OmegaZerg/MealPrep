export interface CardData {
<<<<<<< HEAD
	name: string;
	description: string;
	quantity: number;
	unit: string;
=======
  id?: number;
	name: string;
	description: string;
	quantity?: number;
	unit?: string;
>>>>>>> jon
	type: 'food' | 'meal';
	tag?: 'breakfast' | 'lunch' | 'dinner';
	ingredients?: string[];
	calories: number;
	carbs: number;
	fat: number;
	protein: number;
}
