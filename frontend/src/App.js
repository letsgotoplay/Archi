// Main App Component

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ProjectDashboard from './components/ProjectDashboard';
import ProjectSubmissionForm from './components/ProjectSubmissionForm';
import SearchInterface from './components/SearchInterface';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<ProjectDashboard />} />
          <Route path="/submit" element={<ProjectSubmissionForm />} />
          <Route path="/search" element={<SearchInterface />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
