import { configureStore } from '@reduxjs/toolkit';
import trailsReducer from './trailsSlice';
import authReducer from './authSlice';

export const store = configureStore({
  reducer: {
    trails: trailsReducer,
    auth: authReducer,
  },
});
