import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { ArrowLeft, CheckCircle2 } from 'lucide-react';
import { apiGetQuestions } from '../utils/api';

export default function SoruCevapBankasi() {
  const navigate = useNavigate();
  const location = useLocation();
  const { certificateId, certificateName } = location.state || { certificateId: 1 };
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    async function loadQuestions() {
      try {
        const res = await apiGetQuestions(certificateId);
        if (!res) return; // redirected on 401
        const data = await res.json();

        if (res.ok) {
          setQuestions(data.questions || []);
        } else {
          setErrorMsg(data.error || 'Suallar yüklənərkən xəta baş verdi.');
        }
      } catch (err) {
        console.error("API error", err);
        setErrorMsg('Serverlə əlaqə saxlanıla bilmədi.');
      } finally {
        setLoading(false);
      }
    }
    loadQuestions();
  }, [certificateId]);

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out]">
      <div className="flex items-center gap-4 mb-8 border-b border-white/10 pb-4">
        <button onClick={() => navigate(-1)} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
          <ArrowLeft size={24} />
        </button>
        <div>
          <h1 className="text-3xl font-bold">{certificateName || 'Sual-Cavab Bankı'}</h1>
          <p className="text-white/50 mt-1">Öyrənmək üçün bütün suallar və düzgün cavablar</p>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-12 text-white/70">Yüklənir...</div>
      ) : errorMsg ? (
        <div className="text-center py-12 text-red-400">{errorMsg}</div>
      ) : questions.length === 0 ? (
        <div className="text-center py-12 text-white/70">Bu sertifikat üçün sual tapılmadı.</div>
      ) : (
        <div className="space-y-4 max-h-[60vh] overflow-y-auto pr-2 custom-scrollbar">
          {questions.map((qa, index) => {
            const correctAnswerText = qa.options[qa.correct_answer];
            return (
              <div key={qa.id || index} className="glass p-5 rounded-xl border border-white/5">
                <div className="flex gap-4">
                  <div className="font-bold text-primary text-xl opacity-50">{(index + 1).toString().padStart(2, '0')}</div>
                  <div className="flex-1">
                    <h3 className="text-lg font-medium mb-3">{qa.question}</h3>
                    {qa.image_url && (
                      <div className="mb-4 max-w-sm rounded-lg overflow-hidden border border-white/10 bg-black/30 p-2">
                        <img src={qa.image_url} alt="Sual şəkli" className="max-h-52 rounded object-contain" />
                      </div>
                    )}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mb-3">
                      {Object.entries(qa.options).map(([key, value]) => (
                         <div key={key} className="text-sm text-white/70 bg-white/5 p-2 rounded border border-white/5">
                           <strong>{key})</strong> {value}
                         </div>
                      ))}
                    </div>
                    <div className="flex items-center gap-2 text-green-400 bg-green-500/10 px-3 py-2 rounded-lg inline-flex">
                      <CheckCircle2 size={18} />
                      <span><strong>Düzgün Cavab:</strong> {qa.correct_answer}) {correctAnswerText}</span>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
