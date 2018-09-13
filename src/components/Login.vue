<template>
	<div class="login">
		<h2>Log In</h2>
		<p v-if="error">{{ errorMsg }}</p>
		<p v-else>Log in to save recipes and post your own!</p>
		<form method="get" @submit.prevent="login">
			<input type="text" name="username" v-model="username">
			<input type="text" name="password" v-model="password">
			<input type="submit" name="submit" value="Submit">
		</form>
	</div>
</template>
<script>
	export default{
		name: "Login",
		data() {
			return {
				username: '',
				password: '',
				error: false,
				errorMsg: ''
			}
		},
		methods: {
			// Method to check the password for the appropriate security considerations
			check(pass){				
				// Define an alphabet string in lower case and uppercase,
				// An alphabet count to check the amount of 3 letter straights
				// A pair count to check for non-overlapping character pairs
				// A letter to initialize the check
				// bl = banned letters
				let alphabet = 'abcdefghijklmnopqrstuvwxyz',
					capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
					acount = 0,
					pcount = 0,
					bl = 'iOl';
				if(pass.length <= 32){
					// loop through each character of the password
					for(let i=1; i < pass.length; i++){
						// if the password contains a bad letter, return false
						if(bl.indexOf(pass[i]) >= 0){
							console.log("Contains a banned letter");
							return false;
						}
						// if the current letter is a capital letter
						if(capital.indexOf(pass[i]) >= 0 || capital.indexOf(pass[i-1]) >= 0){
							console.log("Contains a capital letter");
							return false;
						}
						// If the current letter is equal to the letter that came before (aka pairing), add to the pair counter
						if(pass.charAt(i) === pass.charAt(i-1)){
							pcount++;
						}
						// if the current letter is not the last letter in the password
						if(i != (pass.length-1)){
							// if the current letter combined with its surrounding letters (making a straight) exists within the alphabet string, add to the straight counter
							if(alphabet.indexOf(pass.charAt(i-1)+pass.charAt(i)+pass.charAt(i+1)) >= 0){
								acount++;
							}
						}
					}
					// If the straight count is at least 1 and pair count is at least 2, return true, else false
					if(acount >= 1 && pcount >= 2){
						return true;
					}
				}
				return false;
				
			},
			login() {
				// Create error instance
				this.error = false;
				// If the form has been fully filled in
				if(this.username != "" && this.password != "") {
					// Check to see if password is properly validated
					if(this.check(this.password)){
						this.errorMsg = "Logged in successfully!";
						// Set username as session variable
						this.$session.set("username", this.username);
						// Reload the window from cache
						window.location.reload();
					} else {
						// Reveal error message
						this.error = true;
						this.errorMsg = "Password does not meet the security standards";
					}
				// Reveal another error message
				} else {
					this.error = true;
					this.errorMsg = "Please fill in all fields";
				}
			}
		}
	}
</script>