import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { User, Mail, ArrowLeft, Shield, AlertCircle, CheckCircle2, History, Award } from 'lucide-react';
import { apiChangePassword } from '../utils/api';

export default function Profile() {
  const navigate = useNavigate();
  const [showPasswordForm, setShowPasswordForm] = useState(false);
  const [passwordSuccess, setPasswordSuccess] = useState(false);
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [loading, setLoading] = useState(false);

  const [testHistory, setTestHistory] = useState([]);

  const savedUser = JSON.parse(localStorage.getItem('user') || '{}');
  const username = savedUser.username || 'İstifadəçi';
  const email = savedUser.email || 'Məlumat yoxdur';

  useEffect(() => {
    // Retrieve last 3 test history items specifically for this logged in user
    const userKey = savedUser.id ? `test_history_${savedUser.id}` : 'test_history_guest';
    const savedHistory = JSON.parse(localStorage.getItem(userKey) || '[]');
    setTestHistory(savedHistory.slice(0, 3));
  }, [savedUser.id]);

  const handlePasswordSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg('');

    if (newPassword.length < 8) {
      setErrorMsg('Yeni şifrə ən azı 8 simvol olmalıdır.');
      return;
    }

    if (newPassword !== confirmPassword) {
      setErrorMsg('Yeni şifrə və təkrarı uyğun gəlmir!');
      return;
    }

    setLoading(true);

    try {
      const res = await apiChangePassword(oldPassword, newPassword);
      if (!res) return;
      const data = await res.json();

      if (res.ok) {
        setPasswordSuccess(true);
        setOldPassword('');
        setNewPassword('');
        setConfirmPassword('');
        setTimeout(() => {
          setPasswordSuccess(false);
          setShowPasswordForm(false);
        }, 3000);
      } else {
        setErrorMsg(data.error || 'Şifrə dəyişdirilərkən xəta baş verdi.');
      }
    } catch (err) {
      console.error(err);
      setErrorMsg('Serverlə əlaqə saxlanıla bilmədi.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out] max-w-3xl mx-auto">
      {/* Top Header */}
      <div className="flex items-center gap-4 mb-8 border-b border-white/10 pb-4">
        <button onClick={() => navigate('/menu')} className="p-2 hover:bg-white/10 rounded-lg transition-colors cursor-pointer">
          <ArrowLeft size={24} />
        </button>
        <div>
          <h1 className="text-3xl font-bold">Profil Ayarları</h1>
          <p className="text-white/50 mt-1">İstifadəçi məlumatlarınız və imtahan tarixçəsi</p>
        </div>
      </div>

      <div className="space-y-6">
        {/* User Card */}
        <div className="glass p-6 rounded-2xl border border-white/10 flex items-center gap-6">
          <div className="w-20 h-20 rounded-full bg-gradient-to-tr from-primary to-secondary flex items-center justify-center shadow-lg flex-shrink-0">
            <User size={40} className="text-white" />
          </div>
          <div className="space-y-1">
            <h2 className="text-2xl font-bold">{username}</h2>
            <div className="flex items-center gap-2 text-white/60 text-sm">
              <Mail size={16} />
              <span>{email}</span>
            </div>
          </div>
        </div>

        {/* Test History Section (Last 3 tests) */}
        <div className="glass p-6 rounded-2xl border border-white/10">
          <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
            <History size={20} className="text-secondary" />
            Son İmtahan Tarixçəsi (Son 3 Test)
          </h3>

          {testHistory.length === 0 ? (
            <p className="text-white/40 text-sm italic py-2">Hələ ki keçirilmiş imtahan tarixçəsi yoxdur.</p>
          ) : (
            <div className="space-y-3">
              {testHistory.map((item) => (
                <div key={item.id} className="bg-white/5 border border-white/10 p-4 rounded-xl flex items-center justify-between gap-4 hover:bg-white/10 transition-colors">
                  <div className="min-w-0 flex-1">
                    <h4 className="font-semibold text-white truncate">{item.certificateName}</h4>
                    <p className="text-xs text-white/50 mt-0.5">{item.date}</p>
                  </div>

                  <div className="flex items-center gap-4 flex-shrink-0">
                    <div className="text-right">
                      <span className="text-sm font-bold text-white block">{item.correct} / {item.total} Düzgün</span>
                      <span className="text-xs text-white/50">Nəticə</span>
                    </div>
                    <div className={`px-3 py-1.5 rounded-lg text-sm font-bold border ${
                      item.percentage >= 70 
                        ? 'bg-green-500/20 text-green-400 border-green-500/30' 
                        : 'bg-red-500/20 text-red-400 border-red-500/30'
                    }`}>
                      {item.percentage}%
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Security / Password Section */}
        <div className="glass p-6 rounded-2xl border border-white/10">
          <h3 className="text-xl font-bold mb-2 flex items-center gap-2">
            <Shield size={20} className="text-primary" />
            Hesab Təhlükəsizliyi
          </h3>
          <p className="text-white/50 text-sm mb-6">Şifrənizi müntəzəm olaraq yeniləməyiniz tövsiyə olunur.</p>

          {passwordSuccess ? (
            <div className="bg-emerald-500/20 text-emerald-400 p-4 rounded-xl border border-emerald-500/30 flex items-center gap-2">
              <CheckCircle2 size={20} />
              <span>Şifrəniz uğurla dəyişdirildi!</span>
            </div>
          ) : showPasswordForm ? (
            <form onSubmit={handlePasswordSubmit} className="space-y-4 bg-black/20 p-5 rounded-xl border border-white/10">
              {errorMsg && (
                <div className="p-3 rounded-lg bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-2">
                  <AlertCircle size={16} />
                  <span>{errorMsg}</span>
                </div>
              )}
              <div>
                <label className="block text-sm text-white/70 mb-1 font-medium">Cari Şifrə</label>
                <input 
                  type="password" 
                  placeholder="••••••••" 
                  className="w-full bg-black/30 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-primary transition-colors"
                  value={oldPassword}
                  onChange={(e) => setOldPassword(e.target.value)}
                  required
                />
              </div>
              <div>
                <label className="block text-sm text-white/70 mb-1 font-medium">Yeni Şifrə (min. 8 simvol)</label>
                <input 
                  type="password" 
                  placeholder="••••••••" 
                  className="w-full bg-black/30 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-primary transition-colors"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  required
                  minLength={8}
                />
              </div>
              <div>
                <label className="block text-sm text-white/70 mb-1 font-medium">Yeni Şifrə (Təkrar)</label>
                <input 
                  type="password" 
                  placeholder="••••••••" 
                  className="w-full bg-black/30 border border-white/10 rounded-lg p-3 text-white focus:outline-none focus:border-primary transition-colors"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  required
                  minLength={8}
                />
              </div>
              <div className="flex gap-3 pt-3">
                <button 
                  type="submit"
                  disabled={loading}
                  className="btn btn-primary flex-1 disabled:opacity-50"
                >
                  {loading ? 'Yadda saxlanılır...' : 'Yadda Saxla'}
                </button>
                <button 
                  type="button"
                  onClick={() => {
                    setShowPasswordForm(false);
                    setErrorMsg('');
                  }}
                  className="btn bg-white/10 hover:bg-white/20 flex-1"
                >
                  Ləğv Et
                </button>
              </div>
            </form>
          ) : (
            <button 
              onClick={() => setShowPasswordForm(true)}
              className="btn btn-secondary cursor-pointer"
            >
              Şifrəni Dəyiş
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
