const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const https = require("https");
const app = express();

app.use(express.static("public"));

app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req,res){
  res.sendFile(__dirname + "/signup.html");
});

app.post("/",function(req,res){
  var name = req.body.name;
  var email = req.body.email;
  var data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields:{
          FNAME: name
        }
      }
    ]

  };
  var jsonData = JSON.stringify(data);
  var url = "https://usX.api.mailchimp.com/3.0/lists/---------";
  var options = {
    method: "POST",
    auth: "--------"


  }
  const request = https.request(url,options, function(response){
    request.on("data", function(data){
      console.log(JSON.parse(data));
    })

  })
  request.write(jsonData);
  request.end();

  // console.log(name,email);

});

app.listen(3000,function(){
  console.log("Server is running");
});

//api key
//-----------------

// unique id
//---------------
