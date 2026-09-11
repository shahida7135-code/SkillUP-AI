import React, { useState, useEffect } from 'react';
import YouTubeSearch from './YouTubeSearch';
import YouTubeVideoCard from './YouTubeVideoCard';
import { fetchYouTubeVideos } from '../../services/youtubeService';

const YouTubeVideoList = ({ defaultQuery }) => {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loadVideos = async (searchQuery) => {
    setLoading(true);
    setError(null);
    try {
      const results = await fetchYouTubeVideos(searchQuery);
      if (results.length === 0) {
        setError("No videos found or error fetching resources.");
      }
      setVideos(results);
    } catch (err) {
      setError("Failed to load videos.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (defaultQuery) {
      loadVideos(defaultQuery);
    }
  }, [defaultQuery]);

  return (
    <div style={{ padding: '20px 0' }}>
      <YouTubeSearch onSearch={loadVideos} />
      
      {loading && <p>Loading learning resources...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      {!loading && !error && (
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
          gap: '20px' 
        }}>
          {videos.map((video) => (
             <YouTubeVideoCard key={video.videoId} video={video} />
          ))}
        </div>
      )}
    </div>
  );
};

export default YouTubeVideoList;