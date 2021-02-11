import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import notes from "../notes";





function App() {
  return (
    <div>
      <Header />
      {notes.map( (noteItems) => <Note 
    key = {noteItems.id}
    title = {noteItems.title}
    content = {noteItems.content}
  /> 
)};
      <Footer />
    </div>
  );
}

export default App;
