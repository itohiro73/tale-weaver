import React, { useState, useEffect } from "react";
import { fetchFirstPart } from "../api";

const StoryPart = () => {
  const [storyPart, setStoryPart] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await fetchFirstPart();
        setStoryPart(result);
      } catch (error) {
        console.error("Failed to fetch the story part:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>{storyPart.title}</h2>
      <p>{storyPart.content}</p>
    </div>
  );
};

export default StoryPart;
