import redis from 'redis'
import { promisify }

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client)

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message)
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print());
};

const displaySchoolValue = async(schoolName) => {
  try{
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
