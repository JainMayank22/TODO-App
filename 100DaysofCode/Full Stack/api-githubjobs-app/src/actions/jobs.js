import axios from 'axios';
import moment from 'moment';
import { BASE_API_URL } from '../utils/constants';
import { setErrors } from './errors';


// Get JSON data by making API Call to Express Server 
export const initiateGetJobs = (data,isLoadMore) => {
  return async (dispatch) => {
    try {
      let { description, full_time, location, page } = data;
      description = description ? encodeURIComponent(description) : '';
      location = location ? encodeURIComponent(location) : '';
      full_time = full_time ? '&full_time=true' : '';

      if (page) {
        page = parseInt(page);
        page = isNaN(page) ? '' : `&page=${page}`;
      }
//  for calling from the api
      const jobs = await axios.get(
        `${BASE_API_URL}/jobs?description=${description}&location=${location}${full_time}${page}`
      );

      //  Pre stored json data
      // const jobs = await axios.get('./jobs.json');

    
      //  For sorting the jobs
      const sortedJobs = jobs.data.sort(
        (a, b) =>
          moment(new Date(b.created_at)) - moment(new Date(a.created_at))
      );
      if (isLoadMore) {
        return dispatch(setLoadMoreJobs(sortedJobs));
      } else {
        return dispatch(setJobs(sortedJobs));
      }
    } catch (error) {
      error.response && dispatch(setErrors(error.response.data));
    }
  };
};

// Adding job once dispatched by executing switch case in reducers/jobs.js file
export const setJobs = (jobs) => ({
  type: 'SET_JOBS',
  jobs
});

export const setLoadMoreJobs = (jobs) => ({
  type: 'LOAD_MORE_JOBS',
  jobs
});
