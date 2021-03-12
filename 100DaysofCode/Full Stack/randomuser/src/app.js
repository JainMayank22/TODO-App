import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class App extends React.Component {
    componentDidMount() {
        axios.get('http://localhost:3000/users')
         .then(response => {
           console.log(response.data);
         })
       }
    render() {
        return (
            <h1>Welcome to REACT!</h1>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));