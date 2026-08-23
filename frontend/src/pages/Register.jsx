import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Ship, UserPlus, AlertCircle, KeyRound, CheckCircle2 } from 'lucide-react';
import { apiRegister, apiVerifyEmail, saveTokens } from '../utils/api';

export default function Register() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Email verification step states
   // 1: Register Info, 2: Verification Code OTP
  
  

  const handleRegisterSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    if (password.length < 8) {
      setError('Şifrə ən azı 8 simvol olmalıdır.');
      setLoading(false);
      return;
    }

    try {
      const res = await apiRegister(username, email, password);
      const data = await res.json();

      if (res.ok) {
        // Direct Registration Success -> Save tokens and login
        saveTokens(data.access, data.refresh);
        if (data.user) {
          localStorage.setItem('user', JSON.stringify(data.user));
        }
        navigate('/menu');
      } else {
        setError(data.error || 'Qeydiyyat zamanı xəta baş verdi.');
      }
    } catch (err) {
      console.error(err);
      setError('Serverlə əlaqə saxlanıla bilmədi.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto glass-card p-8 animate-[fadeIn_0.5s_ease-out]">
      <div className="text-center mb-8">
        <div className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-primary/10 border border-primary/30 p-1 mb-4 shadow-[0_0_25px_rgba(16,185,129,0.3)]">
          <img src="/seapass_logo.jpg" alt="SeaPass Logo" className="w-full h-full object-cover rounded-xl" />
        </div>
        <h1 className="text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 tracking-tight">SeaPass</h1>
        <p className="text-white/60 text-sm mt-1 font-medium">
          Yeni hesab yaradın
        </p>
      </div>

      {error && (
        <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-3">
          <AlertCircle size={20} className="flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      

      <form onSubmit={handleRegisterSubmit} className="space-y-4">
            
            <div className="bg-yellow-500/20 text-yellow-200 p-3 rounded-lg text-sm mb-4 border border-yellow-500/30 flex items-start gap-2">
              <AlertCircle size={20} className="shrink-0 mt-0.5" />
              <p>Zəhmət olmasa <strong>öz şəxsi və həqiqi e-poçt ünvanınızla</strong> qeydiyyatdan keçin. Hər e-poçtla yalnız 1 dəfə qeydiyyatdan keçmək mümkündür. Gələcəkdə şifrənizi unutsanız və ya ödəniş etsəniz, hesabınızı bərpa etmək üçün bu e-poçt mütləq lazımdır!</p>
            </div>

            <div>
              <label className="block text-sm font-medium text-white/70 mb-1">İstifadəçi Adı</label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-white/40">
                  <UserPlus size={18} />
                </div>
                <input 
                  type="text" 
                  placeholder="İstifadəçi adınızı təyin edin" 
                  className="input-glass pl-10"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required 
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-white/70 mb-1">E-poçt Ünvanı</label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-white/40">
                  <Ship size={18} />
                </div>
                <input 
                  type="email" 
                  placeholder="E-poçt ünvanınız" 
                  className="input-glass pl-10"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required 
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-white/70 mb-1">Şifrə (Ən azı 8 simvol)</label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-white/40">
                  <KeyRound size={18} />
                </div>
                <input 
                  type="password" 
                  placeholder="Şifrənizi təyin edin" 
                  className="input-glass pl-10"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  minLength={8}
                  required 
                />
              </div>
            </div>

            <button 
              type="submit" 
              className="btn-primary w-full mt-6"
              disabled={loading}
            >
              {loading ? 'Qeydiyyat gedir...' : 'Qeydiyyatdan Keç'}
            </button>
          </form>

      <div className="mt-6 text-center text-sm text-white/50">
        Artıq hesabınız var?{' '}
        <Link to="/login" className="text-secondary hover:text-white transition-colors font-medium">
          Daxil olun
        </Link>
      </div>
    </div>
  );
}
