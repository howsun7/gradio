<script lang="ts">
	import { Checkbox } from "@gradio/form";
	import { Block } from "@gradio/atoms";
	import StatusTracker from "../StatusTracker/StatusTracker.svelte";

	export let value: boolean = false;
	export let default_value: boolean = false;
	export let style: string = "";
	export let label: string = "Checkbox";
	export let mode: "static" | "dynamic";
	export let form_position: "first" | "last" | "mid" | "single" = "single";

	export let loading_status: "complete" | "pending" | "error";

	if (default_value) value = default_value;
</script>

<Block {form_position}>
	<StatusTracker tracked_status={loading_status} />

	<Checkbox {style} {label} bind:value on:change disabled={mode === "static"} />
</Block>
