const jobsReducer = (state = [], action) => {
    switch (action.type) {
      case 'SET_JOBS':
        return action.jobs;
      case 'LOAD_MORE_JOBS':
        return [...state, ...action.jobs];
      default:
        return state;
    }
  };
  export default jobsReducer;

//  SET_JOBS:For adding jobs data from API using redux
//  LOAD_MORE_JOBS: For adding more jobs to the existing using spread operator 