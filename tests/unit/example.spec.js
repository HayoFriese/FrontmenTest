import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld.vue'
import Login from '@/components/Login.vue'

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg }
    })
    expect(wrapper.text()).to.include(msg)
  })
})

describe('Login.vue', () => {
	it('checks if password matches the assignment criterias', () =>{
		const wrapper = shallowMount(Login)
		const passwordTests = [
			{password: 'password', expected: false},
			{password: 'abcdefghijklmnop', expected: false},
			{password: 'qweqweqweqweqweqweqweqweqweqweqwe', expected: false},
			{password: 'OverPowered', expected: false},
			{password: 'I can Fly', expected: false},
			{password: 's0Awsome', expected: false},
			{password: 'abcdef', expected: false},
			{password: 'aabbccddee', expected: false},
			{password: 'abceeff', expected: true},
			{password: 'aabbcd', expected: true}
		]
		passwordTests.forEach(pass => {
			expect(wrapper.vm.check(pass.password)).to.be.equal(pass.expected)
		})
	})
})