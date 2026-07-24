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
  const [step, setStep] = useState(1); // 1: Register Info, 2: Verification Code OTP
  const [verificationCode, setVerificationCode] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleRegisterSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (password.length < 8) {
      setError('Şifrə ən azı 8 simvol olmalıdır.');
      return;
    }

    setLoading(true);

    try {
      const res = await apiRegister(username, email, password);
      const data = await res.json();

      if (res.ok) {
        setSuccessMessage(data.message);
        setStep(2); // Move to OTP confirmation screen
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

  const handleVerifyOtpSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const res = await apiVerifyEmail(email, verificationCode);
      const data = await res.json();

      if (res.ok) {
        saveTokens(data.access, data.refresh);
        if (data.user) {
          localStorage.setItem('user', JSON.stringify(data.user));
        }
        navigate('/menu');
      } else {
        setError(data.error || 'Təsdiq kodu yanlışdır.');
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
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-secondary/20 text-secondary mb-4 shadow-[0_0_20px_rgba(59,130,246,0.2)]">
          <Ship size={32} />
        </div>
        <h1 className="text-3xl font-bold text-white">Qeydiyyat</h1>
        <p className="text-white/50 mt-2">
          {step === 1 ? 'Yeni hesab yaradın' : 'E-poçt ünvanınızı təsdiqləyin'}
        </p>
      </div>

      {error && (
        <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-3">
          <AlertCircle size={20} className="flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {successMessage && (
        <div className="mb-6 p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-sm flex items-center gap-3">
          <CheckCircle2 size={20} className="flex-shrink-0" />
          <span>{successMessage}</span>
        </div>
      )}

      {step === 1 ? (
        /* STEP 1: QEYDİYYAT MƏLUMATLARININ DAXİL EDİLMƏSİ */
        <form onSubmit={handleRegisterSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-white/70 mb-1">İstifadəçi adı</label>
            <input 
              type="text" 
              className="input-glass" 
              placeholder="istifadəçi adı"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required 
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-white/70 mb-1">E-poçt</label>
            <input 
              type="email" 
              className="input-glass" 
              placeholder="nümunə@mail.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required 
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-white/70 mb-1 font-medium">Şifrə (min. 8 simvol)</label>
            <input 
              type="password" 
              className="input-glass" 
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required 
              minLength={8}
            />
          </div>
          
          <button 
            type="submit" 
            disabled={loading}
            className="w-full btn bg-secondary hover:bg-secondary/80 text-white shadow-[0_0_15px_rgba(59,130,246,0.3)] mt-6 flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer"
          >
            <UserPlus size={20} />
            {loading ? 'Kod Göndərilir...' : 'Təsdiq Kodu Göndər'}
          </button>
        </form>
      ) : (
        /* STEP 2: GMAIL OTP TƏSDİQLƏMƏ */
        <form onSubmit={handleVerifyOtpSubmit} className="space-y-4">
          <div className="bg-white/5 p-4 rounded-xl border border-white/10 text-center mb-4">
            <p className="text-xs text-white/60">
              Biz <strong>{email}</strong> ünvanına 6 rəqəmli doğrulama kodu göndərdik. Zəhmət olmasa daxil edin.
            </p>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-white/70 mb-1 text-center font-bold">6 Rəqəmli Təsdiq Kodu</label>
            <input 
              type="text" 
              maxLength={6}
              placeholder="123456" 
              className="input-glass text-center text-2xl font-bold tracking-[0.5em] focus:tracking-[0.5em]"
              value={verificationCode}
              onChange={(e) => setVerificationCode(e.target.value.replace(/\D/g, ''))}
              required 
            />
          </div>

          <button 
            type="submit" 
            disabled={loading}
            className="w-full btn bg-emerald-500 hover:bg-emerald-600 text-black font-black mt-6 flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer"
          >
            <KeyRound size={20} />
            {loading ? 'Hesab Aktivləşdirilir...' : 'Hesabı Aktivləşdir Və Giriş Et'}
          </button>

          <button 
            type="button" 
            onClick={() => {
              setStep(1);
              setSuccessMessage('');
              setVerificationCode('');
            }}
            className="w-full btn bg-white/10 hover:bg-white/20 text-white mt-2 cursor-pointer text-xs"
          >
            Məlumatları düzəlt
          </button>
        </form>
      )}

      <div className="mt-6 text-center text-sm text-white/50">
        Artıq hesabınız var?{' '}
        <Link to="/login" className="text-secondary hover:text-white transition-colors font-medium">
          Daxil olun
        </Link>
      </div>
    </div>
  );
}
