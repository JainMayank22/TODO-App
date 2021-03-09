
//  telling webpack where the entry point is to put the generated output file bundle.js inside the public directory.
const path = require('path');
module.exports = {
    entry: './src/app.js',
    output: {
        filename: 'bundle.js',
        path: path.join(__dirname, 'public')
    },
    // telling babel-loader to look for only .js files to convert to ES5 code but exclude them from node_modules directory.
    module: {
        rules: [{
         loader: 'babel-loader',
         test: /\.js$/,
         exclude: /node_modules/
        }]
       },
    //  to speed up build process default production mode changed to development mode   
    mode: 'development',
    // this informs webpack-dev-server to load file from public directory
    devServer: {
    contentBase: path.join(__dirname, 'public')
   }
};
