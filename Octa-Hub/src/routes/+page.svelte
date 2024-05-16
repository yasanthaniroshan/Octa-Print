<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>Welcome to the Octa-Print</h1>
	<div class="welcome">
		<a href="/submit" class="button">Getting Started</a>
	</div>
</section>

<style>
	@font-face {
		font-family: 'Octapus';
		font-style: normal;
		font-weight: 400;
		src: url('$lib/OctopusBold.woff2') format('woff2');
	}

	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		font-family: 'Octapus', sans-serif;
		font-size: 3rem;
		width: 100%;
	}

	.welcome {
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.button {
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
