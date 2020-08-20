import React, { useState } from 'react';

function Header({ dropdownOptions, updateFilter }) {
  const [option, setOption] = useState(dropdownOptions[0].value)
  return (
    <header className="Header">
      <div className="logo">Time Zone App</div>
      <div>{option}</div>
      <div>
        <select onChange={(e) => {
          updateFilter(e.target.value)
          setOption(e.target.value)
        }}>
          {
            dropdownOptions.map((e, key) => {
              return <option key={key} value={e.value}>{e.text}</option>;
            })
          }
        </select></div>


    </header>
  );
}

export default Header;
