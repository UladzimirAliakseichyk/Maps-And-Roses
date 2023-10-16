import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import ReviewList from './components/ReviewList';
import Header from './components/Header';
import LeaveReviewPage from './components/LeaveReviewPage';


function App() {
  return (
    <Router>
      <div>
        <Header />
        <Routes>
          <Route path="/" element={<ReviewList />} />
          <Route path="/new-review" element={<LeaveReviewPage />} />
          {/* Добавьте другие маршруты, если необходимо */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
