import React from 'react';
import {Card} from 'react-bootstrap';

const Picture = ({id}) => {
    return (
        <Card className="photo">
        <Card.Img variant = "top" src = {`http://localhost:3300/photos/${id}`} alt = "Picture"/>
        </Card>
    );
};
export default Picture;