<script lang="ts">
	import { Dropdown } from "@gradio/form";
	import { Block } from "@gradio/atoms";
	import StatusTracker from "../StatusTracker/StatusTracker.svelte";

	export let label: string = "Dropdown";
	export let value: string = "";
	export let default_value: string = "";
	export let style: string = "";
	export let choices: Array<string>;
	export let form_position: "first" | "last" | "mid" | "single" = "single";

	export let loading_status: "complete" | "pending" | "error";

	export let mode: "static" | "dynamic";

	if (default_value) value = default_value;
</script>

<Block {form_position}>
	<StatusTracker tracked_status={loading_status} />

	<Dropdown
		bind:value
		{style}
		{choices}
		{label}
		on:change
		disabled={mode === "static"}
	/>
</Block>
