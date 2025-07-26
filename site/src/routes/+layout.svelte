<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<nav class="w-full bg-orange-600 py-5 md:py-0">
	<div class="la:px-8 mx-auto max-w-7xl px-4 sm:px-6">
		<div class="flex h-16 items-center justify-between">
			<div class="flex flex-1 justify-start">
				<div class="flex items-baseline justify-start gap-x-4">
					<a href="/">Home</a>
					<a href="/daily">Daily View</a>
					<a href="/plan">Plan</a>
				</div>
			</div>
			<h1 class="px-4 text-xl md:text-4xl lg:text-5xl">Meal Prep</h1>
			<div class="flex flex-1 justify-end">
				<div class="flex items-baseline gap-x-4">
					<a href="/meals">Add Meals</a>
					<a href="/foods">Add Foods</a>
					<a href="#" class="invisible">Dummy Link</a>
				</div>
			</div>
		</div>
	</div>
</nav>

{@render children()}
