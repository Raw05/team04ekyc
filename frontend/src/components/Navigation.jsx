import React from "react";
import { Link } from "react-router-dom";

const Navigation = () => {
  return (
    <nav style={navStyle}>
      <div>
        <img
          src="/bgimg.jpg"
          alt="Logo"
          style={{ height: "40px", cursor: "pointer" }}
        />
      </div>
      <ul style={ulStyle}>
        <li>
          <Link to="/" style={{ ...linkStyle, ...buttonStyle }}>
            Home
          </Link>
        </li>
        <li>
          <Link to="/user-login" style={{ ...linkStyle, ...buttonStyle }}>
            GetStarted
          </Link>
        </li>
        <li>
          <Link to="/upload-documents" style={{ ...linkStyle, ...buttonStyle }}>
            Upload
          </Link>
        </li>
      </ul>
    </nav>
  );
};

const navStyle = {
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  padding: "10px 20px",
  backgroundColor: "#007bff",
  color: "white",
};

const ulStyle = {
  listStyle: "none",
  display: "flex",
  gap: "15px",
  margin: 0,
  padding: 0,
};

const linkStyle = {
  color: "white",
  textDecoration: "none",
  fontSize: "16px",
};

const buttonStyle = {
  backgroundColor: "orange",
  padding: "10px 20px",
  borderRadius: "5px",
  textAlign: "center",
  transition: "background-color 0.3s",
  border: "none",
  cursor: "pointer",
};

export default Navigation;
