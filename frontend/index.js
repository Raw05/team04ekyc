import React from 'react';
import ReactDOM from 'react-dom/client'; // Correct import for React 18
import './styles/global.css'; // Ensure this file exists for your global styles
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root')); // Updated for React 18
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
