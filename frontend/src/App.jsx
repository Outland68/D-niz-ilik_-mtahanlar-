import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import MainMenu from './pages/MainMenu';
import NovSecimi from './pages/NovSecimi';
import SertifikatSecimi from './pages/SertifikatSecimi';
import TestPage from './pages/TestPage';
import SoruCevapBankasi from './pages/SoruCevapBankasi';
import Profile from './pages/Profile';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-dark to-dark-paper text-light flex items-center justify-center p-4">
        {/* Decorative background circles for modern look */}
        <div className="fixed top-[-10%] left-[-10%] w-[40vw] h-[40vw] bg-primary/20 rounded-full blur-[120px] pointer-events-none"></div>
        <div className="fixed bottom-[-10%] right-[-10%] w-[40vw] h-[40vw] bg-secondary/20 rounded-full blur-[120px] pointer-events-none"></div>
        
        <div className="w-full max-w-6xl z-10 relative">
          <Routes>
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/menu" element={<MainMenu />} />
            <Route path="/type-selection" element={<NovSecimi />} />
            <Route path="/certificate-selection" element={<SertifikatSecimi />} />
            <Route path="/test" element={<TestPage />} />
            <Route path="/qa-bank" element={<SoruCevapBankasi />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
