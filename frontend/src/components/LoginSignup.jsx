import React from 'react';
import { useNavigate } from 'react-router-dom';

const LoginSignup = () => {
  const navigate = useNavigate();

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1 style={{ color: '#007bff' }}>Login or Signup</h1>
      <div style={{ marginTop: '20px' }}>
        <button style={{ margin: '10px', padding: '10px 20px' }} onClick={() => navigate('/login-page')}>Admin</button>
        <button style={{ margin: '10px', padding: '10px 20px' }} onClick={() => navigate('/signup')}>User</button>
      </div>
    </div>
  );
};

export default LoginSignup;
// import React from 'react';
// import { useNavigate } from 'react-router-dom';

// const LoginSignup = () => {
//   const navigate = useNavigate();

//   return (
//     <div style={{ textAlign: 'center', marginTop: '50px' }}>
//       <h1 style={{ color: '#007bff' }}>Login</h1>
//       <div style={{ marginTop: '20px' }}>
//         <button
//           style={{
//             margin: '10px',
//             padding: '10px 20px',
//             backgroundColor: '#007bff',
//             color: '#fff',
//             border: 'none',
//             borderRadius: '5px',
//             cursor: 'pointer',
//             fontSize: '16px',
//           }}
//           onClick={() => navigate('/admin-login')}
//         >
//           Admin Login
//         </button>
//         <button
//           style={{
//             margin: '10px',
//             padding: '10px 20px',
//             backgroundColor: '#28a745',
//             color: '#fff',
//             border: 'none',
//             borderRadius: '5px',
//             cursor: 'pointer',
//             fontSize: '16px',
//           }}
//           onClick={() => navigate('/user-login')}
//         >
//           User Login
//         </button>
//       </div>
//     </div>
//   );
// };

// export default LoginSignup;
