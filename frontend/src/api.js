// Axios configuration

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Connect to Backend
});

export default api;
