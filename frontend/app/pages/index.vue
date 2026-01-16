<template>
    <div class="">
        <UInput v-model="firstName" placeholder="first name"/>
        <UInput v-model="lastName" placeholder="last name"/>
        <UInput v-model="email" placeholder="email"/>
        <UButton @click="addUser">Add user</UButton>
    </div>
</template>

<script setup>
const firstName = ref('')
const lastName = ref('')
const email = ref('')

// Create a computed property for reactive body
const requestBody = computed(() => ({
  firstName: firstName.value,
  lastName: lastName.value,
  email: email.value
}))

const {data, refresh:store_user, error} = useFetch('http://127.0.0.1:8000/signin/signin', {
    method: 'POST',
    body: requestBody,
    immediate: false
})

const addUser = () => {
    console.log(firstName.value, lastName.value, email.value); 
    store_user()
}

</script>