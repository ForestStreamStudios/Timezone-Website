import React, { useState } from 'react';

function Header({ dropdownOptions, updateFilter }) {
  const [option, setOption] = useState(dropdownOptions[0].text)
  return (
    <header className="Header">
      <div>Time Zone App</div>
      <div>{option}</div>
      <select onChange={(e) => {
        updateFilter(e.target.value)
        setOption(e.target.value)
      }}>
        {
          dropdownOptions.map((e, key) => {
            return <option key={key} value={e.text}>{e.text}</option>;
          })
        }
      </select>


    </header>
  );
}

export default Header;
