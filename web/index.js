const request = new XMLHttpRequest();

request.addEventListener("readystatechange", () => {
    if (request.readyState === 4) {
        console.log(request.responseText)
    }
})

request.send("https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f")