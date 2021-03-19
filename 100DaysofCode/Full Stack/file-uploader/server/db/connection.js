const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/file-uploader', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});