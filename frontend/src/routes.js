import React from 'react';
import { Route, Routes as ReactRouterRoutes } from 'react-router-dom';
import Home from './pages/Home';
import Story from './pages/Story';

const TaleWeaverRoutes = () => {
  return (
    <ReactRouterRoutes>
      <Route path="/" element={<Home />} />
      <Route path="/story/:id" element={<Story />} />
    </ReactRouterRoutes>
  );
};

export default TaleWeaverRoutes;
