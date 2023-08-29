<script>
	const pages = [
    {
        title: "Dashboard",
        url: "/",
        icon: "fas fa-home",
    },
    {
        title: "Collection",
        url: "/collection",
        icon: "fas fa-info-circle",
    },
    {
        title: "Test",
        url: "/test",
        icon: "fas fa-info-circle",
    }
  ];
</script>


<ul>
  {#each pages as page}
  <li class="px-5 py-2">
    <span class="{page.icon}"></span>
    <a href={page.url}>{page.title}</a>
  </li>
  {/each}
</ul>