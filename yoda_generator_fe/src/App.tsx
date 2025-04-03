import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [inputText, setInputText] = useState('');
  const [yodaText, setYodaText] = useState('');

  const translateToYoda = () => {
    // Placeholder translation: reverse the word order.
    // Replace with your API call to generate Yoda speech.
    const words = inputText.split(' ');
    const translated = words.reverse().join(' ');
    setYodaText(translated);
  };

  return (
    <div className="app-container">
      <h1>Yoda Speech Generator</h1>
      <div className="translator-container">
        <div className="yoda-image-container">
          <img src="/baby_yoda.jpg" alt="Yoda" style={{ transform: "scaleX(-1)" }} />
        </div>
        <div className="input-output-area">
          <textarea
            className="input-textarea"
            placeholder="Type your message here..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
          <button className="translate-button" onClick={translateToYoda}>
            Translate
          </button>
          {yodaText && (
            <div className="output-area">
              <h2>Yoda Says:</h2>
              <p>{yodaText}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;