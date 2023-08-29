<script>
    import { onMount } from 'svelte';
	const url = 'http://localhost:8000/card';
    let cards = [];

    onMount(async function() {
        const response = await fetch(url);
        cards = await response.json();
    });

</script>
<main>

    <CardsTable id="collection-table" cards={cards} />
    
</main>

