import React, {useState, useEffect} from 'react';
import {connect} from 'react-redux';
import {Form, Button} from 'react-bootstrap';
import {beginAddPicture} from '../actions/photos';

//  Add Comment if any
const UploadForm = ({errors,dispatch}) => {
    const [picture, setPicture] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMsg, setErrorMsg] = useState(null);

//  Add Comment if any
    useEffect(()=>{
        setErrorMsg(errors);
    },[errors]);
//  Add Comment if any
    useEffect(()=>{
        setErrorMsg('');
    },[]);
//  Add Comment if any
    const handleOnChange =(event) => {
        const file = event.target.files[0];
        setPicture(file);
    };
// Add Comment if any
    const handleFormSubmit =(event) => {
        event.preventDefault();
        if(picture){
            setErrorMsg('');
            dispatch(beginAddPicture(picture));
            setIsSubmitted(true);
        }
    };
// Add Comment if any
    return(
        <React.Fragment>
            {errorMsg && errorMsg.upload_error ? (<p className="errorMsg centered-message">{errorMsg.upload_error}</p>):
            isSubmitted && (<p className="successMsg centered-message">Picture successfully uploaded</p>)
            }
            <Form onSubmit = {handleFormSubmit}
            method = "POST"
            encType = "multipart/form-data"
            className="upload-form"
            >
            <Form.Group>
                <Form.Text>Choose Picture to Upload</Form.Text>
                <Form.Control type = "file" name = "picture" onChange = {handleOnChange} />
            </Form.Group>
            <Button variant="primary" type="submit" className = {`${ !picture ? 'disabled submit-btn': 'submit-btn' }`} disabled = {picture? false:true}>Upload</Button>
            </Form>
        </React.Fragment>
    );
};

// Add Comment if any

const mapStateToProps = (state) => ({
    pictures: state.pictures || [],
    errors: state.errors || {}
});

export default connect(mapStateToProps)(UploadForm);
