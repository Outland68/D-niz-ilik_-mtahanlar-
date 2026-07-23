import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Anchor, ArrowLeft, Award, FileBadge } from 'lucide-react';
import { apiGetCategories } from '../utils/api';

export default function NovSecimi() {
  const navigate = useNavigate();
  const [types, setTypes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiGetCategories()
      .then(res => res.json())
      .then(data => {
        setTypes(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("API error", err);
        setLoading(false);
      });
  }, []);

  const getIcon = (iconName) => {
    switch(iconName) {
      case 'Anchor': return <Anchor size={32} />;
      case 'FileBadge': return <FileBadge size={32} />;
      case 'Award': return <Award size={32} />;
      default: return <Anchor size={32} />;
    }
  };

  return (
    <div className="w-full glass-card p-8 animate-[fadeIn_0.3s_ease-out]">
      <div className="flex items-center gap-4 mb-8 border-b border-white/10 pb-4">
        <button onClick={() => navigate('/menu')} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
          <ArrowLeft size={24} />
        </button>
        <div>
          <h1 className="text-3xl font-bold">Növ Seçimi</h1>
          <p className="text-white/50 mt-1">İmtahan vermək istədiyiniz sahəni seçin</p>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-12 text-white/50">Yüklənir...</div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {types.map(type => (
            <div 
              key={type.id}
              onClick={() => navigate('/certificate-selection', { state: { categoryId: type.id, categoryName: type.name } })}
              className="glass p-6 rounded-xl cursor-pointer hover:-translate-y-2 hover:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:bg-white/10 transition-all duration-300 text-center group"
            >
              <div className={`w-20 h-20 mx-auto rounded-2xl ${type.color || 'bg-blue-500/20 text-blue-400'} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform shadow-lg`}>
                {getIcon(type.icon_name)}
              </div>
              <h3 className="text-lg font-bold leading-tight">{type.name}</h3>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
