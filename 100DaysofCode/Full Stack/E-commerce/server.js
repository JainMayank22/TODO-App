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
//  Connect to MongoDb

const URI = proccess.env.MONGODB_URL
mongoose.connect(URI
, {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
  useFindAndModify: true
},err =>{
    if(err) throw err;
    console.log('Connnected to MongoDB')
});

app.get('/', (req, res) => {
res.json({msg:"Welcome"})	
});
const PORT =  process.env.PORT || 5000
app.listen(PORT, () => {
    console.log(`Server started on port`, PORT);
});