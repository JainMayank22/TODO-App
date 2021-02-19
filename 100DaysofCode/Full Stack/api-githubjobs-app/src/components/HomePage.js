import React, { useState, useEffect } from 'react';
import _ from 'lodash';
import { connect } from 'react-redux';
import { initiateGetJobs } from '../actions/jobs';
import { resetErrors } from '../actions/errors';
import Header from './Header';
import Search from './Search';
import Results from './Results';
import JobDetails from './JobDetails';
import JobsContext from '../context/jobs';

// Declared state variables by hook to store the results from the API in array 
// and flag for "loading.." & "when to display the details page" default is set to home
// and object for error detection
const HomePage = (props) => {
  const [results, setResults] = useState([]);
  const [errors, setErrors] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [jobId,setJobId] = useState([-1]);
  const [page, setPage] = useState('home');
//  Calling the hooks to get list or error if any
//  passing dependency array as second argument to control when effect executed and is different 
  useEffect(() => {
    setResults(props.jobs);
  }, [props.jobs]);

  useEffect(() => {
    setErrors(props.errors);
  }, [props.errors]);

  const loadJobs = (selection) => {
    const { dispatch } = props;
    const { description, location, full_time, page = 1 } = selection;
    dispatch(resetErrors());
    setIsLoading(true);
    dispatch(initiateGetJobs({ description, location, full_time, page }))
      .then(() => {
        setIsLoading(false);
      })
      .catch(() => setIsLoading(false));
  };
//  handleSearch calling function loadJobs->
// initiateGetJobs action to make API call to Express server
  const handleSearch = (selection) => {
    loadJobs(selection);
  };
//  for handling and filtering the job results for job more info display page
  const handleItemClick = (jobId) => {
    setPage('details');
    setJobId(jobId);
  };
  const handleResetPage = () => {
    setPage('home');
  };
  
  let jobDetails = {};
  if (page === 'details') {
    jobDetails = results.find((job) => job.id === jobId);
  }

  const value = {
    results,
    details: jobDetails,
    onSearch: handleSearch,
    onItemClick: handleItemClick,
    onResetPage: handleResetPage
  };
// JobsContext.Provider tag can access any value from the value object passed as prop
  return (
    <JobsContext.Provider value={value}>
      <div className={`${page === 'details' && 'hide'}`}>
        <Header /> 
        <Search />
        {!_.isEmpty(errors) && (
          <div className="errorMsg">
            <p>{errors.error}</p>
          </div>
        )}
        {isLoading && <p className="loading">Loading...</p>} 
        <Results />
      </div>
      <div className={`${page === 'home' && 'hide'}`}>
        {page === 'details' && <JobDetails />}
      </div>
    </JobsContext.Provider>
  );
};
//  the data is saved for the dependency array props.jobs
const mapStateToProps = (state) => ({
  jobs: state.jobs,
  errors: state.errors
});
//  connection of react-redux lib
export default connect(mapStateToProps)(HomePage);


// Implemented the componentDidUpdate lifecycle method of class component using the hooks