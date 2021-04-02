const Users = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');


const userController = {
    // Register
    register: async (req, res) => {
        try {
            const {name, email, password} = req.body;
            const user = await Users.findOne({email})
            //  Validation of email uniqueness and password length
            if(user) {
                return res.status(400).json({msg: "The email already exists."})
            }
            if(password.length < 6){
                return res.status(400).json({msg:"The password should be atleast 6 characters long."})
            }
            // Password  Encryption
            const passwordHash = await bcrypt.hash(password, 10)
            //  Assign to the specific user after encryption
            const newUser = new Users({
                name, email, password: passwordHash
            }) 

            //  Save mongodb 
            await newUser.save()
            
            // Then create jsonwebtoken to authentication 
            const accessToken = createAccessToken({id: newUser._id});
            const refreshToken = createRefreshToken({id: newUser._id});


            // Cookie comments
            res.cookie('refreshToken', refreshToken,{
                httpOnly: true,
                path: '/user/refresh_token'
            })

            res.json({accessToken})


        } catch (err) {
            return res.status(500).json({msg: err.message})
        }

    },
    //  Login Functionality 
    login: async(req, res) => {
        try {
            const {email, password} = req.body;

            const user = await Users.findOne({email})
            if (!user) return res.status(400).json({msg: "user does not exists."})

            const isMatch = await bcrypt.compare(password, user.password)

            if(!isMatch) return res.status(400).json({msg: "Incorrect Password"})

            //  If login successful, create access token and refresh token

            const accessToken = createAccessToken({id: user._id});
            const refreshToken = createRefreshToken({id: user._id});


            // Cookie comments
            res.cookie('refreshToken', refreshToken,{
                httpOnly: true,
                path: '/user/refresh_token'
            })

            res.json({accessToken})


        } catch (err) {
            return res.status(500).json({msg: err.message})

        }
    },
    //  Logout Functionality
    logout: async (req, res) => {
        try {
            res.clearCookie('refreshToken', {path: '/user/refresh_token' })
            return res.json({msg: "Logged Out"})

        } catch (err) {
            return res.status(500).json({msg: err.message})
        }

    },
    //  RefreshToken
    refreshToken: (req, res) => {
        try {
            const rf_token = req.cookies.refreshToken;
            if(!rf_token) return res.status(400).json({msg:"Please Login or Register"})
            jwt.verify(rf_token, process.env.REFRESH_TOKEN_SECRET, (err, user) => {
            if(err) return res.status(400).json({msg:"Please Login or Register"})
            
            const accessToken = createAccessToken({id:user.id})
            res.json({accessToken})
        })
            
        } catch (err) {
            return res.status(500).json({msg: err.message})
        }

    },
    //  Get user info
    getUser: async (req, res) => {
        try {
            const user = await Users.findById(req.user.id).select('-password')
            if(!user) return res.status(500).json({msg: "User does not exist"})

            res.json(user)
        } catch (err) {
            return res.status(500).json({msg: err.message})
            
        }
    }

};
// CreateAToken
const createAccessToken = (user)  => {
    return jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, {expiresIn: '1d'})
}
//  CreateRToken
const createRefreshToken = (user)  => {
    return jwt.sign(user, process.env.REFRESH_TOKEN_SECRET, {expiresIn: '7d'})
}

module.exports = userController;