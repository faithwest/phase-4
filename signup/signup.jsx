// SignUp.js
import React, { useState } from 'react';
import firebase from './firebase'; // Import your firebase configuration

function SignUp() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleEmailSignUp = async (e) => {
    e.preventDefault();
    try {
      await firebase.auth().createUserWithEmailAndPassword(formData.email, formData.password);
      console.log('Signed up successfully!');
    } catch (error) {
      console.error('Error signing up:', error);
    }
  };

  const handleGoogleSignUp = async () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    try {
      await firebase.auth().signInWithPopup(provider);
      console.log('Signed up with Google successfully!');
    } catch (error) {
      console.error('Error signing up with Google:', error);
    }
  };

  return (
    <div className="container">
      <h2>Sign Up</h2>
      <form onSubmit={handleEmailSignUp}>
        <input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} />
        <button type="submit">Sign Up with Email</button>
      </form>
      <button onClick={handleGoogleSignUp}>Sign Up with Google</button>
    </div>
  );
}

export default SignUp;
