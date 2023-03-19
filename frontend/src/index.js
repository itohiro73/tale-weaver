import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import './index.css';
import App from './App';
import TaleWeaverRoutes from './routes';
import reportWebVitals from './reportWebVitals';
import { fetchFirstPart } from './api';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App>
        <TaleWeaverRoutes />
      </App>
    </BrowserRouter>
  </React.StrictMode>,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

(async () => {
  const firstPart = await fetchFirstPart();
  console.log('First part of the story:', firstPart);
})();