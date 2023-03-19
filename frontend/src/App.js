import React, { useEffect, useState } from 'react';
import './App.css';
import StoryChoices from './components/StoryChoices';
import { fetchFirstPart, fetchNextPart } from './api';

const App = () => {
  const [storyPart, setStoryPart] = useState(null);

  useEffect(() => {
    const loadFirstPart = async () => {
      const firstPart = await fetchFirstPart();
      setStoryPart(firstPart);
    };
    loadFirstPart();
  }, []);

  const handleChoiceSelected = async (choice) => {
    const nextPart = await fetchNextPart(choice);
    setStoryPart(nextPart);
  };

  return (
    <div className="App">
      {storyPart && (
        <>
          <h1>{storyPart.title}</h1>
          <p>{storyPart.content}</p>
          <StoryChoices choices={storyPart.choices} onChoiceSelected={handleChoiceSelected} />
        </>
      )}
    </div>
  );
};

export default App;
