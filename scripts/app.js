const itemForm = document.querySelector("form");
const buyPriceDOM = document.querySelector(".buyPrice");
const sellPriceDOM = document.querySelector(".sellPrice");
const itemNameDOM = document.querySelector(".itemName");
const imageDOM = document.querySelector(".itemImage");

itemForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const item = itemForm.item.value.trim().toUpperCase();
  itemForm.reset();
  getItem(item).then((data) => {
    itemName = data.productId;
    buyPrice = Math.round(data.buyPrice);
    sellPrice = Math.round(data.sellPrice);
    //
    itemNameDOM.textContent = itemName;
    buyPriceDOM.textContent = `BP:${buyPrice}`;
    sellPriceDOM.textContent = `SP:${sellPrice}`;
    imageDOM.src = `assets/${itemName}.PNG`;
  });
});
