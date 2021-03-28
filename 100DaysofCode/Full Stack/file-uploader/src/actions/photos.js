import axios from 'axios';
import { BASE_API_URL } from '../utils/constants';
import { getErrors } from './errors';

// makes API call for uploading the image to the server.

export const beginAddPicture = (photo) => {
  return async (dispatch) => {
    try {
      const formData = new FormData();
      formData.append('photo', photo);
      await axios.post(`${BASE_API_URL}/photos`, formData, {
        headers: {
          // To handle the file upload, the content-type must be of multipart/form-data type.
          'Content-Type': 'multipart/form-data'
        }
      });
    } catch (error) {
      error.response && dispatch(getErrors(error.response.data));
    }
  };
};

export const startLoadPictures = () => {
  return async (dispatch) => {
    try {
      const photos = await axios.get(`${BASE_API_URL}/photos`);
      dispatch(loadPhotos(photos.data));
    } catch (error) {
      error.response && dispatch(getErrors(error.response.data));
    }
  };
};

export const loadPhotos = (photos) => ({
  type: 'LOAD_PHOTOS',
  photos
});