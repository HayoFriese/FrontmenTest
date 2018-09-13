<template>
	<Login v-if="!session" />
	<main v-else>
		<TopNav />
		<LogoutButton/>
		<HelloWorld msg="About Page"/>
		<p>
			This is a second page. Feel free to logout and see what happens.
		</p>
		<p>
			For this test I kind of had to divert off of my original plan, as it became too complex to develop, despite everything being relatively set up. The original stack was to work as follows:
		</p>
		<ul>
			<li>Docker-compose file running three services:</li>
			<ol>
				<li>API, processing login, and written in python</li>
				<li>Frontend, in vue, processing the views and the sessions</li>
				<li>Database, where users would be stored</li>
			</ol>
			<li>An API with two calls: register and login. Register would create users in accordance to the password restrictions, and login would log you in</li>
			<li>A front-end module written in VueJS to load a page</li>
		</ul>
		<p>
			It became impossible to accomplish my goals, as I couldn't seem to get my API calls working from my frontend module due to headers being ommitted, no matter how much I tried to force them in. Given the deadline, I reverted to the Vue CLI.
		</p>
		<p>
			With the Vue CLI I set up a unit test in Mocha + Chai, and did the login rendering with a password. I think I might've misunderstood the challenge at first, so now I resolved it by running a check function in the login component. This function has a unit test in accordance to it, so feel free to set up some more password cases should you wish to see more cases.
		</p>
		<p>
			Because of the whole functionality ordeal, I didn't get a chance to create the design I wanted to. Should I have had one more day I'd have made a functioning design with Mock functionality. Based off of an existing design, I wanted to implement this:
		</p>
		<img src="../assets/recipe.png" v-bind:style="{'width': '100%'}" alt="Recipe Page">
	</main>
</template>

<script>
	import Login from '@/components/Login.vue'
	import HelloWorld from '@/components/HelloWorld.vue'
	import TopNav from '@/components/TopNav.vue'
	import LogoutButton from '@/components/LogoutButton.vue'

	export default {
		name: 'about',
		components: {
			Login,
			TopNav,
			HelloWorld,
			LogoutButton
		},
		data() {
			return {
				session: this.$session.get("username")
			}
		}
	}
</script>