import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render() {
        return (
            <div class = "scene"><div id="container"> <div class="card"> <img src="https://github.com/JainMayankA.png?size=280" alt="Mayank Ambalal Jain"></img>

            <div class="card__details">

                <span class="tag">Full Stack Web Developer</span>

                <span class="tag">Computer Vision Engineer</span>

                <div class="name">Mayank Ambalal Jain</div>

                <p>My enthusiasm lies in solving problems with appropriate solutions. Always been a persistent learner, I am enhancing my skills to develop more useful full-stack web applications and computer vision projects.</p>
                <a href="https://github.com/JainMayankA"><button>Read more</button></a></div>
            <div class = "card__face card__face--back"></div> 
        </div> 
        </div>
        </div>
            

        
        
    
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));