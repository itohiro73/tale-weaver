import React from 'react';
import './StoryChoices.css';

const StoryChoices = ({ choices, onChoiceSelected }) => {
  return (
    <div className="story-choices">
      {choices.map((choice, index) => (
        <button key={index} onClick={() => onChoiceSelected(choice)}>
          {choice}
        </button>
      ))}
    </div>
  );
};

export default StoryChoices;
