import React from "react";

const Home = () => {
  return (
    <div style={homeStyle}>
      <h1 style={titleStyle}>Welcome to the KYC Portal</h1>
      <p style={textStyle}>Streamline your document management with ease.</p>
    </div>
  );
};

const homeStyle = {
  backgroundImage: 'url("https://via.placeholder.com/1920x1080")', // Replace with your background image URL
  backgroundSize: "cover",
  backgroundPosition: "center",
  textAlign: "center",
  marginTop: "50px",
  padding: "20px",
};

const titleStyle = {
  color: "#007bff",
};

const textStyle = {
  color: "#555",
};

export default Home;
