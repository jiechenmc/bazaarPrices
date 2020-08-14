const getItem = async (item) => {
  const url = "https://api.hypixel.net/skyblock/bazaar";
  const key = "191e62a6-2d3e-49b1-b58e-106f0e16bb1f";
  const query = `${url}?key=${key}`;
  const resposne = await fetch(query);
  const { products } = await resposne.json();
  const quickStatus = products[item].quick_status;
  return quickStatus;
};
