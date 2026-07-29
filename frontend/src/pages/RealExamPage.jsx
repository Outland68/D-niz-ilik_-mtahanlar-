import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { 
  ArrowLeft, CheckCircle2, XCircle, Shuffle, RotateCcw, 
  Award, AlertTriangle, Flag, Check, X, Clock
} from 'lucide-react';
import { apiGetQuestions, getImageUrl } from '../utils/api';

export default function RealExamPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { certificateId, certificateName, isClassic, customCount, isShuffle } = location.state || { certificateId: 1, isClassic: true, isShuffle: true };

  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [isFinished, setIsFinished] = useState(false);
  const [showWrongOnlyModal, setShowWrongOnlyModal] = useState(false);

  // ⏳ TIMER STATE (30 Minutes = 1800 seconds)
  const [timeLeft, setTimeLeft] = useState(1800);
  const [timeExpired, setTimeExpired] = useState(false);

  // Load and randomize questions
  useEffect(() => {
    async function loadQuestions() {
      try {
        const res = await apiGetQuestions(certificateId);
        if (!res) return;
        const data = await res.json();

        if (res.ok) {
          let list = data.questions || [];
          // Shuffle questions if isShuffle is enabled
          if (isShuffle !== false) {
            list = [...list].sort(() => Math.random() - 0.5);
          }

          // Determine question count (Classic DDLA = 20 questions, Custom = user selected)
          const targetCount = isClassic ? 20 : (customCount || 20);
          if (list.length > targetCount) {
            list = list.slice(0, targetCount);
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
  }, [certificateId, isClassic, customCount]);

  // ⏳ Timer Countdown Effect
  useEffect(() => {
    if (loading || isFinished || questions.length === 0) return;

    if (timeLeft <= 0) {
      setTimeExpired(true);
      handleFinishTest(true);
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft(prev => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, loading, isFinished, questions]);

  // Format seconds to MM:SS
  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleOptionSelect = (key, optIdx) => {
    if (isFinished) return;
    const q = questions[currentQuestion];
    const correctKey = typeof q.correct_answer === 'number' ? (['A','B','C','D'][q.correct_answer] || q.correct_answer) : q.correct_answer;
    const correctIndex = typeof q.correct_answer === 'number' ? q.correct_answer : ['A','B','C','D'].indexOf(q.correct_answer);
    
    const isCorrect = String(key) === String(correctKey) || optIdx === correctIndex;

    setUserAnswers(prev => ({
      ...prev,
      [currentQuestion]: {
        selected: key,
        selectedIndex: optIdx,
        isCorrect: isCorrect
      }
    }));
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
    
    // DDLA Pass criteria: 20 questions -> 14+ correct (70%+)
    const isPassed = isClassic ? (correct >= 14) : (percentage >= 70);

    return { correct, wrong, unanswered, total, percentage, isPassed };
  };

  const handleFinishTest = (autoExpired = false) => {
    setIsFinished(true);

    const { correct, total, percentage, isPassed } = calculateResults();
    const savedUser = JSON.parse(localStorage.getItem('user') || '{}');
    const userKey = savedUser.id ? `test_history_${savedUser.id}` : 'test_history_guest';

    const newEntry = {
      id: Date.now(),
      certificateName: `${certificateName || 'İmtahan'} (${isClassic ? 'Klassik DDLA' : 'Sərbəst'})`,
      date: new Date().toLocaleDateString('az-AZ', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }),
      correct,
      total,
      percentage,
      isPassed
    };

    const existingHistory = JSON.parse(localStorage.getItem(userKey) || '[]');
    const updatedHistory = [newEntry, ...existingHistory].slice(0, 3);
    localStorage.setItem(userKey, JSON.stringify(updatedHistory));
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
    const { correct, wrong, unanswered, total, percentage, isPassed } = calculateResults();
    const wrongQuestionsList = questions.map((q, idx) => ({ q, idx, ans: userAnswers[idx] }))
      .filter(item => item.ans && !item.ans.isCorrect);

    return (
      <div className="w-full glass-card p-4 sm:p-8 animate-[fadeIn_0.3s_ease-out]">
        {/* Pass / Fail Banner */}
        <div className={`p-4 sm:p-6 rounded-2xl mb-6 border text-center flex flex-col items-center justify-center gap-3 ${
          isPassed 
            ? 'bg-emerald-500/20 border-emerald-500/40 text-emerald-300' 
            : 'bg-red-500/20 border-red-500/40 text-red-300'
        }`}>
          <div className={`w-12 h-12 sm:w-16 sm:h-16 rounded-full flex items-center justify-center text-2xl sm:text-3xl font-extrabold shadow-lg ${
            isPassed ? 'bg-emerald-500 text-black' : 'bg-red-500 text-white'
          }`}>
            {isPassed ? '✓' : '✕'}
          </div>
          <div>
            <h2 className="text-xl sm:text-2xl md:text-3xl font-black uppercase tracking-wider leading-tight">
              {isPassed ? 'TƏBRİKLƏR! İMTAHANDAN KEÇDİNİZ 🎉' : 'İMTAHANDAN KƏSİLDİNİZ! ❌'}
            </h2>
            <p className="text-xs sm:text-sm opacity-80 mt-1">
              {isClassic 
                ? `Klassik DDLA Standartı: 20 sualdan ən azı 14-nü düzgün yazmalısınız. Siz ${correct} düzgün yazdınız.` 
                : `Ümumi Nəticə: ${percentage}% (Tələb olunan keçid balı: 70%)`
              }
            </p>
            {timeExpired && (
              <p className="text-xs text-yellow-400 font-bold mt-2">⏱️ 30 dəqiqəlik imtahan vaxtınız başa çatdı.</p>
            )}
          </div>
        </div>

        {/* Overview Stats (2x2 on mobile, 4x1 on desktop) */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mb-6">
          <div className="glass p-3.5 sm:p-5 rounded-2xl border border-white/10 text-center">
            <p className="text-xs sm:text-sm text-white/60 mb-1">Düzgün Faizi</p>
            <p className="text-2xl sm:text-4xl font-extrabold text-primary">{percentage}%</p>
          </div>
          <div className="glass p-3.5 sm:p-5 rounded-2xl border border-green-500/20 bg-green-500/5 text-center">
            <p className="text-xs sm:text-sm text-green-400 mb-1">Düzgün Cavab</p>
            <p className="text-2xl sm:text-4xl font-extrabold text-green-400">{correct} / {total}</p>
          </div>
          <div className="glass p-3.5 sm:p-5 rounded-2xl border border-red-500/20 bg-red-500/5 text-center">
            <p className="text-xs sm:text-sm text-red-400 mb-1">Səhv Cavab</p>
            <p className="text-2xl sm:text-4xl font-extrabold text-red-400">{wrong}</p>
          </div>
          <div className="glass p-3.5 sm:p-5 rounded-2xl border border-yellow-500/20 bg-yellow-500/5 text-center">
            <p className="text-xs sm:text-sm text-yellow-400 mb-1">Boş Buraxılan</p>
            <p className="text-2xl sm:text-4xl font-extrabold text-yellow-400">{unanswered}</p>
          </div>
        </div>

        {/* Action Buttons (Stacked on Mobile) */}
        <div className="flex flex-col sm:flex-row flex-wrap gap-3 mb-8">
          {wrong > 0 && (
            <button 
              onClick={() => setShowWrongOnlyModal(!showWrongOnlyModal)}
              className="btn bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/30 flex items-center justify-center gap-2 py-3 sm:py-2.5 text-xs sm:text-sm font-semibold cursor-pointer w-full sm:w-auto"
            >
              <AlertTriangle size={16} />
              {showWrongOnlyModal ? 'Bütün Suallara Bax' : `Səhv Cavabları Göstər (${wrong})`}
            </button>
          )}
          <button 
            onClick={() => window.location.reload()} 
            className="btn btn-primary flex items-center justify-center gap-2 py-3 sm:py-2.5 text-xs sm:text-sm font-bold cursor-pointer w-full sm:w-auto"
          >
            <RotateCcw size={16} />
            İmtahanı Yenidən Başla
          </button>
          <button 
            onClick={() => navigate(-1)} 
            className="btn btn-secondary flex items-center justify-center gap-2 py-3 sm:py-2.5 text-xs sm:text-sm font-semibold cursor-pointer w-full sm:w-auto"
          >
            Sertifikatlara Qayıt
          </button>
        </div>

        {/* Detailed Question Review */}
        <div className="space-y-4 sm:space-y-6">
          <h2 className="text-lg sm:text-xl font-bold border-b border-white/10 pb-3">
            {showWrongOnlyModal ? 'Yalnız Səhv Cavablandırılan Suallar' : 'Bütün Sualların İcmalı'}
          </h2>

          {(showWrongOnlyModal ? wrongQuestionsList : questions.map((q, idx) => ({ q, idx, ans: userAnswers[idx] }))).map(({ q, idx, ans }) => {
            const isAnswered = !!ans;
            const isCorrect = ans?.isCorrect;
            const optionKeys = Object.keys(q.options || {});

            return (
              <div 
                key={idx} 
                className={`glass p-4 sm:p-6 rounded-2xl border ${
                  !isAnswered 
                    ? 'border-white/10' 
                    : isCorrect 
                    ? 'border-green-500/30 bg-green-500/5' 
                    : 'border-red-500/30 bg-red-500/5'
                }`}
              >
                <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 mb-3">
                  <h3 className="font-semibold text-base sm:text-lg leading-snug">
                    <span className="text-primary mr-2">Sual {idx + 1}:</span> {q.question}
                  </h3>
                  {isAnswered ? (
                    isCorrect ? (
                      <span className="flex items-center gap-1 text-xs bg-green-500/20 text-green-400 px-2.5 py-1 rounded-full flex-shrink-0 font-bold self-start sm:self-auto">
                        <Check size={14} /> Düzgün
                      </span>
                    ) : (
                      <span className="flex items-center gap-1 text-xs bg-red-500/20 text-red-400 px-2.5 py-1 rounded-full flex-shrink-0 font-bold self-start sm:self-auto">
                        <X size={14} /> Səhv
                      </span>
                    )
                  ) : (
                    <span className="text-xs bg-yellow-500/20 text-yellow-400 px-2.5 py-1 rounded-full flex-shrink-0 font-bold self-start sm:self-auto">
                      Cavablandırılmadı
                    </span>
                  )}
                </div>

                {q.image_url && (
                  <div className="mb-4 max-w-sm mx-auto rounded-xl overflow-hidden border border-white/20 bg-black/40 p-2 text-center">
                    <img src={getImageUrl(q.image_url)} alt="Sual şəkli" className="max-h-48 mx-auto rounded object-contain" />
                  </div>
                )}

                <div className="grid grid-cols-1 gap-2 mb-2">
                  {(Array.isArray(q.options) ? ['A','B','C','D'].slice(0, q.options.length) : Object.keys(q.options || {})).map((key, optIdx) => {
                    const optText = Array.isArray(q.options) ? q.options[optIdx] : q.options[key];
                    const isUserSelected = String(ans?.selected) === String(key) || ans?.selected === optIdx;

                    const correctKey = typeof q.correct_answer === 'number' ? ['A','B','C','D'][q.correct_answer] : q.correct_answer;
                    const isCorrectOpt = String(correctKey) === String(key) || q.correct_answer === optIdx;

                    let optStyle = "p-3 rounded-xl text-xs sm:text-sm border flex flex-col sm:flex-row sm:items-center justify-between gap-1 ";
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
                        <div className="flex gap-1">
                          {isCorrectOpt && <span className="text-[10px] sm:text-xs bg-green-500 text-black px-2 py-0.5 rounded font-bold w-max">Düzgün Variant ✓</span>}
                          {isUserSelected && !isCorrectOpt && <span className="text-[10px] sm:text-xs bg-red-500 text-white px-2 py-0.5 rounded font-bold w-max">Sizin Seçiminiz ✕</span>}
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

  // ─── ACTIVE EXAM QUESTION VIEW WITH 30-MIN TIMER ─────────
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
            <h1 className="text-xl font-bold leading-tight">{certificateName || 'İmtahan Simulyasiyası'}</h1>
            <p className="text-xs text-white/50">
              {isClassic ? 'Klassik DDLA İmtahanı (20 Sual)' : `Sərbəst İmtahan (${questions.length} Sual)`} • Sual {currentQuestion + 1} / {questions.length}
            </p>
          </div>
        </div>

        {/* ⏱️ Timer & Actions */}
        <div className="flex items-center gap-4 w-full sm:w-auto justify-between sm:justify-end">
          <div className={`flex items-center gap-2 px-4 py-2 rounded-xl border text-sm font-mono font-bold ${
            timeLeft < 300 
              ? 'bg-red-500/20 border-red-500/40 text-red-400 animate-pulse' 
              : 'bg-white/5 border-white/10 text-amber-300'
          }`}>
            <Clock size={18} />
            <span>{formatTime(timeLeft)}</span>
          </div>

          <button 
            onClick={() => handleFinishTest(false)} 
            className="btn bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/30 px-4 py-2 text-sm flex items-center gap-2 rounded-xl transition-all"
          >
            <Flag size={16} />
            İmtahanı Bitir
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
          {(Array.isArray(q.options) ? ['A','B','C','D'].slice(0, q.options.length) : Object.keys(q.options || {})).map((key, optIdx) => {
            const optText = Array.isArray(q.options) ? q.options[optIdx] : q.options[key];
            const isSelected = currentAnswer?.selected === key || currentAnswer?.selectedIndex === optIdx;
            
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
                onClick={() => handleOptionSelect(key, optIdx)}
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

      {/* Navigation Controls */}
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
            onClick={() => handleFinishTest(false)}
            className="btn bg-green-500 hover:bg-green-600 text-black font-bold"
          >
            Nəticələri Gör
          </button>
        )}
      </div>
    </div>
  );
}
