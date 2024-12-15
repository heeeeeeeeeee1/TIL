const todoForm = document.getElementById("todo-form")
const todoInput = todoForm.querySelector("input")
const todoList = document.getElementById("todo-list")

// todos 저장하기 위한 배열
let todos = []

// 저장 시 username 기반으로 todos 저장
const saveTodos = () => {
  const username = localStorage.getItem("username")
  // localStorage는 array 저장 불가. 문자만 저장 가능
  if (username) {
    localStorage.setItem(`${username}_todos`, JSON.stringify(todos)) // array 모양으로 저장
  }
}


const addTodo = (newTodo) => {
  // if (todos.some((todo) => todo.id === newTodo.id)) return; // 이미 존재하는 todo 항목은 추가하지 않음
  
  const liTag = document.createElement("li")
  liTag.id = newTodo.id
  const spanTag = document.createElement("span")
  spanTag.innerText = newTodo.text
  const deleteBtn = document.createElement("button")
  deleteBtn.innerText = "x" // 회색 구술(원) 모양
  // todo를 수행했다면 노란구술(원) 체크 -> 이거 어떻게 해
  deleteBtn.addEventListener("click", deleteTodo)

  liTag.appendChild(spanTag)
  liTag.appendChild(deleteBtn)
  todoList.appendChild(liTag)
}

const deleteTodo = (e) => {
  // 어떤 li의 삭제 버튼인지 찾기
  const deleteLiTag = e.target.parentElement
  todos = todos.filter(todo => todo.id !== parseInt(deleteLiTag.id))  // todo 삭제를 위해 클릭한 li.id와 다른 todo는 남기기. li.id는 string
  deleteLiTag.remove()
  saveTodos()
}

// 페이지 로드 시 todos 복원
const restoreTodos = () => {
  const username = localStorage.getItem("username")
  if (username) {
    const savedTodos = localStorage.getItem(`${username}_todos`)
    if (savedTodos) {
      const parsedTodos = JSON.parse(savedTodos)
      todos = parsedTodos // 기존 todos 배열 대체
      todoList.innerHTML = ''
      parsedTodos.forEach(addTodo)
    } else {
      todos = []  // 저장된 데이터가 없으면 todos 배열 초기화화
    }
  } else {
    todos = [] // 사용자 정보가 없으면 todos 배열 초기화
  }
}


const handleTodoSubmit = (e) => {
  e.preventDefault()
  // enter 누르면 입력창 비우기
  const newTodo = todoInput.value
  todoInput.value = ""
  const newTodoObj = {
    text: newTodo,
    id: Date.now(), // li item 구별을 위한 id
  }
  todos.push(newTodoObj) // array에 저장
  addTodo(newTodoObj) // 화면에 추가
  saveTodos() // 저장
}

todoForm.addEventListener("submit", handleTodoSubmit)

restoreTodos()  // 페이지 로드 시 todos 복원

// restoreTodos 사용하면서 불필요해짐짐
// localstorage에 저장된 배열(todos) 꺼내오기
// const savedTodos = localStorage.getItem("todos")
// if (savedTodos !== null) {
//   const parsedTodos = JSON.parse(savedTodos)
//   todos = parsedTodos // 이전에 저장된 todos 복원
//   parsedTodos.forEach(addTodo)
// }
