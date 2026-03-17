import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../api';

export const fetchTrails = createAsyncThunk('trails/fetchTrails', async (params) => {
  const response = await api.get('/trails/', { params });
  return response.data;
});

export const likeTrail = createAsyncThunk('trails/likeTrail', async (id) => {
  const response = await api.post(`/trails/${id}/like/`);
  return response.data;
});

const trailsSlice = createSlice({
  name: 'trails',
  initialState: { items: [], loading: false },
  extraReducers: (builder) => {
    builder
      .addCase(fetchTrails.pending, (state) => { state.loading = true; })
      .addCase(fetchTrails.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(likeTrail.fulfilled, (state, action) => {
        const updated = action.payload;
        const index = state.items.findIndex(t => t.id === updated.id);
        if (index !== -1) state.items[index] = updated;
      });
  },
});

export default trailsSlice.reducer;
