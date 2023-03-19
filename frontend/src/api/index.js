import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:3000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchFirstPart = async () => {
  const response = await api.get('/story/first');
  return response.data;
};

export const fetchNextPart = async (choice) => {
  const response = await api.post('/story/next', { choice });
  return response.data;
};
