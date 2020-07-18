const request = new XMLHttpRequest();
const paragraph = document.querySelector("p");

function getRequest(cb) {
  request.addEventListener("readystatechange", () => {
    if ((request.readyState === 4) & (request.status === 200)) {
      const data = JSON.parse(request.responseText);
      cb(undefined, data);
    } else if (request.readyState === 4) {
      console.log("ERROR!", undefined);
    }
  });

  request.open(
    "GET",
    "https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f"
  );

  request.send();
}

getRequest((err, data) => {
  if (!err) {
    console.log(data);
  }
});

// Promise Example

function getSomething() {
  return new Promise((resolve, reject) => {
    //fetch
    resolve("Some Data");
    //reject("ERROR!");
  });
}
