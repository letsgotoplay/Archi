// AI Search Interface Component

import React, { useState } from 'react';
import api from '../api';

const SearchInterface = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query) return;

    setLoading(true);
    try {
      const response = await api.get(`/search/?query=${encodeURIComponent(query)}`);
      setResults(response.data);
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div style={{ textAlign: 'center', marginBottom: '40px' }}>
        <h2>Chat with your Codebase</h2>
        <p>Ask natural language questions to discover internal tools and projects.</p>
        <form onSubmit={handleSearch} style={{ maxWidth: '600px', margin: '0 auto', display: 'flex', gap: '10px' }}>
          <input
            type="text"
            className="form-control"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g., Do we have any internal tools for Kafka monitoring?"
            style={{ fontSize: '1.1rem', padding: '12px' }}
          />
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? 'Searching...' : 'Ask AI'}
          </button>
        </form>
      </div>

      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        {results.map((item, index) => (
          <div key={index} className="card">
             <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <h3 style={{ margin: '0 0 10px 0' }}>
                    {item.project.name}
                    <span style={{ fontSize: '0.8rem', fontWeight: 'normal', marginLeft: '10px', color: '#666' }}>
                        Match Score: {Math.round(item.score * 100)}%
                    </span>
                </h3>
                <span className="badge">{item.project.status}</span>
             </div>
             <p style={{ fontStyle: 'italic', color: '#555', borderLeft: '4px solid #007bff', paddingLeft: '10px' }}>
                 AI Insight: {item.reason}
             </p>
             <p>{item.project.description}</p>
             <a href={item.project.vcs_url} target="_blank" rel="noopener noreferrer">View Code</a>
          </div>
        ))}
        {results.length === 0 && !loading && query && (
            <p style={{ textAlign: 'center', color: '#666' }}>No relevant projects found.</p>
        )}
      </div>
    </div>
  );
};

export default SearchInterface;
