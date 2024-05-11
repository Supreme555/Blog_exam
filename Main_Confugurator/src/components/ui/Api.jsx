import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000', 
    timeout: 5000,
    headers: {
      'Content-Type': 'application/json',
    },
  });


async function GetObj(){
  let comp = await instance.get()
  .then(response => {
    return response.data;
  })
  .catch(error => {
    return [];
  });
  return comp;
};

export default GetObj