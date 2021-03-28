/* eslint-disable react-hooks/exhaustive-deps */
import React, {useState, useEffect} from 'react';
import {connect} from 'react-redux';
import {startLoadPictures} from '../actions/photos';
import Picture from  './Picture';

const Gallery = ({errors, photos, dispatch})=>{

    const [isLoading, setIsLoading] = useState(false);
    useEffect(()=>{
        setIsLoading(true);
        dispatch(startLoadPictures());
    }, []);
    useEffect(()=>{
        if (photos.length >   0){
            setIsLoading(false);    
        }
        
    }, [photos]);

    return (
        <div className="photos-list">
        {errors && errors.get_error && (
            <p  className="errorMsg centered-message">{errors.get_error}</p>
        )}
        {isLoading ? (
            <div className="loading-msg centered-message">Loading...</div>
        ): (photos.map((photo)   =>  <Picture key={photo._id}  id ={photo._id} />))
        }
        </div>
    );
};
const mapStateToProps = (state) => ({
    photos: state.photos || [],
    errors: state.errors || {}
  });
  
  export default connect(mapStateToProps)(Gallery);
