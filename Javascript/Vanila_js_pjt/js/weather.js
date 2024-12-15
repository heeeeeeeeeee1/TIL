const API_KEY = '0ea063a13d109d45bee8e2250be08090'

const onGeoCorrect = (position) => {
  const lat = position.coords.latitude    // 위도
  const lon =  position.coords.longitude  // 경도
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
  fetch(url)
    .then(response => response.json())
    .then(data =>{
      const city = document.querySelector("#location")
      const weather = document.querySelector("#weather")
      city.innerText= data.name
      weather.innerText = data.weather[0].main
  })
}

const onGeoError = () => {
  alert("Can't find you. No weather for you")
}

navigator.geolocation.getCurrentPosition(onGeoCorrect, onGeoError)

