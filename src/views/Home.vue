<template>
	<main>
		<div v-if="!session">
			<HelloWorld msg="Welcome to Your Vue.js App"/>
			<Login />
		</div>
		<div v-else-if="session">
			<div>
				<TopNav />
				<HelloWorld msg="Welcome to Your Vue.js App"/>
				<LogoutButton />
			</div>
			<Success />
		</div>
	</main>
</template>

<script>
	import HelloWorld from '@/components/HelloWorld.vue'
	import Login from '@/components/Login.vue'
	import TopNav from '@/components/TopNav.vue'
	import LogoutButton from '@/components/LogoutButton.vue'
	import Success from '@/components/Success.vue'


	export default {
		name: 'home',
		components: {
			HelloWorld,
			Login,
			TopNav,
			LogoutButton,
			Success
		},
		data() {
			return {
		    	session: this.$session.get("username")
		    }
		},
		methods:{
		    logout: function(){
		    	console.log(this.$session.get("username"));
		    	this.$session.clear();
		    }
		}
	}
</script>