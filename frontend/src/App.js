import React, { useState } from 'react';
import './App.css';
import StoryChoices from './components/StoryChoices';
import StoryPart from './components/StoryPart';
import { fetchNextPart } from './api';

const App = () => {
    const [storyPart, setStoryPart] = useState(null);

    const handleChoiceSelected = async (selectedChoice) => {
        const nextPart = await fetchNextPart({ choice: selectedChoice, prev_title: storyPart.title, prev_content: storyPart.content });
        console.log('Next part:', nextPart);
        setStoryPart(nextPart);
    };

    return (
        <div className="App">
            <StoryPart storyPart={storyPart} onStoryLoaded={setStoryPart} />
            {storyPart && (
                <>
                    <StoryChoices choices={storyPart.choices} onChoiceSelected={handleChoiceSelected} />
                </>
            )}
        </div>
    );
};

export default App;
