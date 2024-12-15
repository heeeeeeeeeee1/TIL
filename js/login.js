// 프로필 구성
const characters = document.querySelectorAll("#characters img")
const charactersContainer = document.querySelector("#characters")
const profileSection = document.querySelector("#profile")
const profileImage = document.querySelector("#profile-image")
const profileUsername = document.querySelector("#profile-username")
const main = document.querySelector("main")
const profileContainer = document.querySelector(".profile-container")

let selectedCharacter = null

// 캐릭터 선택하기  
const selectCharacter = (e) => {
  characters.forEach((img) => img.classList.remove("selected")) // 캐릭터 선택 초기화
  e.target.classList.add("selected")
  selectedCharacter = e.target.dataset.profile // 선택된 캐릭터 프로필 정보 저장
}
// 모든 캐릭터 이미지에 이벤트 리스너 추가
characters.forEach((img) => img.addEventListener("click", selectCharacter)) 


// 로그인
const loginForm = document.querySelector('#login-form')
const loginInput = document.querySelector("#login-form input")
const loginBtn = document.querySelector("#login-form input:last-child")
const greeting = document.querySelector('#greeting')
const todoContainer = document.querySelector("#todo-container")
const logoutBtn = document.querySelector("#logout")

const onLoginSubmit = (e) => {
  e.preventDefault()
  if (!selectedCharacter) {
    alert("Please select your emotion")
    return
  }
  // 로컬스토리지에 저장
  const username = loginInput.value
  localStorage.setItem("username", username)
  localStorage.setItem("character", selectedCharacter)
  
  // 화면 전환
  // 로그인 후 캐릭터 선택 화면은 사라지고 선택한 캐릭터 프로필 화면 띄우기
  main.classList.add("hidden")
  profileContainer.classList.remove("hidden")
  loginForm.classList.add("hidden") // 로그인 폼 숨기기
  charactersContainer.classList.add("hidden") // 캐릭터 선택 화면 숨기기
  paintProfile(username, selectedCharacter)
  todoContainer.classList.remove("hidden") // 로그인 후에 todo container 보이도록 설정
  logoutBtn.classList.remove("hidden")  // 로그아웃 버튼 표시

  // todos 복원
  restoreTodos()
}


// 프로필 화면 구성
const paintProfile = (username, characterProfileImg) => {
  profileImage.src = `characters/${characterProfileImg}` // 선택된 캐릭터 프로필 이미지
  profileUsername.innerText = username
  profileSection.classList.remove("hidden") // 프로필 표시
}


// 로그아웃
const onClickLogout = () => {
  // 사용자 정보 초기화화
  localStorage.removeItem("username")
  localStorage.removeItem("character")

  // 화면 초기화
  main.classList.remove("hidden")  // 메인 화면 다시 보이기
  profileSection.classList.add("hidden") // 프로필 숨기기
  todoContainer.classList.add("hidden")  // 투두리스트 숨기기
  loginForm.classList.remove("hidden")   // 로그인 폼 다시 보여주기
  charactersContainer.classList.remove("hidden")  // 캐릭터 선택창 보여주기
  loginInput.value = ""                  // 입력필드 초기화
  characters.forEach((img) => img.classList.remove("selected"))
  selectedCharacter = null               // 캐릭터 선택 초기화
  logoutBtn.classList.add("hidden")  // 로그아웃 버튼 숨기기
  profileContainer.classList.add("hidden")  // 프로필 컨테이너 숨기기

  todos = []
  todoList.innerHTML = ""
}


// 페이지 로드 시 초기 상태
const savedUsername = localStorage.getItem("username")
const savedCharacter = localStorage.getItem("character")

// 이전에 로그인한 기록이 있다면                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      숨겼던 로그인폼 보여주기
if (savedUsername && savedCharacter) {
  main.classList.add("hidden")
  charactersContainer.classList.add("hidden")
  loginForm.classList.add("hidden")
  
  profileContainer.classList.remove("hidden")  
  profileSection.classList.remove("hidden")
  todoContainer.classList.remove("hidden")

  // 프로필 화면을 다시 그리기
  paintProfile(savedUsername, savedCharacter);
  logoutBtn.classList.remove("hidden")  // 로그아웃 버튼 표시
  restoreTodos()
} else {
  main.classList.remove("hidden")
  // 없다면 로그인 폼, 캐릭터 선택 화면 보이기
  loginForm.classList.remove("hidden")
  charactersContainer.classList.remove("hidden")
  logoutBtn.classList.add("hidden")  // 로그아웃 버튼 숨기기
}

logoutBtn.addEventListener("click", onClickLogout)
loginForm.addEventListener("submit", onLoginSubmit) // submit 이벤트는 enter나 버튼 클릭시 발생