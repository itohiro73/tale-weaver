import React, { useEffect, useState } from 'react';
import './App.css';
import StoryChoices from './components/StoryChoices';
import { fetchFirstPart } from './api';

const App = () => {
  const [storyPart, setStoryPart] = useState(null);
  const choices = ["Go to the forest", "Visit the blacksmith"];

  useEffect(() => {
    const loadFirstPart = async () => {
      const firstPart = await fetchFirstPart();
      setStoryPart(firstPart);
    };
    loadFirstPart();
  }, []);

  const handleChoiceSelected = (choice) => {
    console.log("Selected choice:", choice);
  };

  return (
    <div className="App">
      {storyPart && (
        <>
          <h1>{storyPart.title}</h1>
          <p>{storyPart.content}</p>
        </>
      )}
      <StoryChoices choices={choices} onChoiceSelected={handleChoiceSelected} />
    </div>
  );
};

export default App;
