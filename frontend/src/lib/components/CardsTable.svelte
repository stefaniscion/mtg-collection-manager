<script>
    import jQuery from "jquery";
    import DataTable from 'datatables.net-dt';
    import { onMount } from "svelte";
    onMount(async function() {
        const response = await fetch(url);
        cards = await response.json();
    });
</script>
    <input id={id+"_input"} type="text" placeholder="Search..." on:keyup={search} />
    <table id={id+"_table"} class="table-auto">
        <thead>
            <tr>
                <th></th>
                <th>id</th>
                <th>name</th>
                <th>qty</th>
                <th>alt</th>
                <th>foil</th>
                <th>cond</th>
            </tr>
        </thead>
        <tbody>
            {#each cards as card}
                <tr>
                    <td><img class="w-10" src={card.card_info.image_uris.art_crop}></td>
                    <td>{card.id}</td>
                    <td>{card.card_info.name}</td>
                    <td>{card.quantity}</td>
                    <td>{card.altered}</td>
                    <td>{card.foil}</td>
                    <td>{card.condition}</td>
                </tr>
            {/each}
        </tbody>
    </table>
