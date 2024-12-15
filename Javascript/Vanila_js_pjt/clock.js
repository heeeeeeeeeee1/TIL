const clock = document.querySelector("#clock")

const getClock = () => {
  const date = new Date()
  const hours = String(date.getHours()).padStart(2, "0")
  const minutes = String(date.getMinutes()).padStart(2, "0")
  const seconds = String(date.getSeconds()).padStart(2, "0")
  clock.innerText = `${hours}:${minutes}:${seconds}`
}

getClock() // 페이지 로드 직후 시간 표시
setInterval(getClock, 1000) // 1초마다 getClock 호출