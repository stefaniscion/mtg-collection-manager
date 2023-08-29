<script>
  import "../app.css";
	import Menu from './Menu.svelte';
</script>

<div class="flex flex-row h-screen text-slate-100">
  <aside class="max-w-max bg-slate-900 px-5 py-5">
    <Menu/>
  </aside>
  <div class="grow bg-slate-800 px-10 py-5">
    <slot/>
  </div>
</div>