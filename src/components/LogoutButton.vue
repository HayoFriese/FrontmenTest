<template>
	<div>
		<button @click="logout()">Log Out</button>
	</div>
</template>

<script>
	export default{
		name: 'LogoutButton',
		methods: {
			logout: function(){
				this.$session.clear();
				window.location.reload();
			}
		}
	}
</script>

<style lang="scss">
	button{
		display:block;
		margin:0 auto;
	}
	
</style>