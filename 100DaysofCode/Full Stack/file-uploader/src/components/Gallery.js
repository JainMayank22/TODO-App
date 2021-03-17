import React, {useState, useEffect} from 'react';
import {connect} from 'react-redux';
import {startLoadPictures} from '../actions/photos';
import Picture from  './Picture';

const Gallery = ({errors, pictures, dispatch})=>{

    const [isLoading, setIsLoading] = useState(false);
    useEffect(()=>{
        setIsLoading(true);
        dispatch(startLoadPictures());
    }, []);
    useEffect(()=>{
        if (pictures.length>0){
            setIsLoading(false);    
        }
        
    }, [pictures]);

    return (
        <div className="photos-list">
        {errors && errors.get_error && (
            <p  className="errorMsg centered-message">{errors.get_error}</p>
        )}
        {isLoading ? (
            <div className="loading-msg centered-message">Loading...</div>
        ): (pictures.map((picture)   =>  <Picture key={picture._id}  id ={picture._id} />))
        }
        </div>
    );
};
const mapStateToProps = (state) => ({
    pictures: state.pictures || [],
    errors: state.errors || {}
  });
  
  export default connect(mapStateToProps)(Gallery);

