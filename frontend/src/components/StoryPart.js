import React, { useState, useEffect } from "react";
import { fetchFirstPart } from "../api";

const StoryPart = ({ storyPart, onStoryLoaded }) => {
  const [localStoryPart, setLocalStoryPart] = useState({});

  useEffect(() => {
    let fetched = false;

    const fetchData = async () => {
      try {
        const result = await fetchFirstPart();
        if (!fetched) {
          setLocalStoryPart(result);
          onStoryLoaded(result);
        }
      } catch (error) {
        console.error("Failed to fetch the story part:", error);
      }
    };

    if (!storyPart) {
      fetchData();
    }

    return () => {
      fetched = true;
    };
  }, [storyPart, onStoryLoaded]);

  const displayStoryPart = storyPart || localStoryPart;

  return (
      <div className="story-part">
        <h1>{displayStoryPart.title}</h1>
        <p>{displayStoryPart.content}</p>
      </div>
  );
};

export default StoryPart;
