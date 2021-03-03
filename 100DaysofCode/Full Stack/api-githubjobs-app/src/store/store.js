import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import {apiMiddleware} from 'redux-api-middleware';
import api from 'redux-cached-api-middleware';
import jobsReducer from '../reducers/jobs';
import errorsReducer from '../reducers/errors';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  combineReducers({
    jobs: jobsReducer,
    errors: errorsReducer,
    [api.constants.NAME]: api.reducer,
  }),
  composeEnhancers(applyMiddleware(thunk,apiMiddleware))
);

console.log(store.getState());

export default store;

// ReduxThunk as a Middleware for Asynchronous API handling