const request = new XMLHttpRequest();
const paragraph = document.querySelector("p");

request.addEventListener("readystatechange", () => {
  if (request.readyState === 4) {
    console.log(request.responseText);
    paragraph.innerText = request.responseText;
  }
});

request.open(
  "GET",
  "https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f"
);

request.send();
