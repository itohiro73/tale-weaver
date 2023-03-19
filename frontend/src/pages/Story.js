import React from 'react';
import { useParams } from 'react-router-dom';

const Story = () => {
  const { id } = useParams();

  return (
    <div>
      <h1>Story {id}</h1>
      <p>This is the detail page for story {id}.</p>
    </div>
  );
};

export default Story;
