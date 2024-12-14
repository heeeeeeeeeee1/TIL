const todoForm = document.getElementById("todo-form")
const todoInput = todoForm.querySelector("input")
const todoList = document.getElementById("todo-list")

const TODOS_KEY ="todos"
// todos 저장하기 위한 배열
let todos = []

const saveTodos = () => {
  // localStorage는 array 저장 불가. 문자만 저장 가능
  localStorage.setItem("todos", JSON.stringify(todos)) // array 모양으로 저장
}

const deleteTodo = (e) => {
  // 어떤 li의 삭제 버튼인지 찾기기
  const deleteLiTag = e.target.parentElement
  deleteLiTag.remove()
}

const addTodo = (newTodo) => {
  const liTag = document.createElement("li")
  const spanTag = document.createElement("span")
  spanTag.innerText = newTodo.text
  const deleteBtn = document.createElement("button")
  deleteBtn.innerText = "x"
  deleteBtn.addEventListener("click", deleteTodo)

  liTag.appendChild(spanTag)
  liTag.appendChild(deleteBtn)
  todoList.appendChild(liTag)
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
  addTodo(newTodoObj)
  saveTodos()
}

todoForm.addEventListener("submit", handleTodoSubmit)

// localstorage에 저장된 배열(todos) 꺼내오기
const savedTodos = localStorage.getIem(TODOS_KEY)
if (savedTodos !== null) {
  const parsedTodos = JSON.parse(savedTodos)
  todos = parsedTodos // 이전에 저장된 todos 복원
  parsedTodos.forEach(addTodo)
}