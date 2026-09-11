import React from 'react';

const YouTubeVideoCard = ({ video }) => {
  const videoUrl = `https://www.youtube.com/watch?v=${video.videoId}`;

  return (
    <div style={{ 
      border: '1px solid #e0e0e0', 
      borderRadius: '8px', 
      overflow: 'hidden',
      backgroundColor: '#fff',
      transition: 'transform 0.2s',
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
    }}>
      <a href={videoUrl} target="_blank" rel="noopener noreferrer">
        <img 
          src={video.thumbnail} 
          alt={video.title} 
          style={{ width: '100%', height: 'auto', display: 'block' }} 
        />
      </a>
      <div style={{ padding: '12px' }}>
        <a 
          href={videoUrl} 
          target="_blank" 
          rel="noopener noreferrer" 
          style={{ 
            textDecoration: 'none', 
            color: '#0f0f0f', 
            fontWeight: '600',
            fontSize: '16px',
            display: '-webkit-box',
            WebkitLineClamp: 2,
            WebkitBoxOrient: 'vertical',
            overflow: 'hidden'
          }}
        >
          {video.title}
        </a>
        <p style={{ color: '#606060', fontSize: '14px', margin: '8px 0 0 0' }}>
          {video.channelTitle}
        </p>
      </div>
    </div>
  );
};

export default YouTubeVideoCard;