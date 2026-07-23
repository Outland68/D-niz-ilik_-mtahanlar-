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
      <div className="min-h-screen bg-gradient-to-br from-dark to-dark-paper text-light flex flex-col items-center justify-between p-4 relative overflow-x-hidden">
        {/* Decorative background circles for modern look */}
        <div className="fixed top-[-10%] left-[-10%] w-[40vw] h-[40vw] bg-primary/20 rounded-full blur-[120px] pointer-events-none"></div>
        <div className="fixed bottom-[-10%] right-[-10%] w-[40vw] h-[40vw] bg-secondary/20 rounded-full blur-[120px] pointer-events-none"></div>
        
        {/* Main Content Area */}
        <div className="w-full max-w-6xl z-10 my-auto py-6">
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

        {/* Global Footer Disclaimer Notice */}
        <footer className="w-full z-10 text-center py-4 border-t border-white/10 mt-auto bg-black/20 backdrop-blur-md rounded-t-2xl">
          <p className="text-xs text-white/50 max-w-4xl mx-auto px-4 leading-relaxed">
            ⚠️ <strong>Xəbərdarlıq / Disclaimer:</strong> Bu saytın Dövlət Dəniz və Liman Agentliyi (DDLA) ilə rəsmi bir əlaqəsi yoxdur. Saytdakı suallar DDLA tərəfindən ictimaiyyətə açıq şəkildə təqdim edilən imtahan sualları əsasında hazırlanmışdır.
          </p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
