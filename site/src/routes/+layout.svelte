<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<nav>
	<a href="/">Home</a>
	<a href="/daily">Daily View</a>
	<a href="/plan">Plan</a>
	<a href="/"></a>
	<a href="/"></a>
</nav>

{@render children()}
