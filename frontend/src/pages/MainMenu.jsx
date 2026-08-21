import { useNavigate } from 'react-router-dom';
import { authFetch } from '../utils/api';
import { useEffect, useState } from 'react';
import { BookOpen, Award, Settings, LogOut, User } from 'lucide-react';

export default function MainMenu() {
  
  const navigate = useNavigate();
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    authFetch('/auth/me/').then(user => {
      if (user && user.is_superuser) {
        setIsAdmin(true);
      }
    }).catch(() => {});
  }, []);


  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.5s_ease-out]">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 border-b border-white/10 pb-4 gap-4">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-xl bg-primary/10 border border-primary/30 p-0.5 flex-shrink-0 shadow-[0_0_15px_rgba(16,185,129,0.2)]">
            <img src="/seapass_logo.jpg" alt="SeaPass Logo" className="w-full h-full object-cover rounded-lg" />
          </div>
          <div>
            <h1 className="text-3xl sm:text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 tracking-tight">SeaPass</h1>
            <p className="text-white/50 text-xs mt-0.5 font-medium">Dənizçilik İmtahanları Portalı</p>
          </div>
        </div>
        <div className="flex gap-3">
          
          {isAdmin && (
            <button onClick={() => navigate('/admin-dashboard')} className="btn bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 border border-blue-500/30 flex items-center gap-2">
              <Settings size={18} />
              Admin
            </button>
          )}

          <button onClick={() => navigate('/profile')} className="btn bg-white/10 hover:bg-white/20 flex items-center gap-2">
            <User size={18} />
            Profil
          </button>
          <button onClick={() => navigate('/login')} className="btn btn-secondary flex items-center gap-2">
            <LogOut size={18} />
            Çıxış
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Növ Seçimi Card */}
        <div 
          onClick={() => navigate('/type-selection')}
          className="glass p-6 rounded-xl cursor-pointer hover:-translate-y-1 hover:shadow-2xl hover:bg-white/5 transition-all duration-300 group"
        >
          <div className="w-12 h-12 rounded-lg bg-primary/20 text-primary flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
            <BookOpen size={24} />
          </div>
          <h3 className="text-xl font-semibold mb-2">İmtahanlar</h3>
          <p className="text-white/50 text-sm">Növ seçimi edərək imtahanlara və sertifikatlara baxın.</p>
        </div>

        {/* Placeholder for other features */}
        <div className="glass p-6 rounded-xl cursor-pointer hover:-translate-y-1 hover:shadow-2xl hover:bg-white/5 transition-all duration-300 group opacity-50">
          <div className="w-12 h-12 rounded-lg bg-secondary/20 text-secondary flex items-center justify-center mb-4">
            <Award size={24} />
          </div>
          <h3 className="text-xl font-semibold mb-2">Mənim Nəticələrim</h3>
          <p className="text-white/50 text-sm">Keçmiş imtahan nəticələrinizə baxın. (Tezliklə)</p>
        </div>

        <div 
          onClick={() => navigate('/profile')}
          className="glass p-6 rounded-xl cursor-pointer hover:-translate-y-1 hover:shadow-2xl hover:bg-white/5 transition-all duration-300 group"
        >
          <div className="w-12 h-12 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
            <Settings size={24} />
          </div>
          <h3 className="text-xl font-semibold mb-2">Profil və Ayarlar</h3>
          <p className="text-white/50 text-sm">Şəxsi məlumatlarınızı və hesab ayarlarınızı idarə edin.</p>
        </div>
      </div>
    </div>
  );
}
