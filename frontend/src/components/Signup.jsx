import React, { useState } from 'react';

const Signup = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!username || !email || !password) {
      setError('All fields are required.');
      return;
    }

    const emailPattern = /\S+@\S+\.\S+/;
    if (!emailPattern.test(email)) {
      setError('Please enter a valid email address.');
      return;
    }

    const passwordPattern = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
    if (!passwordPattern.test(password)) {
      setError(
        'Password must contain at least one number, one uppercase and lowercase letter, and at least 8 characters.'
      );
      return;
    }

    const registeredUsers = JSON.parse(localStorage.getItem('registeredUsers')) || [];
    if (registeredUsers.includes(username)) {
      setError('Username is already taken. Please choose another.');
      return;
    }

    registeredUsers.push(username);
    localStorage.setItem('registeredUsers', JSON.stringify(registeredUsers));

    setError('');
    alert('Signup successful!');
    window.location.href = '/user-login'; 
  };

  return (
    <div style={containerStyle}>
      <div style={cardStyle}>
        <h1 style={titleStyle}>Sign Up</h1>
        <form style={formStyle} onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            style={inputStyle}
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="email"
            placeholder="Email"
            style={inputStyle}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            style={inputStyle}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {error && <p style={errorStyle}>{error}</p>}
          <button style={buttonStyle} type="submit">
            Sign Up
          </button>
        </form>
        <p style={loginTextStyle}>
          Already have an account?{' '}
          <button
            onClick={() => (window.location.href = '/user-login')}
            style={loginButtonStyle}
          >
            Login
          </button>
        </p>
      </div>
    </div>
  );
};

const containerStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh',
  backgroundImage: 'url("/background.webp")',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat',
  backgroundPosition: 'center',
};

const cardStyle = {
  backgroundColor: 'white',
  padding: '30px',
  borderRadius: '10px',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
  width: '400px',
  textAlign: 'center',
};

const titleStyle = {
  color: '#ed930c',
  marginBottom: '20px',
};

const formStyle = {
  display: 'flex',
  flexDirection: 'column',
  gap: '15px',
};

const inputStyle = {
  padding: '10px',
  border: '1px solid #ccc',
  borderRadius: '5px',
};

const buttonStyle = {
  padding: '10px',
  fontSize: '16px',
  borderRadius: '5px',
  backgroundColor: '#ed930c',
  color: '#fff',
  border: 'none',
  cursor: 'pointer',
};

const errorStyle = {
  color: 'red',
  fontSize: '14px',
};

const loginTextStyle = {
  marginTop: '20px',
  fontSize: '14px',
  color: '#555',
};

const loginButtonStyle = {
  color: '#ed930c',
  background: 'none',
  border: 'none',
  cursor: 'pointer',
  textDecoration: 'underline',
};

export default Signup;
