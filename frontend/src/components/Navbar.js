// Navigation Bar Component

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav style={{ background: '#333', color: '#fff', padding: '10px 20px' }}>
      <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ margin: 0, fontSize: '1.5rem' }}>InnerSource Hub</h1>
        <ul style={{ listStyle: 'none', display: 'flex', gap: '20px', margin: 0 }}>
          <li><Link to="/" style={{ color: '#fff', textDecoration: 'none' }}>Dashboard</Link></li>
          <li><Link to="/submit" style={{ color: '#fff', textDecoration: 'none' }}>Submit Idea</Link></li>
          <li><Link to="/search" style={{ color: '#fff', textDecoration: 'none' }}>AI Search</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
