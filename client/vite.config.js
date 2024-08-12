import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5000, // Set the port for development server
    host: '0.0.0.0',
  },
  preview: {
    port: 3000, // Set the port for preview server
    host: '0.0.0.0',
  },
})
