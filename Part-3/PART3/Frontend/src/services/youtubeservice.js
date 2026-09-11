import axios from 'axios';

const API_BASE_URL = 'http://localhost:8002/api/youtube';

export const fetchYouTubeVideos = async (query) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/search`, {
      params: {
        query,
        max_results: 6
      }
    });

    return response.data.videos;
  } catch (error) {
    console.error('Error fetching YouTube videos:', error);
    return [];
  }
};