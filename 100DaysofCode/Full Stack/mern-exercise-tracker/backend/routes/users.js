const router = require('express').Router();
let User = require('../models/user.model');

//Handles Incoming HTTP GET Requests on /users/URL path
// We call User.find() to get list of user in database

router.route('/').get((req, res) => {
  User.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Error: ' + err));
});

//Handles Incoming HTTP POST Requests on /users/add/URL path
// For adding new user in database

router.route('/add').post((req, res) => {
  const username = req.body.username;

  const newUser = new User({username});

  newUser.save()
    .then(() => res.json('User added!'))
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;