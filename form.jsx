// body {
// 	background-color: #f5f7fa; /* Soft background color */
// 	font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
// 	display: flex;
// 	justify-content: center;
// 	align-items: center;
// 	height: 100vh;
// 	margin: 0;
//   }
  
//   h2 {
// 	text-align: center;
// 	color: #333;
// 	font-size: 24px;
// 	margin-bottom: 20px;
//   }
  
//   form {
// 	background-color: white;
// 	border-radius: 10px;
// 	padding: 30px;
// 	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
// 	width: 100%;
// 	max-width: 400px;
// 	text-align: center;
//   }
  
//   label {
// 	font-size: 16px;
// 	color: #333;
// 	display: block;
// 	margin-bottom: 8px;
// 	text-align: left;
//   }
  
//   input, select {
// 	width: 100%;
// 	padding: 10px;
// 	border: 1px solid #ccc;
// 	border-radius: 5px;
// 	font-size: 14px;
// 	margin-bottom: 20px;
// 	box-sizing: border-box;
//   }
  
//   input[type="radio"] {
// 	width: auto;
//   }
  
//   span {
// 	color: red;
// 	font-size: 12px;
// 	display: block;
// 	text-align: left;
//   }
  
//   button {
// 	background-color: #4CAF50;
// 	color: white;
// 	padding: 10px 20px;
// 	border: none;
// 	border-radius: 5px;
// 	cursor: pointer;
// 	font-size: 16px;
// 	transition: background-color 0.3s ease;
//   }
  
//   button:hover {
// 	background-color: #45a049;
//   }
  
//   input:focus, select:focus {
// 	outline: none;
// 	border-color: #4CAF50;
// 	box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
//   }
  
// CSSSS
import React, { useState } from 'react';
import './RegistrationForm.css'; // Assuming the CSS is in this file

function RegistrationForm() {
  const [formData, setFormData] = useState({
    name: '',
    dob: '',
    gender: '',
    school: '',
    classLevel: '',
    contact: '',
  });

  const [errors, setErrors] = useState({});

  const validate = () => {
    let formErrors = {};

    if (!formData.name.trim()) formErrors.name = 'Full name is required';
    if (!formData.dob) formErrors.dob = 'Date of birth is required';
    if (!formData.gender) formErrors.gender = 'Gender is required';
    if (!formData.school) formErrors.school = 'School selection is required';
    if (!formData.classLevel) formErrors.classLevel = 'Class level is required';
    if (!formData.contact) {
      formErrors.contact = 'Contact number is required';
    } else if (!/^\d{10}$/.test(formData.contact)) {
      formErrors.contact = 'Contact must be a valid 10-digit number';
    }

    setErrors(formErrors);
    return Object.keys(formErrors).length === 0;
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      console.log('Form submitted successfully:', formData);
      // You can send the form data to an API here.
    }
  };

  return (
    <div>
      <h2>High School Registration Form</h2>
      <form onSubmit={handleSubmit}>
        {/* Full Name */}
        <label htmlFor="name">Full Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        {errors.name && <span>{errors.name}</span>}
        
        {/* Date of Birth */}
        <label htmlFor="dob">Date of Birth:</label>
        <input
          type="date"
          id="dob"
          name="dob"
          value={formData.dob}
          onChange={handleChange}
          required
        />
        {errors.dob && <span>{errors.dob}</span>}

        {/* Gender */}
        <label>Gender:</label>
        <input
          type="radio"
          id="male"
          name="gender"
          value="male"
          onChange={handleChange}
          required
        />
        <label htmlFor="male">Male</label>
        <input
          type="radio"
          id="female"
          name="gender"
          value="female"
          onChange={handleChange}
          required
        />
        <label htmlFor="female">Female</label>
        {errors.gender && <span>{errors.gender}</span>}

        {/* School Dropdown */}
        <label htmlFor="school">Select School:</label>
        <select
          id="school"
          name="school"
          value={formData.school}
          onChange={handleChange}
          required
        >
          <option value="" disabled>Select a school</option>
          <option value="alliance_high_school">Alliance High School</option>
          <option value="kenya_high_school">Kenya High School</option>
          <option value="mang'u_high_school">Mang'u High School</option>
          <option value="starehe_boys_center">Starehe Boys' Center</option>
          <option value="precious_blood">Precious Blood Riruta</option>
          <option value="lenana_school">Lenana School</option>
        </select>
        {errors.school && <span>{errors.school}</span>}

        {/* Class Dropdown */}
        <label htmlFor="classLevel">Select Class:</label>
        <select
          id="classLevel"
          name="classLevel"
          value={formData.classLevel}
          onChange={handleChange}
          required
        >
          <option value="" disabled>Select a class</option>
          <option value="form_1">Form 1</option>
          <option value="form_2">Form 2</option>
          <option value="form_3">Form 3</option>
          <option value="form_4">Form 4</option>
        </select>
        {errors.classLevel && <span>{errors.classLevel}</span>}

        {/* Parent/Guardian Contact */}
        <label htmlFor="contact">Parent/Guardian Contact Number:</label>
        <input
          type="tel"
          id="contact"
          name="contact"
          value={formData.contact}
          onChange={handleChange}
          required
        />
        {errors.contact && <span>{errors.contact}</span>}

        {/* Submit Button */}
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default RegistrationForm;



