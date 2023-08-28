import redis from 'redis';

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

function displaySchoolValue(schoolName){
    client.get(schoolName, function(err, result){
	if (err) {
	    console.error('Error:', err);
	} else {
	    console.log(result);
	}
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
