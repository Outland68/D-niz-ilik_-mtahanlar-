import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { FileBadge, ArrowLeft, Play, Database, Shuffle, Timer, Settings2 } from 'lucide-react';
import { apiGetCertificates } from '../utils/api';

export default function SertifikatSecimi() {
  const navigate = useNavigate();
  const location = useLocation();
  const { categoryId, categoryName } = location.state || {};
  
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);

  const [isShuffle, setIsShuffle] = useState(true);

  // Exam Modal State
  const [selectedCert, setSelectedCert] = useState(null);
  const [examMode, setExamMode] = useState('classic'); // 'classic' (20 q), 'custom'
  const [customCount, setCustomCount] = useState(20);

  useEffect(() => {
    apiGetCertificates(categoryId)
      .then(res => res.json())
      .then(data => {
        setCertificates(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("API error", err);
        setLoading(false);
      });
  }, [categoryId]);

  const handleStartRealExam = () => {
    if (!selectedCert) return;
    navigate('/real-exam', {
      state: {
        certificateId: selectedCert.id,
        certificateName: selectedCert.name,
        isClassic: examMode === 'classic',
        customCount: parseInt(customCount, 10) || 20,
        isShuffle: isShuffle
      }
    });
  };

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out] relative">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8 border-b border-white/10 pb-4">
        <div className="flex items-center gap-4">
          <button onClick={() => navigate('/type-selection')} className="p-2 hover:bg-white/10 rounded-lg transition-colors cursor-pointer">
            <ArrowLeft size={24} />
          </button>
          <div>
            <h1 className="text-3xl font-bold">Sertifikat Seçimi</h1>
            <p className="text-white/50 mt-1">{categoryName ? `${categoryName} üçün sertifikatlar` : 'İmtahan və ya Sual Bankı üçün sertifikat seçin'}</p>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-12 text-white/50">Yüklənir...</div>
      ) : certificates.length === 0 ? (
        <div className="text-center py-12 text-white/50">Bu kateqoriyada sertifikat tapılmadı.</div>
      ) : (
        <div className="space-y-4 max-h-[75vh] overflow-y-auto pr-2 custom-scrollbar">
          {certificates.map(cert => (
            <div key={cert.id} className="glass p-5 rounded-xl flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 hover:bg-white/5 transition-colors">
              <div className="flex items-center gap-4 flex-1 w-full">
                <div className="w-12 h-12 rounded-lg bg-primary/20 text-primary flex-shrink-0 flex items-center justify-center">
                  <FileBadge size={24} />
                </div>
                <div className="flex-1 min-w-0">
                  <h3 className="text-lg font-bold break-words leading-tight">{cert.name}</h3>
                  <p className="text-sm text-white/50 mt-1">{cert.question_count} Sual</p>
                </div>
              </div>
              
              <div className="flex flex-col sm:flex-row gap-2.5 w-full lg:w-auto flex-shrink-0">
                <button 
                  onClick={() => navigate('/qa-bank', { state: { certificateId: cert.id, certificateName: cert.name } })}
                  className="flex-1 sm:flex-none btn btn-secondary flex items-center justify-center gap-2 px-3.5 py-2 text-xs font-semibold cursor-pointer"
                >
                  <Database size={15} />
                  Sual Bankı
                </button>
                <button 
                  onClick={() => navigate('/test', { state: { certificateId: cert.id, certificateName: cert.name } })}
                  className="flex-1 sm:flex-none btn bg-white/10 hover:bg-white/20 text-white flex items-center justify-center gap-2 px-3.5 py-2 text-xs font-semibold cursor-pointer"
                >
                  <Play size={15} />
                  Təcrübə Testi
                </button>
                <button 
                  onClick={() => {
                    setSelectedCert(cert);
                    setExamMode('classic');
                    setCustomCount(Math.min(20, cert.question_count || 20));
                  }}
                  className="flex-1 sm:flex-none btn btn-primary flex items-center justify-center gap-2 px-4 py-2 text-xs font-bold whitespace-nowrap shadow-lg shadow-primary/20 cursor-pointer"
                >
                  <Timer size={16} />
                  İmtahana Başla (30 dəq)
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Real Exam Configuration Modal */}
      {selectedCert && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 p-4 animate-[fadeIn_0.2s_ease-out]">
          <div className="glass-card w-full max-w-lg p-6 border border-white/15 shadow-2xl relative">
            <div className="flex items-center justify-between mb-6 border-b border-white/10 pb-4">
              <div className="flex items-center gap-3">
                <div className="p-3 bg-amber-500/20 text-amber-400 rounded-xl">
                  <Timer size={24} />
                </div>
                <div>
                  <h2 className="text-xl font-bold">İmtahan Tənzimləmələri</h2>
                  <p className="text-xs text-white/50 truncate max-w-xs">{selectedCert.name}</p>
                </div>
              </div>
              <button 
                onClick={() => setSelectedCert(null)}
                className="text-white/50 hover:text-white text-lg font-bold px-2 cursor-pointer"
              >
                ✕
              </button>
            </div>

            <div className="space-y-5 mb-6">
              {/* Exam Mode Selection */}
              <div>
                <label className="block text-sm font-semibold text-white/80 mb-3 flex items-center gap-2">
                  <Settings2 size={16} className="text-primary" /> İmtahan Rejimi Seçin:
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <button
                    onClick={() => setExamMode('classic')}
                    className={`p-4 rounded-xl border text-left transition-all cursor-pointer ${
                      examMode === 'classic'
                        ? 'border-primary bg-primary/20 text-white shadow-lg ring-2 ring-primary/30'
                        : 'border-white/10 bg-white/5 text-white/70 hover:bg-white/10'
                    }`}
                  >
                    <div className="font-bold text-sm mb-1 text-primary">Klassik DDLA İmtahanı</div>
                    <div className="text-xs opacity-75">20 Sual • 30 Dəqiqə • Keçid: 14/20 (70%)</div>
                  </button>

                  <button
                    onClick={() => setExamMode('custom')}
                    className={`p-4 rounded-xl border text-left transition-all cursor-pointer ${
                      examMode === 'custom'
                        ? 'border-primary bg-primary/20 text-white shadow-lg ring-2 ring-primary/30'
                        : 'border-white/10 bg-white/5 text-white/70 hover:bg-white/10'
                    }`}
                  >
                    <div className="font-bold text-sm mb-1 text-secondary">Sərbəst Sual Seçimi</div>
                    <div className="text-xs opacity-75">Sual sayını özünüz seçin • 30 Dəqiqə</div>
                  </button>
                </div>
              </div>

              {/* Custom Count Input */}
              {examMode === 'custom' && (
                <div className="bg-white/5 p-4 rounded-xl border border-white/10 animate-[fadeIn_0.2s_ease-out]">
                  <label className="block text-sm font-medium text-white/80 mb-2">
                    Göstəriləcək Sual Sayı (Mövcud: {selectedCert.question_count} sual)
                  </label>
                  <input
                    type="number"
                    min="1"
                    max={selectedCert.question_count || 100}
                    value={customCount}
                    onChange={(e) => setCustomCount(e.target.value)}
                    className="input-glass w-full text-lg font-bold text-center"
                  />
                </div>
              )}

              {/* Shuffle Questions Toggle */}
              <div className="flex items-center justify-between p-3.5 bg-white/5 rounded-xl border border-white/10">
                <div className="flex items-center gap-2 text-sm font-semibold">
                  <Shuffle size={18} className={isShuffle ? 'text-primary animate-spin-slow' : 'text-white/50'} />
                  <span>Sualları Sıra İlə Qarışdır</span>
                </div>
                <button
                  type="button"
                  onClick={() => setIsShuffle(!isShuffle)}
                  className={`w-12 h-6 flex items-center rounded-full p-1 cursor-pointer transition-colors duration-300 ${
                    isShuffle ? 'bg-primary justify-end' : 'bg-white/20 justify-start'
                  }`}
                >
                  <div className="w-4 h-4 rounded-full bg-black shadow-md"></div>
                </button>
              </div>
            </div>

            <div className="flex gap-3">
              <button 
                onClick={handleStartRealExam}
                className="btn btn-primary flex-1 py-3 text-base font-bold flex items-center justify-center gap-2 shadow-lg cursor-pointer"
              >
                <Play size={18} />
                İmtahanı Başlat (30 dəq)
              </button>
              <button 
                onClick={() => setSelectedCert(null)}
                className="btn bg-white/10 hover:bg-white/20 flex-1 py-3 cursor-pointer"
              >
                Ləğv Et
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
