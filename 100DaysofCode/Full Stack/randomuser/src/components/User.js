// import React from 'react';
// const User = ({ name, location, email, picture }) => {
//  return (
//   <div className="random-user">
//    <div className="user-image">
//     <img src={picture.medium} alt={name.first} />
//    </div>
//    <div><strong>Name:</strong> {name.first} {name.last}</div>
//    <div><strong>Country:</strong> {location.country}</div>
//    <div><strong>Email:</strong> {email}</div>
//   </div>
//  );
// };
// export default User;


import React from 'react';
const User = ({ name, location, phone, picture }) => {
 return (
  <div className="card">
    <img className = "card--image" src={picture.medium} alt={name.first} />
   <div className='card--name'><strong>Name:</strong> {name.first} {name.last}</div>
   <div className='card--details'><strong>Country:</strong> {location.country}</div>
   <div className='card--name'><strong>Phone:</strong> {phone}</div>
  </div>
 );
};
export default User;