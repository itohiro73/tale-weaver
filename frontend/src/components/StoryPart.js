import React, { useState, useEffect } from "react";
import { fetchFirstPart } from "../api";

const StoryPart = ({ storyPart, onStoryLoaded }) => {
  const [localStoryPart, setLocalStoryPart] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await fetchFirstPart();
        setLocalStoryPart(result);
        onStoryLoaded(result);
      } catch (error) {
        console.error("Failed to fetch the story part:", error);
      }
    };

    if (!localStoryPart.title) {
      fetchData();
    }
  }, [localStoryPart, onStoryLoaded]);

  const displayStoryPart = storyPart || localStoryPart;

  return (
      <div className="story-part">
        <h1>{displayStoryPart.title}</h1>
        <p>{displayStoryPart.content}</p>
      </div>
  );
};

export default StoryPart;
