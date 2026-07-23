import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { FileBadge, ArrowLeft, Play, Database, Shuffle } from 'lucide-react';
import { apiGetCertificates } from '../utils/api';

export default function SertifikatSecimi() {
  const navigate = useNavigate();
  const location = useLocation();
  const { categoryId, categoryName } = location.state || {};
  
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isShuffle, setIsShuffle] = useState(false);

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

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out]">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8 border-b border-white/10 pb-4">
        <div className="flex items-center gap-4">
          <button onClick={() => navigate('/type-selection')} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
            <ArrowLeft size={24} />
          </button>
          <div>
            <h1 className="text-3xl font-bold">Sertifikat Seçimi</h1>
            <p className="text-white/50 mt-1">{categoryName ? `${categoryName} üçün sertifikatlar` : 'Test və ya Sual-Cavab bankı üçün sertifikat seçin'}</p>
          </div>
        </div>

        {/* Karıştır Button */}
        <button
          onClick={() => setIsShuffle(!isShuffle)}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl border text-sm font-semibold transition-all duration-300 ${
            isShuffle 
              ? 'bg-primary/20 border-primary text-primary shadow-lg shadow-primary/20 ring-2 ring-primary/30' 
              : 'bg-white/5 border-white/10 text-white/70 hover:bg-white/10 hover:text-white'
          }`}
        >
          <Shuffle size={18} className={isShuffle ? 'animate-spin-slow text-primary' : ''} />
          <span>Qarışdır</span>
          {isShuffle && <span className="text-xs bg-primary text-black px-1.5 py-0.5 rounded font-bold ml-1">Aktiv</span>}
        </button>
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
              
              <div className="flex flex-col sm:flex-row gap-3 w-full lg:w-auto flex-shrink-0">
                <button 
                  onClick={() => navigate('/qa-bank', { state: { certificateId: cert.id, certificateName: cert.name } })}
                  className="flex-1 sm:flex-none btn btn-secondary flex items-center justify-center gap-2 px-4 py-2 text-sm"
                >
                  <Database size={16} />
                  Sual Bankı
                </button>
                <button 
                  onClick={() => navigate('/test', { state: { certificateId: cert.id, certificateName: cert.name, isShuffle } })}
                  className="flex-1 sm:flex-none btn btn-primary flex items-center justify-center gap-2 px-4 py-2 text-sm whitespace-nowrap"
                >
                  <Play size={16} />
                  Testə Başla
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
