// SignUp.js
import React, { useState } from 'react';
import firebase from './firebase'; // Import your firebase configuration

function SignUp() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    age: '',
    bio: ''
  });
  const [profilePicture, setProfilePicture] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleFileChange = (e) => {
    setProfilePicture(e.target.files[0]);
  };

  const handleEmailSignUp = async (e) => {
    e.preventDefault();
    try {
      const userCredential = await firebase.auth().createUserWithEmailAndPassword(formData.email, formData.password);
      const user = userCredential.user;

      let profilePictureUrl = '';
      if (profilePicture) {
        const storageRef = firebase.storage().ref();
        const fileRef = storageRef.child(`profilePictures/${user.uid}`);
        const uploadTask = fileRef.put(profilePicture);

        uploadTask.on('state_changed', 
          (snapshot) => {
            const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            setUploadProgress(progress);
          },
          (error) => {
            console.error('Error uploading file:', error);
          },
          async () => {
            profilePictureUrl = await uploadTask.snapshot.ref.getDownloadURL();
            console.log('File available at', profilePictureUrl);

            // Update the user's profile with additional information
            await user.updateProfile({
              displayName: formData.username,
              photoURL: profilePictureUrl
            });

            // Optionally, you can store additional user data in Firestore
            await firebase.firestore().collection('users').doc(user.uid).set({
              username: formData.username,
              email: formData.email,
              age: formData.age,
              bio: formData.bio,
              profilePictureUrl
            });

            console.log('Signed up successfully and profile updated!');
          }
        );
      } else {
        // Update the user's profile without a profile picture
        await user.updateProfile({
          displayName: formData.username
        });

        await firebase.firestore().collection('users').doc(user.uid).set({
          username: formData.username,
          email: formData.email,
          age: formData.age,
          bio: formData.bio
        });

        console.log('Signed up successfully without a profile picture!');
      }
    } catch (error) {
      console.error('Error signing up:', error);
    }
  };

  const handleGoogleSignUp = async () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    try {
      const result = await firebase.auth().signInWithPopup(provider);
      const user = result.user;

      // Optionally, you can store additional user data in Firestore
      await firebase.firestore().collection('users').doc(user.uid).set({
        username: user.displayName,
        email: user.email,
        profilePictureUrl: user.photoURL
      });

      console.log('Signed up with Google successfully!');
    } catch (error) {
      console.error('Error signing up with Google:', error);
    }
  };

  return (
    <div className="container">
      <h2>Sign Up</h2>
      <form onSubmit={handleEmailSignUp}>
        <input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
        <input type="number" name="age" placeholder="Age" value={formData.age} onChange={handleChange} required />
        <textarea name="bio" placeholder="Bio" value={formData.bio} onChange={handleChange} required></textarea>
        <input type="file" onChange={handleFileChange} />
        {uploadProgress > 0 && <p>Upload progress: {uploadProgress}%</p>}
        <button type="submit">Sign Up with Email</button>
      </form>
      <button onClick={handleGoogleSignUp}>Sign Up with Google</button>
    </div>
  );
}

export default SignUp;
