import redis from 'redis';
const util = require('util');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, function(err, result){
	if (err) {
	    console.log(err);
	}else{
	    redis.print(`Reply: OK`);
	}
    });
}

const syncClient = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName){
    try {
	const result = await syncClient(schoolName);
	console.log(result);
    } catch (error) {
	console.error('Error:', error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
