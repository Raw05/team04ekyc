import axios from 'axios';

// Base URL for backend API
const BASE_URL = 'http://localhost:5000/api'; // Replace with your backend's URL

// User authentication (login)
export const loginUser = (credentials) =>
  axios.post(`${BASE_URL}/login`, credentials);

// Fetch all users (for Admin role management)
export const getUsers = () =>
  axios.get(`${BASE_URL}/users`);

// Update user role
export const updateUserRole = (userId, roleData) =>
  axios.put(`${BASE_URL}/users/${userId}/role`, roleData);

// Upload document for processing
export const uploadDocument = (formData) =>
  axios.post(`${BASE_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

// Fetch dashboard data (e.g., analytics)
export const getDashboardData = () =>
  axios.get(`${BASE_URL}/dashboard`);