import React, { useState, useCallback } from 'react';
import './App.css';
import StoryChoices from './components/StoryChoices';
import StoryPart from './components/StoryPart';
import { fetchNextPart } from './api';

const App = () => {
    const [storyPart, setStoryPart] = useState(null);
    const [choiceCount, setChoiceCount] = useState(0);

    const handleChoiceSelected = async (selectedChoice) => {
        const requestData = { choice: selectedChoice, prev_title: storyPart.title, prev_content: storyPart.content, choice_count: choiceCount };
        console.log('Request data:', requestData);  // 追加
        const nextPart = await fetchNextPart(requestData);
        console.log('Next part:', nextPart);
        setStoryPart(nextPart);
        setChoiceCount(choiceCount + 1);
    };

    const onStoryLoaded = useCallback((story) => {
        setStoryPart(story);
    }, []);

    return (
        <div className="App">
            <StoryPart storyPart={storyPart} onStoryLoaded={onStoryLoaded} />
            {storyPart && storyPart.choices && (
                <>
                    <StoryChoices choices={storyPart.choices} onChoiceSelected={handleChoiceSelected} />
                </>
            )}
        </div>
    );
};

export default App;
