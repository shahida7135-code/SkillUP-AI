import React, { useState } from 'react';

const YouTubeSearch = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSearch} style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
      <input 
        type="text" 
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search skills (e.g., Python Basics)"
        style={{ 
          padding: '10px', 
          width: '100%', 
          maxWidth: '400px', 
          borderRadius: '4px', 
          border: '1px solid #ccc' 
        }}
      />
      <button 
        type="submit" 
        style={{ 
          padding: '10px 20px', 
          backgroundColor: '#007BFF', 
          color: 'white', 
          border: 'none', 
          borderRadius: '4px', 
          cursor: 'pointer' 
        }}
      >
        Search
      </button>
    </form>
  );
};

export default YouTubeSearch;