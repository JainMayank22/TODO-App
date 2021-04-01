/* eslint-disable react-hooks/exhaustive-deps */

import React, {useState, useEffect, useRef} from 'react';
import _ from 'lodash';
import { connect } from 'react-redux';
import {loadUsers} from '../actions/users';
import UsersList from './UsersList';
import Header from './Header';
import Filters from  './Filters';

const HomePage = (props) => {
    const [users, setUsers] = useState(props.users);
    const [sortOrder, setSortOrder] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const inputRef = useRef();
    //  call api to get list of users
    useEffect(()=>{
        setIsLoading(true);
        props.dispatch(loadUsers());
        //  to avoid many api calls
        // initialize debounce function to search once user has
        //  stopped typing every half second
        inputRef.current = _.debounce(onSearchText, 500);
        //  storing function returned by debounce in inputRef
    }, []);
    // initializing the debounce method once when component mounter
    //  because passing the empty array as second argument
    useEffect(() => {
        if (props.users.length>0){
            setUsers(props.users);
            setIsLoading(false);
        }
    }, [props.users]);
    //  this is internally called by handleSearch to filter out the results
    function onSearchText(text,props){
        let filtered;
        if (text) {
            filtered = props.users.filter((user)=>
            user.country.toLowerCase().includes(text.toLowerCase()));
        } else {
            filtered = props.users;
        }
        setUsers(filtered);
        setSortOrder('');
    }
    // used for calling inputRef function when user inputs in text box 
    function handleSearch(event){
        inputRef.current(event.target.value, props);
    }
    //   to handle the prop call for sort method from Filters select component
    //  lodash orderBy method optimize the performance to sort faster
    function handleSort(sortOrder){
        setSortOrder(sortOrder);
        if (sortOrder.value) {
            setUsers(_.orderBy(users, ['age'], [sortOrder.value]));
        }
    }
    return (
        <React.Fragment>
            <Header handleSearch={handleSearch} />
            <Filters handleSort={handleSort} sortOrder={sortOrder} />
            <UsersList users = {users} isLoading={isLoading} />
        </React.Fragment>
    );
};

// populate with user results which can be accessed by props.users

const mapStateToProps = (state) => ({
    users: state.users
});
//  connection to handle change in redux store  
export default connect (mapStateToProps)(HomePage);