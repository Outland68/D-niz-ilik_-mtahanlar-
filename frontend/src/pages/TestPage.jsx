import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { 
  ArrowLeft, CheckCircle2, XCircle, Shuffle, RotateCcw, 
  Award, AlertTriangle, Eye, EyeOff, Flag, Check, X 
} from 'lucide-react';
import { apiGetQuestions, getImageUrl } from '../utils/api';

export default function TestPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { certificateId, certificateName, isShuffle: initialShuffle } = location.state || { certificateId: 1 };

  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState({}); // { qIndex: { selected: 'A', isCorrect: true/false } }
  const [isFinished, setIsFinished] = useState(false);
  const [showWrongOnlyModal, setShowWrongOnlyModal] = useState(false);

  useEffect(() => {
    async function loadQuestions() {
      try {
        const res = await apiGetQuestions(certificateId);
        if (!res) return;
        const data = await res.json();

        if (res.ok) {
          let list = data.questions || [];
          if (initialShuffle) {
            list = [...list].sort(() => Math.random() - 0.5);
          }
          setQuestions(list);
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
  }, [certificateId, initialShuffle]);

  const handleOptionSelect = (key) => {
    if (isFinished) return;
    const q = questions[currentQuestion];
    const optionKeys = Array.isArray(q.options) ? q.options.map((_, i) => ['A','B','C','D'][i] || i) : Object.keys(q.options || {});
    const correctKey = typeof q.correct_answer === 'number' ? (['A','B','C','D'][q.correct_answer] || q.correct_answer) : q.correct_answer;
    const isCorrect = String(key) === String(correctKey);

    setUserAnswers(prev => ({
      ...prev,
      [currentQuestion]: {
        selected: key,
        isCorrect: isCorrect
      }
    }));
  };

  const handleFinishTest = () => {
    setIsFinished(true);

    // Save test history scoped to user (max 3)
    const { correct, total, percentage } = calculateResults();
    const savedUser = JSON.parse(localStorage.getItem('user') || '{}');
    const userKey = savedUser.id ? `test_history_${savedUser.id}` : 'test_history_guest';

    const newEntry = {
      id: Date.now(),
      certificateName: certificateName || 'İmtahan Testi',
      date: new Date().toLocaleDateString('az-AZ', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }),
      correct,
      total,
      percentage
    };

    const existingHistory = JSON.parse(localStorage.getItem(userKey) || '[]');
    const updatedHistory = [newEntry, ...existingHistory].slice(0, 3);
    localStorage.setItem(userKey, JSON.stringify(updatedHistory));
  };

  const calculateResults = () => {
    let correct = 0;
    let wrong = 0;
    let unanswered = 0;

    questions.forEach((q, idx) => {
      const ans = userAnswers[idx];
      if (!ans) {
        unanswered++;
      } else if (ans.isCorrect) {
        correct++;
      } else {
        wrong++;
      }
    });

    const total = questions.length;
    const percentage = total > 0 ? Math.round((correct / total) * 100) : 0;

    return { correct, wrong, unanswered, total, percentage };
  };

  if (loading) {
    return <div className="text-center py-12 text-white/70">Yüklənir...</div>;
  }

  if (errorMsg) {
    return <div className="text-center py-12 text-red-400">{errorMsg}</div>;
  }

  if (questions.length === 0) {
    return <div className="text-center py-12 text-white/70">Bu sertifikat üçün sual tapılmadı.</div>;
  }

  // ─── RESULTS VIEW ─────────────────────────────────────────
  if (isFinished) {
    const { correct, wrong, unanswered, total, percentage } = calculateResults();
    const wrongQuestionsList = questions.map((q, idx) => ({ q, idx, ans: userAnswers[idx] }))
      .filter(item => item.ans && !item.ans.isCorrect);

    return (
      <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out]">
        <div className="flex items-center justify-between mb-8 border-b border-white/10 pb-4">
          <h1 className="text-2xl font-bold flex items-center gap-3">
            <Award className="text-yellow-400" size={32} />
            Test Nəticələri
          </h1>
          <button 
            onClick={() => navigate(-1)} 
            className="btn btn-secondary text-sm flex items-center gap-2 cursor-pointer hover:bg-white/10"
          >
            Sertifikatlara Qayıt
          </button>
        </div>

        {/* Overview Stats */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="glass p-5 rounded-2xl border border-white/10 text-center">
            <p className="text-sm text-white/60 mb-1">Ümumi Düzgün Faizi</p>
            <p className="text-4xl font-extrabold text-primary">{percentage}%</p>
          </div>
          <div className="glass p-5 rounded-2xl border border-green-500/20 bg-green-500/5 text-center">
            <p className="text-sm text-green-400 mb-1">Düzgün Cavablar</p>
            <p className="text-4xl font-extrabold text-green-400">{correct} / {total}</p>
          </div>
          <div className="glass p-5 rounded-2xl border border-red-500/20 bg-red-500/5 text-center">
            <p className="text-sm text-red-400 mb-1">Səhv Cavablar</p>
            <p className="text-4xl font-extrabold text-red-400">{wrong}</p>
          </div>
          <div className="glass p-5 rounded-2xl border border-yellow-500/20 bg-yellow-500/5 text-center">
            <p className="text-sm text-yellow-400 mb-1">Cavablandırılmayan</p>
            <p className="text-4xl font-extrabold text-yellow-400">{unanswered}</p>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap gap-4 mb-8">
          {wrong > 0 && (
            <button 
              onClick={() => setShowWrongOnlyModal(!showWrongOnlyModal)}
              className="btn bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/30 flex items-center gap-2"
            >
              <AlertTriangle size={18} />
              {showWrongOnlyModal ? 'Bütün Suallara Bax' : `Səhv Cavabları Göstər (${wrong})`}
            </button>
          )}
          <button 
            onClick={() => window.location.reload()} 
            className="btn btn-primary flex items-center gap-2"
          >
            <RotateCcw size={18} />
            Testi Yenidən Başla
          </button>
        </div>

        {/* Detailed Question Review */}
        <div className="space-y-6">
          <h2 className="text-xl font-bold border-b border-white/10 pb-3">
            {showWrongOnlyModal ? 'Yalnız Səhv Cavablandırılan Suallar' : 'Bütün Sualların İcmalı'}
          </h2>

          {(showWrongOnlyModal ? wrongQuestionsList : questions.map((q, idx) => ({ q, idx, ans: userAnswers[idx] }))).map(({ q, idx, ans }) => {
            const isAnswered = !!ans;
            const isCorrect = ans?.isCorrect;
            const optionKeys = Object.keys(q.options || {});

            return (
              <div 
                key={idx} 
                className={`glass p-6 rounded-2xl border ${
                  !isAnswered 
                    ? 'border-white/10' 
                    : isCorrect 
                    ? 'border-green-500/30 bg-green-500/5' 
                    : 'border-red-500/30 bg-red-500/5'
                }`}
              >
                <div className="flex items-start justify-between gap-4 mb-4">
                  <h3 className="font-semibold text-lg">
                    <span className="text-primary mr-2">Sual {idx + 1}:</span> {q.question}
                  </h3>
                  {isAnswered ? (
                    isCorrect ? (
                      <span className="flex items-center gap-1 text-sm bg-green-500/20 text-green-400 px-3 py-1 rounded-full flex-shrink-0 font-medium">
                        <Check size={16} /> Düzgün
                      </span>
                    ) : (
                      <span className="flex items-center gap-1 text-sm bg-red-500/20 text-red-400 px-3 py-1 rounded-full flex-shrink-0 font-medium">
                        <X size={16} /> Səhv
                      </span>
                    )
                  ) : (
                    <span className="text-sm bg-yellow-500/20 text-yellow-400 px-3 py-1 rounded-full flex-shrink-0 font-medium">
                      Cavablandırılmadı
                    </span>
                  )}
                </div>

                <div className="grid grid-cols-1 gap-2 mb-3">
                  {(Array.isArray(q.options) ? ['A','B','C','D'].slice(0, q.options.length) : Object.keys(q.options || {})).map((key, optIdx) => {
                    const optText = Array.isArray(q.options) ? q.options[optIdx] : q.options[key];
                    const isUserSelected = String(ans?.selected) === String(key) || ans?.selected === optIdx;
                    
                    const correctKey = typeof q.correct_answer === 'number' ? ['A','B','C','D'][q.correct_answer] : q.correct_answer;
                    const isCorrectOpt = String(correctKey) === String(key) || q.correct_answer === optIdx;

                    let optStyle = "p-3 rounded-xl text-sm border flex items-center justify-between ";
                    if (isCorrectOpt) {
                      optStyle += "border-green-500 bg-green-500/20 text-green-300 font-semibold";
                    } else if (isUserSelected && !isCorrectOpt) {
                      optStyle += "border-red-500 bg-red-500/20 text-red-300 font-semibold";
                    } else {
                      optStyle += "border-white/5 opacity-60";
                    }

                    return (
                      <div key={key} className={optStyle}>
                        <span><strong>{key})</strong> {optText}</span>
                        <div className="flex gap-2">
                          {isCorrectOpt && <span className="text-xs bg-green-500 text-black px-2 py-0.5 rounded font-bold">Düzgün Variant ✓</span>}
                          {isUserSelected && !isCorrectOpt && <span className="text-xs bg-red-500 text-white px-2 py-0.5 rounded font-bold">Sizin Seçiminiz ✕</span>}
                        </div>
                      </div>
                    );
                  })}
                </div>

                {q.explanation && (
                  <div className="mt-3 p-3 rounded-lg bg-blue-500/10 text-blue-200 text-xs border border-blue-500/20">
                    <strong>İzah:</strong> {q.explanation}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // ─── ACTIVE TEST QUESTION VIEW ───────────────────────────
  const q = questions[currentQuestion];
  const optionKeys = Object.keys(q.options || {});
  const currentAnswer = userAnswers[currentQuestion];

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out]">
      {/* Header Bar */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8 border-b border-white/10 pb-4">
        <div className="flex items-center gap-4">
          <button onClick={() => navigate(-1)} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
            <ArrowLeft size={24} />
          </button>
          <div>
            <h1 className="text-xl font-bold leading-tight">{certificateName || 'Test'}</h1>
            <p className="text-xs text-white/50">Sual {currentQuestion + 1} / {questions.length}</p>
          </div>
        </div>

        {/* Header Right Actions */}
        <div className="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-end">
          <button
            onClick={() => {
              setQuestions([...questions].sort(() => Math.random() - 0.5));
              setCurrentQuestion(0);
            }}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl border border-white/10 bg-white/5 hover:bg-white/10 text-white/80 hover:text-white text-xs font-semibold transition-all cursor-pointer"
            title="Sualları qarışdır"
          >
            <Shuffle size={15} className="text-primary" />
            <span>Qarışdır</span>
          </button>
          <button 
            onClick={handleFinishTest} 
            className="btn bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/30 px-3.5 py-1.5 text-xs flex items-center gap-1.5 rounded-xl transition-all cursor-pointer"
          >
            <Flag size={15} />
            Testi Bitir
          </button>
        </div>
      </div>

      {/* Disclaimer Banner */}
      <div className="mb-6 p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs flex items-center gap-2.5">
        <AlertTriangle size={18} className="flex-shrink-0 text-amber-400" />
        <span><strong>Xəbərdarlıq:</strong> İmtahan suallarında və ya variantlarında uyğunsuzluq ola bilər. Suallar mütəmadi olaraq yenilənir və dəqiqləşdirilir.</span>
      </div>

      {/* Question Content */}
      <div className="mb-8">
        <h2 className="text-xl md:text-2xl font-medium mb-4 leading-relaxed">{q.question}</h2>
        {q.image_url && (
          <div className="mb-6 max-w-md mx-auto rounded-xl overflow-hidden border border-white/20 shadow-lg bg-black/40 p-2 text-center">
            <img src={getImageUrl(q.image_url)} alt="Sual şəkli" className="max-h-64 mx-auto rounded-lg object-contain" />
          </div>
        )}
        <div className="space-y-3">
          {optionKeys.map((key) => {
            const optText = q.options[key];
            const isSelected = currentAnswer?.selected === key;
            
            let btnClass = "w-full text-left p-4 rounded-xl border transition-all duration-200 cursor-pointer ";
            if (isSelected) {
              btnClass += "border-primary bg-primary/20 text-white font-semibold shadow-lg shadow-primary/10";
            } else {
              btnClass += "border-white/10 hover:border-white/30 hover:bg-white/5 text-white/90";
            }

            return (
              <button 
                key={key} 
                className={btnClass}
                onClick={() => handleOptionSelect(key)}
              >
                <div className="flex items-center justify-between">
                  <span><strong className="mr-2 text-primary">{key})</strong> {optText}</span>
                  {isSelected && <CheckCircle2 className="text-primary flex-shrink-0 ml-2" size={20} />}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Navigation Controls (Always Available Next & Prev) */}
      <div className="flex items-center justify-between pt-6 border-t border-white/10">
        <button 
          onClick={() => setCurrentQuestion(prev => Math.max(0, prev - 1))}
          disabled={currentQuestion === 0}
          className="btn btn-secondary disabled:opacity-30 disabled:cursor-not-allowed"
        >
          Əvvəlki Sual
        </button>

        <div className="text-sm text-white/50 hidden sm:block">
          {Object.keys(userAnswers).length} / {questions.length} cavablandırıldı
        </div>

        {currentQuestion < questions.length - 1 ? (
          <button 
            onClick={() => setCurrentQuestion(prev => prev + 1)}
            className="btn btn-primary"
          >
            Növbəti Sual
          </button>
        ) : (
          <button 
            onClick={handleFinishTest}
            className="btn bg-green-500 hover:bg-green-600 text-black font-bold"
          >
            Nəticələri Gör
          </button>
        )}
      </div>
    </div>
  );
}
