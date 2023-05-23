import { createClient, print } from 'redis';
const util = require('util')

const client = createClient();
client.get = util.promisify(client.get);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => console.log(
    `Redis client not connected to the server:${err}`));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
    
}

async function displaySchoolValue(schoolName) {
    const feed = await client.get(schoolName).catch((err) => {
        if(err) {
            console.log(err);
            throw err;
        }
    });
    console.log(feed);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');