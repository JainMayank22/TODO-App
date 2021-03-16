import React from "react";
import {NavLink} from "react-router-dom";

const Header = ()=>(
    <header>
        <h1>Picture Gallery</h1>
        <div className="links">
            <NavLink to="/" className="link">
                Home
            </NavLink>
            <NavLink to="/picture-lib" className="link">
                Gallery
            </NavLink>
        </div>
    </header>
);
export default Header;