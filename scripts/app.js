const itemForm = document.querySelector("form");
const buyPriceDOM = document.querySelector(".buyPrice");
const sellPriceDOM = document.querySelector(".sellPrice");
const itemNameDOM = document.querySelector(".itemName");
const imageDOM = document.querySelector(".itemImage");

itemForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const item = itemForm.item.value.trim().toUpperCase();
  itemForm.reset();
  getItem(item)
    .then((data) => {
      itemName = data.productId;
      buyPrice = Math.round(data.buyPrice);
      sellPrice = Math.round(data.sellPrice);

      itemNameDOM.textContent = itemName;
      buyPriceDOM.textContent = `BP:${buyPrice}`;
      sellPriceDOM.textContent = `SP:${sellPrice}`;
      // Github Pages
      imageDOM.src = `/bazaarPrices/assets/${itemName}.PNG`;
      // Local
      //imageDOM.src = `assets/${itemName}.PNG`;
      imageDOM.alt = "Not Available";
    })
    .catch((err) => {
      itemNameDOM.textContent = "INVALID ITEM";
      buyPriceDOM.textContent = "Check Repository for";
      sellPriceDOM.textContent = "Available Items";
      imageDOM.src =
        "https://upload.wikimedia.org/wikipedia/en/9/93/HypixelLogo.png";
    });
});
