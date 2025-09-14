import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Allows your Vite dev server to be accessed by your ngrok URL
    allowedHosts: [
      'kpr-hackathon-st79zzkrj-agilessshobika-gmailcoms-projects.vercel.app' 
    ],
    proxy: {
  "/api": {
    target: "https://mall-backend-vlie.onrender.com",
    changeOrigin: true,
    secure: false,
  },
}

  }
})
