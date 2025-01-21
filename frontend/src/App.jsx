import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import UserLogin from "./components/UserLogin";
import Signup from "./components/Signup";
import FileUpload from "./components/FileUpload";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/user-login" element={<UserLogin />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/upload-documents" element={<FileUpload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
