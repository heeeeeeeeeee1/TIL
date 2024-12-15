const images = ["headquarters1.jpg", "headquarters2.jpg", "headquarters3.jpg"]

const chosenImage = images[Math.floor(Math.random() * images.length)]

const bgImage = document.createElement("img")
bgImage.src = `background/${chosenImage}`
bgImage.id = "background-image"

document.body.appendChild(bgImage)