import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  render(){
    return (
    <div className="App">
    <div>
        {/* ******HEADER****** */}
        <header className="header">
          <div className="container clearfix">
            <img className="profile-image img-fluid float-left rounded-circle" src="./images/me.svg" alt="profile image" />
            <div className="profile-content float-left">
              <h1 className="name">Mayank Ambalal Jain</h1>
              <h2 className="desc">
                <a className="typewrite" data-period={2000} data-type="[ &quot;Hello,&quot;, &quot;I am a Graduate Student.&quot;, &quot;I Love to Develop.&quot;, &quot;I am a Full-Stack and Computer Vision Developer.&quot; ]">
                  <span className="wrap" />
                </a></h2>
              <ul className="social list-inline">
                <li className="list-inline-item"><a href="https://www.hackerrank.com/Mayank_A_Jain"><i className="fab fa-hackerrank" /></a></li>
                <li className="list-inline-item"><a href="https://www.linkedin.com/in/mayank-jain-maj1066"><i className="fab fa-linkedin-in" /></a></li>
                <li className="list-inline-item"><a href="https://github.com/JainMayankA"><i className="fab fa-github-alt" /></a></li>
                <li className="list-inline-item"><a href="mailto:maxjain71@gmail.com"><i className="fa fa-envelope" /></a></li>            
              </ul>
            </div>
            {/*//profile*/}
          </div>
          {/*//container*/}
        </header>
        {/*//header*/}
        <div className="container sections-wrapper">
          <div className="row">
            <div className="primary col-lg-8 col-12">
              <section className="about section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">About Me</h2>
                  <div className="content">
                    <p>My enthusiasm lies in solving problems with appropriate solutions. Always been a
                      persistent learner, I am enhancing my skills to develop more useful web
                      applications/projects. I hold strong technical skills and an academic background in
                      Full-Stack development (MERN and Django), Software Engineering methodologies, and
                      Machine Learning services. Additionally, I have a summer fellowship experience in the
                      field of computer vision.
                      An aspiring full stack developer or computer vision engineer . Currently, I am
                      developing MERN stack projects for sharpening comprehensive full-stack skills. Lately, I
                      completed a "Computer Vision Nanodegree" under Udacity Nanodegree Program. I am always
                      open to collaborating on projects and innovative/disruptive ideas .</p>
                  </div>
                </div>
              </section>
              <section className="latest section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Latest Projects</h2>
                  <div className="content">
                    <div className="item featured text-center">
                      <div className="featured-image has-ribbon">
                        <a href="#" target="_blank">
                          <img className="img-fluid project-image rounded shadow-sm" src="./images/qaz.jpg" alt="project name" />
                        </a>
                      </div>
                      <h3 className="title mb-3"><a href="https://github.com/JainMayankA/SE1_Project" target="_blank">Campus Car Rental Android Application</a></h3>
                      <div className="desc text-left">
                        <p>A group project of 6 people implemented an android native application car rental
                          for errands or pleasure for university people.
                          My contribution to the project was achieving the search car, profile check, and
                          check the reservation calendar function and designed UX/UI for the rental
                          manager part.</p>
                        {/*                                     <p> <strong>Tech Stack:</strong><span class ="label tgs">Java</span> <span class ="label tgs">SQlite</span></p> */}
                      </div>
                      {/*//desc*/}
                      {/* <a class="btn btn-cta-secondary" href="https://themes.3rdwavemedia.com/bootstrap-templates/startup/launch-bootstrap-4-template-for-saas-businesses/" target="_blank"><i class="fas fa-thumbs-up"></i> Back my project</a> */}
                    </div>
                    {/*//item*/}
                    <hr className="divider" />
                    <div className="item row">
                      <a className="col-md-4 col-12" href="https://github.com/JainMayankA/Machine-Learning-Project-/tree/master" target="_blank">
                        <img className="img-fluid project-image rounded shadow-sm" src="./images/download.png" alt="project name" />
                      </a>
                      <div className="desc col-md-8 col-12">
                        <h3 className="title"><a href="https://github.com/JainMayankA/Machine-Learning-Project-/tree/master" target="_blank">Car Make-Model Classifier</a></h3>
                        <p className="mb-2">Explored YOLOv3 and VGG16 in-depth for car detection and model
                          classification tasks on this
                          dataset:https://www.kaggle.com/jessicali9530/stanford-cars-dataset.
                          Conducted various image data preprocessing such as edge detection, gaussian
                          blur, denoise, image segmentation, and other methods.
                          Implemented a neural network pipeline where YOLOv3 passes object (car) detected
                          bounding box to VGG16 for car model prediction from 196 car classes. Applied
                          transfer learning on the VGG16 model for the task and achieved 99% accuracy on
                          the test and validation set with 100 epochs.</p>
                        {/*                                     <p> <strong>Tech Stack:</strong><span class ="label tgs">Python</span> <span class ="label tgs">Object Detection</span> <span class ="label tgs">Transfer Learning</span> <span class ="label tgs">Digital Image Interpolation</span></p> */}
                        {/*                                     <p> <strong>Tech Stack:</strong><span class ="label tgs">CUDA</span> <span class ="label tgs">scikit-learn</span> <span class ="label tgs">Keras</span> <span class ="label tgs">Tensorflow</span></p> */}
                        <p><a className="more-link" href="https://github.com/JainMayankA/Machine-Learning-Project-/tree/master" target="_blank"><i className="fas fa-external-link-alt" />Find out more</a>
                        </p>
                      </div>
                      {/*//desc*/}
                    </div>
                    {/*//item*/}
                    <hr className="divider" />
                    <div className="item row">
                      <a className="col-md-4 col-12" href="http://maj1066.uta.cloud/trial/jain_ciudad/html/Inicio.php" target="_blank">
                        <img className="img-fluid project-image rounded shadow-sm" src="./images/wdm.png" alt="project name" />
                      </a>
                      <div className="desc col-md-8 col-12">
                        <h3 className="title"><a href="http://maj1066.uta.cloud/trial/jain_ciudad/html/Inicio.php" target="_blank">Gente and Cuidad Website</a></h3>
                        <p className="mb-2">Designed a multi-client, responsive and dynamic website for an NGO
                          in a Spanish city.
                          Programmed login system, account registration/contact form, create/register
                          events, CMS functionality, and deployed on the cloud with MYSQL database. Also
                          adapted this project to the MVC pattern using Laravel 5.</p>
                        {/*                                     <p><strong>Tech Stack:</strong> <i class="devicon-html5-plain-wordmark" style='font-size:30px;'></i>, <i class="devicon-css3-plain" style='font-size:30px;'></i>,<i class="devicon-php-plain" style='font-size:30px;'></i>,<i class="devicon-javascript-plain" style='font-size:30px;'></i>,<i class="devicon-wordpress-plain" style='font-size:30px;'></i>, &amp; <i class="devicon-mysql-plain" style='font-size:30px;'></i></p> */}
                        <p><a className="more-link" href="https://github.com/JainMayankA/Web-Database-Management-Project" target="_blank"><i className="fas fa-external-link-alt" />Find out more</a>
                        </p>
                      </div>
                      {/*//desc*/}
                    </div>
                    {/*//item*/}
                    <hr className="divider" />
                    <div className="item row">
                      <a className="col-md-4 col-12" href="https://github.com/JainMayankA/Data_Mining" target="_blank">
                        <img className="img-fluid project-image rounded shadow-sm" src="./images/food.jpg" alt="project name" />
                      </a>
                      <div className="desc col-md-8 col-12">
                        <h3 className="title"><a href="https://github.com/JainMayankA/Data_Mining" target="_blank">Food Recipe Search</a></h3>
                        <p className="mb-2">Developed a search interface to display food recipes based on the
                          ingredients inserted by a user.
                          Analyzed multiple NTLK method outcomes for preprocessing the
                          dataset:https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions.
                          Programmed TF-IDF from scratch on 180K+ recipes and stored the data in ".pkl"
                          format for rendering search results in 0.2 seconds.</p>
                        {/*                                     <p> <strong>Tech Stack:</strong> <i class="devicon-python-plain-wordmark" style='font-size:30px;'></i>&amp; <i class="devicon-django-plain" style='font-size:30px;'></i></p> */}
                        <p><a className="more-link" href="https://github.com/JainMayankA/Data_Mining" target="_blank"><i className="fas fa-external-link-alt" />Find out more</a>
                        </p>
                      </div>
                    </div>
                    <hr className="divider" />
                    <div className="item row">
                      <a className="col-md-4 col-12" href="https://github.com/JainMayankA/Data_Mining" target="_blank">
                        <img className="img-fluid project-image rounded shadow-sm" src="./images/fd1.png" alt="project name" />
                      </a>
                      <div className="desc col-md-8 col-12">
                        <h3 className="title"><a href="https://github.com/JainMayankA/Data_Mining" target="_blank">Cuisine Classifier</a></h3>
                        <p className="mb-2">A dynamic pie chart interface categorizes the cuisine based on
                          recipes or ingredients entered by a user.
                          Calculated various NLTK method outcomes for preprocessing the dataset
                          https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions.
                          Implemented Multinomial Naive Bayes algorithm from scratch and achieved 80%
                          accuracy.
                        </p>
                        {/*                                    <p> <strong>Tech Stack:</strong> <i class="devicon-python-plain-wordmark" style='font-size:30px;'></i>&amp; <i class="devicon-django-plain" style='font-size:30px;'></i></p> */}
                        <p><a className="more-link" href="https://github.com/JainMayankA/Data_Mining" target="_blank"><i className="fas fa-external-link-alt" />Find out more</a>
                        </p>
                      </div>
                    </div>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </section>
              {/*//section*/}
              <section className="projects section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Projects</h2>
                  <div className="content">
                    <div className="item">
                      <h3 className="title"><a target="_blank">Semantic based automatic web service check
                          detection</a></h3>
                      <p className="summary"> Many web services do not have explicit associated semantic
                        descriptions. Therefore, implemented a prototype for semantic-based service
                        categorization of web services and enhancement of service request.Initiated the
                        ontology framework as a solution, with that implemented algorithms such as support
                        vector machine, prune association patterns, and mapping for achieving the desired
                        task.</p>
                    </div>
                    {/*//item*/}
                    <div className="item">
                      <h3 className="title"><a target="_blank">Pustakalaya (E-Library)</a></h3>
                      <p className="summary">An integrated library system, also known as a library management
                        system, is an enterprise resource planning system for a library, used to track items
                        owned, orders made, bills paid, and patrons who have borrowed.</p>
                    </div>
                    {/*//item*/}
                    <div className="item">
                      <h3 className="title"><a target="_blank">Tweet Creator Application</a></h3>
                      <p className="summary"> An application that will load a predefined set of short forms from a
                        text file that the user inputs as a command line argument. After which it prompts
                        the user to enter a phrase if the application can convert the phrase into an
                        acceptable tweet (that is of size less than 140 characters) it will do so and print
                        the same on the screen else the application will send a message to the user that it
                        cannot convert the message into a tweet. </p>
                    </div>
                    {/*//item*/}
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </section>
              {/*//section*/}
            </div>
            {/*//primary*/}
            <div className="secondary col-lg-4 col-12">
              <aside className="info aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading sr-only">Basic Information</h2>
                  <div className="content">
                    <ul className="list-unstyled">
                      <li><i className="fas fa-map-marker-alt" /><span className="sr-only">Location:</span>Arlington, Texas</li>
                    </ul>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//aside*/}
              <aside className="education aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Experience</h2>
                  <div className="content">
                    <div className="item">
                      <h3 className="title">Summer Fellowship: Computer Vision<span className="place"><br /><a>Athens Information Technology, Greece</a></span><br /><span className="year">(June 2018 - July 2018)</span></h3>
                      <p>
                        Acquired fundamental knowledge of computer vision methods such as image
                        recognition and object detection.
                        Implemented ResNet-34 for Face Recognition and YOLOv3 for Object Detection.
                        Studied the network for a more reliable understanding of their architecture.
                        Trained ResNet-34 on our team's custom face data and extended the project to
                        recognize three types of emotions. Acquired 90% accuracy on the test and
                        validation set by tuning the hyperparameters.
                        Hands-on practice on YOLOv3 based on the paper and other links.
                      </p>
                    </div>
                    {/*//item*/}
                    {/*//item*/}
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//section*/}
              <aside className="education aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Education</h2>
                  <div className="content">
                    <div className="item">
                      <h3 className="title"><i className="fas fa-graduation-cap" /> MSc Computer Science</h3>
                      <h4 className="university">University of Texas at Arlington <span className="year">(Aug. 2019-
                          Present)</span><br /><strong>GPA : 3.44/4 </strong></h4>
                    </div>
                    {/*//item*/}
                    <div className="item">
                      <h3 className="title"><i className="fas fa-graduation-cap" /> BE Computer Engineering</h3>
                      <h4 className="university">University of Mumbai <span className="year">(2014-2018)</span></h4>
                    </div>
                    {/*//item*/}
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//section*/}
              <aside className="skills aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading"> Technical Skills</h2>
                  <div className="content">
                    <p className="intro">
                      {/* Intro about your skills goes here. Keep the list lean and only show your primary skillset. You can always provide a link to your Linkedin or Github profile so people can get more info there.</p> */}
                    </p><div className="skillset">
                      <div className="item">
                        <h3 className="level-title">M.E.R.N. Stack<span className="level-label" data-toggle="tooltip" data-placement="left" data-animation="true" title="Currently sharpening comprehensive full-stack skills, I have academic and project-based experience with this stack."><i className="fas fa-info-circle" /></span></h3>
                        <div className="level-bar">
                          <div className="level-bar-inner" data-level="95%">
                          </div>
                        </div>
                      </div>
                      <div className="item">
                        <h3 className="level-title">Computer Vision or Medical Computer Vision<span className="level-label" data-toggle="tooltip" data-placement="left" data-animation="true" title="I have academic, certifications, fellowship, and projects-based experience in it."><i className="fas fa-info-circle" /></span></h3>
                        <div className="level-bar">
                          <div className="level-bar-inner" data-level="80%">
                          </div>
                        </div>
                      </div>
                      <div className="item">
                        <h3 className="level-title">Python-Django Stack <span className="level-label" data-toggle="tooltip" data-placement="left" data-animation="true" title="Familiar"><i className="fas fa-info-circle" /></span></h3>
                        <div className="level-bar">
                          <div className="level-bar-inner" data-level="60%">
                          </div>
                        </div>
                      </div>
                      <p><a className="more-link" href="https://github.com/JainMayankA"><i className="fas fa-external-link-alt" />More on Github</a></p>
                    </div>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//section*/}
              <aside className="blog asde section">
                <div className="section-inner shadow-sm rounded">
                  <div id="carouselExampleIndicators" className="carousel slide" data-ride="carousel">
                    <div className="carousel-inner">
                      <div className="carousel-item active">
                        <h2 className="heading">Intelligent Systems (Computer Vision)</h2>
                        <dl>
                          <dt>Coursework</dt>
                          <dd>Machine Learning, Neural Network, Design and Analysis of Algorithm, Data Mining, Data Analysis and Modelling Techniques, Artificial Intelligence, Software Testing.</dd>
                          <dt>Skills</dt>
                          <dd>Programming languages: Python, C/C++.</dd>
                          <dd>Cloud: GCP, AWS, Azure.</dd>
                          <dd>Tools/Frameworks: OpenCV, PyTorch, Scipy, Tensorflow, Keras, Matplotlib, Cmake, Numpy, Scikit-Learn, Pandas, scikit-image.</dd>
                          <dd>Platform: Anaconda, Jupyter, Spider, Google Colab.</dd>
                          <dd> 
                            {/* Knowledge: Image Classification, Recognition and Semantic Segmentation, Object Detection, Tracking and Localization, Perception, Multiple View Geometry, Image Processing, Information Retrieval, Hyperparameter Optimization, Multi-class Learning and Classification, A/B testing, 3D Computer Vision, Performance Benchmarking, Linear Algebra, Statistics and Probability.</dd> */}
                          </dd><dt>Certifications:</dt>
                          {/* <ol> */}
                          {/* <li> */}
                          <a href="https://graduation.udacity.com/confirm/NGGCGSZH">
                            <dd>Computer Vision NanoDegree</dd></a>
                          {/* </li> */}
                          {/* <li> */}
                          <a href="https://coursera.org/share/6b7dce850e4adaf391a147507f418d35">
                            <dd>Computer Vision Basics</dd></a>
                          {/* </li> */}
                          {/* <li> */}
                          <a href="https://coursera.org/share/8b68d0da314dfb38a9cb003c76cdda03">
                            <dd>Deep Learning Specialization</dd></a>
                          {/* </li> */}
                          {/* <li> */}
                          <a href="https://coursera.org/share/2e411cb3bb4f115f5b8a08424c884748">
                            <dd>AI for Medicine Specialization</dd>
                            {/* </li> */}
                          </a>
                          {/* </ol> */}
                        </dl>
                      </div>
                      <div className="carousel-item">
                        <h2 className="heading">Software Engineering <br /> (Full-Stack Development)</h2>
                        <dl>
                          <dt>Coursework</dt>
                          <dd>Software Engineering 1, Software Engineering 2, Software Testing, Advanced Software Engineering, Web Database Management, Design and Analysis of Algorithm, Data Mining,  Object Oriented Programming,Data Structures, Database Management Systems, Distributed Database, Big Data Analytics, Cloud Computing, Web technology.</dd>
                          <dt>Skills</dt>
                          <dd>Front-end: Javascript(ES6), jQuery, React.js,HTML5,CSS3,Bootstrap 4,Redux.</dd>
                          <dd>Back-end: Python, PHP, Node.js, Express.js, REST, Django, Express.js, Laravel 5, NPM, EJS, C/C++.</dd>
                          <dd>Operating System: Windows, Linux.</dd>
                          <dd>Database: MySQL, MongoDB, SQLite, Firebase.</dd>
                          <dd>Other: C/C++,Git, Github, Android Studio, Windows, Linux, AWS, GCP.</dd>
                          <dt>Certifications</dt>
                          <a href="https://www.udemy.com/certificate/UC-818d8821-2c4e-4af3-a115-9a2036c1811a/"><dd>The Complete 2021 Web Development Bootcamp</dd></a>
                          <a href="https://www.udemy.com/certificate/UC-3fdaf599-55b2-4c3e-a36f-17fed56c8759/"><dd>Google Associate Cloud Engineer: Udemy</dd></a>
                        </dl>
                      </div>
                    </div>
                    <a className="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                      <span className="carousel-control-prev-icon" aria-hidden="true" />
                      <span className="sr-only">Previous</span>
                    </a>
                    <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                      <span className="carousel-control-next-icon" aria-hidden="true" />
                      <span className="sr-only">Next</span>
                    </a>
                  </div>
                </div>
              </aside>
              <aside className="languages aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">ExtraCurricular</h2>
                  <div className="content">
                    <ul className="list-unstyled">
                      <li className="item">
                        <span className="title"><strong>UTA Student Volunteer:</strong></span>
                        <span className="level">August 2019 - May 2020<br className="visible-xs" /></span>
                      </li>
                      {/*//item*/}
                      <li className="item">
                        <span className="title"><strong>IEEE Student Volunteer:</strong></span>
                        <span className="level"> January 2017 - May 2018 <br className="visible-sm visible-xs" /></span>
                      </li>
                      {/*//item*/}
                    </ul>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              <aside className="list music aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Favourite coding music</h2>
                  <div className="content">
                    <ul className="list-unstyled">
                      <li><i className="fas fa-headphones" /> <a href="https://www.youtube.com/watch?v=Rb0UmrCXxVA">The Best of Mozart</a></li>
                      <li><i className="fas fa-headphones" /> <a href="https://www.youtube.com/watch?v=l9nh1l8ZIJQ">CONNECTION LOST</a></li>
                      <li><i className="fas fa-headphones" /> <a href="https://www.youtube.com/watch?v=5NVa4w-UXwA">Downtempo Music</a></li>
                      <li><i className="fas fa-headphones" /> <a href="https://www.youtube.com/watch?v=OtpnWZQX2yU">Drum &amp; Bass Mix</a></li>
                    </ul>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//section*/}
              <aside className="list conferences aside section">
                <div className="section-inner shadow-sm rounded">
                  <h2 className="heading">Soft Skills</h2>
                  <div className="content">
                    <ul className="list-unstyled">
                      <li><i className="fas fa-angle-right" /> Self-Motivation and Handling Pressure</li>                                
                      <li><i className="fas fa-angle-right" /> Leadership and Collaboration</li>
                      <li><i className="fas fa-angle-right" /> Approachability and Helpfulness</li>
                      <li><i className="fas fa-angle-right" /> Open-mindedness and Communication</li>
                      <li><i className="fas fa-angle-right" /> Detail Oriented and Accountability </li>
                      <li><i className="fas fa-angle-right" /> Creativity and Problem Solving </li>
                      <li><i className="fas fa-angle-right" /> Resilience and Learner</li>
                    </ul>
                  </div>
                  {/*//content*/}
                </div>
                {/*//section-inner*/}
              </aside>
              {/*//section*/}
            </div>
            {/*//secondary*/}
          </div>
          {/*//row*/}
        </div>
        {/*//masonry*/}
        {/* ******FOOTER****** */}
        <footer className="footer">
          <div className="container text-center">
          </div>
          {/*//container*/}
        </footer>
        {/*//footer*/}
        {/* Javascript */}
      </div>
    </div>
  );
}
  
}

export default App;
