import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Adjust if backend runs on a different port

const api = axios.create({
    baseURL: API_BASE_URL,
});

export const boqService = {
    extract: async (file, industry = 'construction') => {
        const formData = new FormData();
        formData.append('file', file);

        const response = await api.post(`/extract?industry=${industry}`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    },

    uploadRaw: async (file) => {
        const formData = new FormData();
        formData.append('file', file);

        const response = await api.post('/upload-excel', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    },
};
