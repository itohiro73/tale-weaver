import React, { useState, useEffect } from "react";
import { fetchFirstPart } from "../api";

const StoryPart = ({ onStoryLoaded }) => {
  const [storyPart, setStoryPart] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await fetchFirstPart();
        setStoryPart(result);
        onStoryLoaded(result);
      } catch (error) {
        console.error("Failed to fetch the story part:", error);
      }
    };

    fetchData();
  }, [onStoryLoaded]);

  return (
      <div className="story-part">
        <h1>{storyPart.title}</h1>
        <p>{storyPart.content}</p>
      </div>
  );
};

export default StoryPart;
