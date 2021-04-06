require ('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const fileUpload = require('express-fileupload');
const cookieParser = require('cookie-parser');


const app = express();

app.use(express.json());
app.use('cookieParser');
app.use(cors());
app.use(fileUpload({
    useTempFiles:true
}));

//  Routes 
app.use('/user', require('./routes/userRouter'));
app.use('/api', require('./routes/categoryRouter'));
app.use('/api', require('./routes/upload'));

//  Connect to MongoDb
const URI = process.env.MONGODB_URL
mongoose.connect(URI,
{
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
  useFindAndModify: false
}, err =>{
    if(err) throw err;
    console.log('Connected to MongoDB')
});



const PORT =  process.env.PORT || 5000
app.listen(PORT, () => {
    console.log(`Server started on port`, PORT);
});