const express = require('express');
const util = require('util');
import { createClient } from 'redis';

const app = express();
const port = 1245;
const redis_port = 6379;

const client = createClient(redis_port);

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(err) {
    console.log(`Redis client not connected to the server ${err}`);
});

client.get = util.promisify(client.get);

const listProducts = [
    {'itemId': 1, 'itemName': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4},
    {'itemId': 2, 'itemName': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10},
    {'itemId': 3, 'itemName': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2},
    {'itemId': 4, 'itemName': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5}
];

function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}



//post the stock
function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

//fetch the stock
async function getCurrentReservedStockById(itemId) {
  const stock = await client.get(itemId);
  return stock;
}


app.get('/list_products', (req, res) => {
  //const all = listProducts.map(product => getItemById(product.Id));
  res.json(listProducts);
});

app.get('/list_products/:itemId',(req, res) => {
    const itemId  = req.params.itemId;
    const val = getItemById(parseInt(itemId));
    if(val) {
        const stock = getCurrentReservedStockById(itemId);
        const newVal = {
            itemId: val.itemId,
            itemName: val.itemName,
            price: val.price,
            initialAvailableQuantity: val.initialAvailableQuantity,
            currentQuantity: val.initialAvailableQuantity,
          };
        res.json(newVal);
    } else {
        res.json({"status": "Product not found"});
    }
});

app.get('/reserve_product/:itemId',  async function (req, res) {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  if(!item) {
    res.json({"status":"Product not found"});
  }
  const stock = await getCurrentReservedStockById(itemId)
  if(stock == null) {
    res.json({"status":"Not enough stock available","itemId":1});
  } else {
    reserveStockById(itemId, stock);
    res.json({"status":"Reservation confirmed","itemId": itemId}
    )
  }
 
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});