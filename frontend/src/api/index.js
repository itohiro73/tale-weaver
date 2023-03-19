import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:3000',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchFirstPart = async () => {
  try {
    const response = await apiClient.get('/api/story/first-part');
    return response.data;
  } catch (error) {
    console.error('Error fetching the first part of the story:', error);
    return null;
  }
};

export default apiClient;
