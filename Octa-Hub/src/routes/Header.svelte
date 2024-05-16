<script>
	import { page } from '$app/stores';
	import Octa_print from '$lib/Octa-Print.png';
</script>

<header>
	<div class="corner"></div>

	<nav>
		<div class="header">
			<img class="logo" src={Octa_print} alt="" />
			<a href="/submut" class="button">Getting Started</a>
		</div>
	</nav>

	<div class="corner"></div>
</header>

<style>
	.header {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		padding: 10px;
	}
	.logo {
		/* align-self: flex-start; */
		max-width: 100px;
	}
	.button {
		cursor: pointer;
		width: 50px;
		height: 50px;
	}
</style>
