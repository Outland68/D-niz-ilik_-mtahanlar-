import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Ship, LogIn, AlertCircle, KeyRound, CheckCircle2, Mail, Lock } from 'lucide-react';
import { apiLogin, apiSendResetCode, apiVerifyResetCode, saveTokens } from '../utils/api';

export default function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Forgot password modal state (Step 1: enter email -> Step 2: enter code & new pass)
  const [showForgotModal, setShowForgotModal] = useState(false);
  const [step, setStep] = useState(1); // 1: Send email, 2: Verify code
  const [forgotEmail, setForgotEmail] = useState('');
  const [forgotCode, setForgotCode] = useState('');
  const [forgotNewPassword, setForgotNewPassword] = useState('');
  const [forgotConfirmPassword, setForgotConfirmPassword] = useState('');
  const [forgotError, setForgotError] = useState('');
  const [forgotSuccess, setForgotSuccess] = useState('');
  const [forgotLoading, setForgotLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const res = await apiLogin(username, password);
      const data = await res.json();

      if (res.ok) {
        saveTokens(data.access, data.refresh);
        if (data.user) {
          localStorage.setItem('user', JSON.stringify(data.user));
        }
        navigate('/menu');
      } else {
        setError(data.error || 'Daxil olarkən xəta baş verdi.');
      }
    } catch (err) {
      console.error(err);
      setError('Serverlə əlaqə saxlanıla bilmədi.');
    } finally {
      setLoading(false);
    }
  };

  // STEP 1: Send OTP code to Email
  const handleSendCode = async (e) => {
    e.preventDefault();
    setForgotError('');
    setForgotSuccess('');
    setForgotLoading(true);

    try {
      const res = await apiSendResetCode(forgotEmail);
      const data = await res.json();

      if (res.ok) {
        setForgotSuccess(data.message);
        setTimeout(() => {
          setForgotSuccess('');
          setStep(2);
        }, 1500);
      } else {
        setForgotError(data.error || 'Kod göndərilərkən xəta baş verdi.');
      }
    } catch (err) {
      console.error(err);
      setForgotError('Serverlə əlaqə saxlanıla bilmədi.');
    } finally {
      setForgotLoading(false);
    }
  };

  // STEP 2: Verify OTP code & Set new password
  const handleVerifyAndReset = async (e) => {
    e.preventDefault();
    setForgotError('');
    setForgotSuccess('');

    if (forgotNewPassword.length < 8) {
      setForgotError('Yeni şifrə ən azı 8 simvol olmalıdır.');
      return;
    }

    if (forgotNewPassword !== forgotConfirmPassword) {
      setForgotError('Yeni şifrələr üst-üstə düşmür!');
      return;
    }

    setForgotLoading(true);

    try {
      const res = await apiVerifyResetCode(forgotEmail, forgotCode, forgotNewPassword);
      const data = await res.json();

      if (res.ok) {
        setForgotSuccess(data.message || 'Şifrəniz uğurla yeniləndi!');
        setTimeout(() => {
          setShowForgotModal(false);
          setStep(1);
          setForgotSuccess('');
          setForgotEmail('');
          setForgotCode('');
          setForgotNewPassword('');
          setForgotConfirmPassword('');
        }, 2500);
      } else {
        setForgotError(data.error || 'Təsdiq kodu yanlışdır.');
      }
    } catch (err) {
      console.error(err);
      setForgotError('Serverlə əlaqə saxlanıla bilmədi.');
    } finally {
      setForgotLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto glass-card p-8 animate-[fadeIn_0.5s_ease-out]">
      <div className="text-center mb-8">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary/20 text-primary mb-4 shadow-[0_0_20px_rgba(16,185,129,0.2)]">
          <Ship size={32} />
        </div>
        <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-white/70">Dənizçilik İmtahanları</h1>
        <p className="text-white/50 mt-2">Sistemə daxil olun</p>
      </div>

      {error && (
        <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-3">
          <AlertCircle size={20} className="flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      <form onSubmit={handleLogin} className="space-y-4">
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
          <div className="flex items-center justify-between mb-1">
            <label className="block text-sm font-medium text-white/70">Şifrə</label>
            <button 
              type="button" 
              onClick={() => {
                setShowForgotModal(true);
                setStep(1);
                setForgotError('');
                setForgotSuccess('');
              }}
              className="text-xs text-primary hover:underline transition-all"
            >
              Şifrəmi unutmuşam?
            </button>
          </div>
          <input 
            type="password" 
            className="input-glass"
            placeholder="••••••••"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        
        <button 
          type="submit" 
          disabled={loading}
          className="w-full btn btn-primary flex items-center justify-center gap-2 mt-6 disabled:opacity-50"
        >
          <LogIn size={20} />
          {loading ? 'Daxil olunur...' : 'Daxil ol'}
        </button>
      </form>

      <div className="mt-6 text-center text-sm text-white/50">
        Hesabınız yoxdur?{' '}
        <Link to="/register" className="text-primary hover:text-primary-dark transition-colors font-medium">
          Qeydiyyatdan keçin
        </Link>
      </div>

      {/* Gmail OTP Reset Modal */}
      {showForgotModal && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-md flex items-center justify-center z-50 p-4 animate-[fadeIn_0.2s_ease-out]">
          <div className="glass-card w-full max-w-md p-6 border border-white/10 shadow-2xl relative">
            <div className="flex items-center justify-between mb-6 border-b border-white/10 pb-3">
              <h2 className="text-xl font-bold flex items-center gap-2">
                <KeyRound size={22} className="text-primary" />
                {step === 1 ? 'E-poçt İlə Təsdiq Kodu' : 'Şifrəni Yenilə'}
              </h2>
              <button 
                onClick={() => setShowForgotModal(false)}
                className="text-white/50 hover:text-white text-lg font-bold px-2"
              >
                ✕
              </button>
            </div>

            {forgotSuccess && (
              <div className="mb-4 p-4 rounded-xl bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-sm flex items-center gap-3">
                <CheckCircle2 size={24} className="flex-shrink-0" />
                <span>{forgotSuccess}</span>
              </div>
            )}

            {forgotError && (
              <div className="mb-4 p-3 rounded-lg bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-2">
                <AlertCircle size={16} />
                <span>{forgotError}</span>
              </div>
            )}

            {/* STEP 1: Enter Email */}
            {step === 1 && (
              <form onSubmit={handleSendCode} className="space-y-4">
                <p className="text-sm text-white/60 mb-2">
                  Qeydiyyatdan keçdiyiniz e-poçt ünvanınızı daxil edin. Sizə 6 rəqəmli təsdiq kodu göndəriləcək.
                </p>
                <div>
                  <label className="block text-sm text-white/70 mb-1 font-medium flex items-center gap-1.5">
                    <Mail size={16} className="text-primary" /> E-poçt Ünvanı
                  </label>
                  <input 
                    type="email" 
                    placeholder="nümunə@mail.com"
                    className="input-glass"
                    value={forgotEmail}
                    onChange={(e) => setForgotEmail(e.target.value)}
                    required
                  />
                </div>

                <div className="flex gap-3 pt-2">
                  <button 
                    type="submit" 
                    disabled={forgotLoading}
                    className="btn btn-primary flex-1 disabled:opacity-50"
                  >
                    {forgotLoading ? 'Göndərilir...' : 'Təsdiq Kodunu Göndər'}
                  </button>
                  <button 
                    type="button"
                    onClick={() => setShowForgotModal(false)}
                    className="btn bg-white/10 hover:bg-white/20 flex-1"
                  >
                    Ləğv Et
                  </button>
                </div>
              </form>
            )}

            {/* STEP 2: Enter OTP Code and New Password */}
            {step === 2 && (
              <form onSubmit={handleVerifyAndReset} className="space-y-4">
                <p className="text-sm text-white/60 mb-2">
                  <strong className="text-primary">{forgotEmail}</strong> ünvanına göndərilmiş 6 rəqəmli kodu daxil edin:
                </p>
                <div>
                  <label className="block text-sm text-white/70 mb-1 font-medium">6 Rəqəmli Təsdiq Kodu</label>
                  <input 
                    type="text" 
                    placeholder="123456"
                    className="input-glass tracking-widest text-center text-xl font-mono font-bold"
                    maxLength={6}
                    value={forgotCode}
                    onChange={(e) => setForgotCode(e.target.value)}
                    autoComplete="one-time-code"
                    required
                  />
                </div>

                <div>
                  <label className="block text-sm text-white/70 mb-1 font-medium flex items-center gap-1.5">
                    <Lock size={16} className="text-primary" /> Yeni Şifrə (min. 8 simvol)
                  </label>
                  <input 
                    type="password" 
                    placeholder="••••••••"
                    className="input-glass"
                    value={forgotNewPassword}
                    onChange={(e) => setForgotNewPassword(e.target.value)}
                    required
                    minLength={8}
                  />
                </div>

                <div>
                  <label className="block text-sm text-white/70 mb-1 font-medium">Yeni Şifrə (Təkrar)</label>
                  <input 
                    type="password" 
                    placeholder="••••••••"
                    className="input-glass"
                    value={forgotConfirmPassword}
                    onChange={(e) => setForgotConfirmPassword(e.target.value)}
                    required
                    minLength={8}
                  />
                </div>

                <div className="flex gap-3 pt-2">
                  <button 
                    type="submit" 
                    disabled={forgotLoading}
                    className="btn btn-primary flex-1 disabled:opacity-50"
                  >
                    {forgotLoading ? 'Yenilənir...' : 'Şifrəni Dəyiş'}
                  </button>
                  <button 
                    type="button"
                    onClick={() => setStep(1)}
                    className="btn bg-white/10 hover:bg-white/20 flex-1"
                  >
                    Geri
                  </button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
