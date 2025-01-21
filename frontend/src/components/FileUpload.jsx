import React, { useState } from "react";
import axios from "axios";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  // Handle file input change
  const handleFileChange = (event) => {
    setFile(event.target.files[0]); // Get the first selected file
  };

  // Handle file upload
  const handleFileUpload = async (event) => {
    event.preventDefault();
    if (!file) {
      setMessage("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file); // 'file' should match the FastAPI endpoint key

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_API_ENDPOINT}/extract/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setMessage("File uploaded successfully!");
    } catch (error) {
      console.error(error);
      setMessage("File upload failed.");
    }
  };

  // Styles for the page
  const styles = {
    container: {
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      flexDirection: "column", // Stack content vertically
      height: "100vh",
      backgroundImage: 'url("https://via.placeholder.com/1920x1080")', // Replace with your background image URL
      backgroundSize: "cover",
      backgroundPosition: "center",
      color: "black",
      textAlign: "center",
    },
    heading: {
      fontSize: "32px",
      fontWeight: "bold",
      marginBottom: "10px",
    },
    subheading: {
      fontSize: "18px",
      marginBottom: "30px",
    },
    formCard: {
      backgroundColor: "rgba(255, 255, 255, 0.9)", // Slightly transparent white background
      padding: "20px",
      borderRadius: "10px",
      boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)",
      width: "300px",
    },
    input: {
      marginBottom: "10px",
      padding: "10px",
      borderRadius: "5px",
      border: "1px solid #ccc",
      fontSize: "14px",
      width: "100%",
    },
    button: {
      backgroundColor: "#007bff",
      color: "white",
      padding: "10px",
      border: "none",
      borderRadius: "5px",
      cursor: "pointer",
      fontSize: "16px",
      width: "100%",
    },
    message: {
      marginTop: "15px",
      fontSize: "14px",
      color: "black",
    },
  };

  return (
    <div style={styles.container}>
      {/* Page Title and Description */}
      <h1 style={styles.heading}>Welcome to the File Upload Page</h1>
      <p style={styles.subheading}>
        Upload your documents securely. Our system ensures your files are
        processed safely.
      </p>

      {/* Upload Form */}
      <div style={styles.formCard}>
        <form onSubmit={handleFileUpload}>
          <input type="file" onChange={handleFileChange} style={styles.input} />
          <button type="submit" style={styles.button}>
            Upload
          </button>
        </form>
        {message && <p style={styles.message}>{message}</p>}
      </div>

      {/* Additional Information */}
      <p style={{ marginTop: "20px", fontSize: "14px" }}>
        Note: Supported formats include PDF, DOCX, and PNG. File size should not
        exceed 5MB.
      </p>
    </div>
  );
};

export default FileUpload;
