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

export const fetchNextPart = async ({ choice, prev_title, prev_content, choice_count }) => { // choice_countを追加
  try {
    const response = await api.post("/story/next", { choice, prev_title, prev_content, choice_count }); // choice_countをリクエストに含める
    return response.data;
  } catch (error) {
    console.error("Error fetching next part:", error);
    return null;
  }
};
