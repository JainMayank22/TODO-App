const express = require('express');
// const cors = require('cors');
const path = require('path');
const photosRouter = require('./routers/photos');
require('./db/connection');

const app = express();
const PORT = process.env.PORT||3300;
 
// app.use(cors());
app.use(express.static(path.join(__dirname, '..', 'build')));
app.use(photosRouter);
// add middleware
app.use((req, res, next) => {
    res.sendFile(path.join(__dirname, '..', 'build', 'index.html'));
   });

app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});