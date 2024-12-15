const loginForm = document.querySelector('#login-form')
const loginInput = document.querySelector("#login-form input")
const loginBtn = document.querySelector("#login-form input:last-child")
const greeting = document.querySelector('#greeting')

const onLoginSubmit = (e) => {
  e.preventDefault()
  loginForm.classList.add("hidden")
  const username = loginInput.value
  localStorage.setItem('username', username)
  paintGreeting(username)
}

const paintGreeting = (username) => {
  greeting.innerText = `Hello ${username}`
  greeting.classList.remove("hidden")
}

// submit 이벤트는 enter나 버튼 클릭시 발생
loginForm.addEventListener("submit", onLoginSubmit)

const savedUsername = localStorage.getItem("username")
// 이전에 로그인한 기록이 있다면                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        숨겼던 로그인폼 보여주기
if(savedUsername === null) {
  loginForm.classList.remove("hidden")
} else {
  paintGreeting(savedUsername)
}