const now = new Date()
const year = now.getFullYear()
const month = now.getMonth()
const date = now.getDate()
const today = document.querySelector("#today")
today.innerText = `${year}년 ${month+1}월 ${date}일`


const clock = document.querySelector("#clock")
const getClock = () => {
  const now = new Date()
  const hours = String(now.getHours()).padStart(2, "0")
  const minutes = String(now.getMinutes()).padStart(2, "0")
  const seconds = String(now.getSeconds()).padStart(2, "0")
  clock.innerText = `${hours}:${minutes}:${seconds}`
}

getClock() // 페이지 로드 직후 시간 표시
setInterval(getClock, 1000) // 1초마다 getClock 호출