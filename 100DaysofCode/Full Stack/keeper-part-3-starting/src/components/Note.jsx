import React from "react";

function Note(props) {

  function handleChange(){
    props.onDelete(props.id);

  }


  return (
    <div className="note">
      <h1>{props.title}</h1>
      <p>{props.content}</p>
      <button onClick = {handleChange}> DELETE</button>
    </div>
  );
}

export default Note;
