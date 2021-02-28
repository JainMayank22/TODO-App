const dotenv  = require('dotenv');
const nodemailer = require('nodemailer');
dotenv.config();    
var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.email, // your email address to send email from
    pass: process.env.password // your gmail account password
  }
});

module.exports = transporter;