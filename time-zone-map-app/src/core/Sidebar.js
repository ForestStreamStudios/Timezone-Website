import React, { useState } from 'react';
import AppStyle from '../App.css';



function Sidebar() {
    const [content, setContent] = useState("");
    return (
        <div className="sidebar">
            <h3>Instructions</h3>
            <p>Use the dropdown to filter by team. Location hotspots will appear on the map.</p>
            <h3>About</h3>
            <p>A tool to plan meetings for decentralized, global organizations.</p>

        </div>
    );
}

export default Sidebar;
