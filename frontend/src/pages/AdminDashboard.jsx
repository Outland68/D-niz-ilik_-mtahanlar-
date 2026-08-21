import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { authFetch } from '../utils/api';
import { Activity, Users, Globe, Clock, ShieldAlert, BarChart3, Calendar } from 'lucide-react';

export default function AdminDashboard() {
  const [visits, setVisits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    authFetch('/auth/me/')
      .then(res => {
        if (!res || !res.ok) throw new Error('Not auth');
        return res.json();
      })
      .then(user => {
        if (!user || !user.is_superuser) navigate('/');
        else fetchVisits();
      })
      .catch(() => navigate('/'));
  }, [navigate]);

  const fetchVisits = async () => {
    try {
      const res = await authFetch('/site-visits/');
      if (!res || !res.ok) throw new Error('Error');
      const data = await res.json();
      if (data && data.error) throw new Error(data.error);
      setVisits(data || []);
    } catch (err) {
      setError('Veriler alınamadı veya yetkiniz yok.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="min-h-screen bg-gray-900 flex items-center justify-center"><div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div></div>;
  if (error) return <div className="min-h-screen bg-gray-900 flex items-center justify-center text-red-500 font-bold text-xl"><ShieldAlert className="mr-2" /> {error}</div>;

  // Analitika Hesablamaları
  const uniqueUsers = new Set(visits.filter(v => v.username !== 'Anonim').map(v => v.username)).size;
  const uniqueIPs = new Set(visits.map(v => v.ip)).size;

  // Günlərə görə ayırma (Son 7 Gün)
  const visitsByDate = visits.reduce((acc, v) => {
    const date = v.time.split(' ')[0]; // '2026-08-21'
    acc[date] = (acc[date] || 0) + 1;
    return acc;
  }, {});

  // Qrafik üçün datanı sıralamaq
  const sortedDates = Object.keys(visitsByDate).sort();
  const maxVisits = Math.max(...Object.values(visitsByDate), 1); // 1 is for fallback to avoid div by zero

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6 pb-24 font-sans">
      <div className="max-w-7xl mx-auto space-y-8">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Activity className="text-blue-500 w-8 h-8" />
            <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
              Analitika Portalı
            </h1>
          </div>
          <button onClick={() => navigate('/menu')} className="px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg transition-colors border border-gray-700">
            Geri Dön
          </button>
        </div>

        {/* Xülasə (Stats) Kartları */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-blue-500/20 p-3 rounded-lg">
              <Activity className="text-blue-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Ümumi Ziyarət (Kliklər)</p>
              <h3 className="text-2xl font-bold">{visits.length}</h3>
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-emerald-500/20 p-3 rounded-lg">
              <Users className="text-emerald-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Giriş Edən Tələbələr</p>
              <h3 className="text-2xl font-bold">{uniqueUsers}</h3>
            </div>
          </div>

          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-purple-500/20 p-3 rounded-lg">
              <Globe className="text-purple-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Fərqli IP Ünvanlar</p>
              <h3 className="text-2xl font-bold">{uniqueIPs}</h3>
            </div>
          </div>

          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-orange-500/20 p-3 rounded-lg">
              <Calendar className="text-orange-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Aktiv Gün Sayı</p>
              <h3 className="text-2xl font-bold">{sortedDates.length}</h3>
            </div>
          </div>
        </div>

        {/* Günlük Statistik Qrafik (Bar Chart) */}
        <div className="bg-gray-800 rounded-xl border border-gray-700 p-6">
          <h2 className="text-lg font-semibold mb-6 flex items-center">
            <BarChart3 className="w-5 h-5 mr-2 text-gray-400" />
            Günlük Ziyarət Qrafiki
          </h2>
          
          {sortedDates.length > 0 ? (
            <div className="flex items-end space-x-2 sm:space-x-4 h-64 overflow-x-auto pb-2">
              {sortedDates.slice(-14).map((date, idx) => {
                const count = visitsByDate[date];
                const heightPercent = (count / maxVisits) * 100;
                
                return (
                  <div key={idx} className="flex flex-col items-center flex-1 min-w-[40px] group">
                    {/* Tooltip on hover */}
                    <span className="opacity-0 group-hover:opacity-100 transition-opacity text-xs font-bold bg-gray-900 px-2 py-1 rounded mb-2 whitespace-nowrap">
                      {count} Ziyarət
                    </span>
                    
                    {/* Bar */}
                    <div 
                      className="w-full max-w-[40px] bg-gradient-to-t from-blue-600 to-blue-400 rounded-t-sm transition-all duration-500 ease-out"
                      style={{ height: `${heightPercent}%`, minHeight: '4px' }}
                    ></div>
                    
                    {/* Date Label */}
                    <span className="text-xs text-gray-400 mt-3 transform -rotate-45 origin-top-left translate-y-2 whitespace-nowrap">
                      {date.slice(5)} {/* MM-DD formatı */}
                    </span>
                  </div>
                );
              })}
            </div>
          ) : (
            <div className="h-48 flex items-center justify-center text-gray-500">Kifayət qədər məlumat yoxdur</div>
          )}
        </div>

        {/* Cədvəl */}
        <div className="bg-gray-800 rounded-xl border border-gray-700 overflow-hidden">
          <div className="p-4 border-b border-gray-700 bg-gray-800/50 flex justify-between items-center">
            <h2 className="text-lg font-semibold flex items-center">
              <Clock className="w-5 h-5 mr-2 text-gray-400" />
              Giriş Tarixçəsi (Son Ziyarətlər)
            </h2>
            <button onClick={fetchVisits} className="text-sm px-3 py-1 bg-blue-600 hover:bg-blue-500 rounded text-white transition shadow">
              Yenilə
            </button>
          </div>
          <div className="overflow-x-auto max-h-[500px]">
            <table className="w-full text-left text-sm">
              <thead className="bg-gray-900/50 text-gray-400 sticky top-0 backdrop-blur-md">
                <tr>
                  <th className="px-4 py-3 font-medium">İstifadəçi</th>
                  <th className="px-4 py-3 font-medium">IP Ünvanı</th>
                  <th className="px-4 py-3 font-medium">Səhifə (URL)</th>
                  <th className="px-4 py-3 font-medium">Tarix / Saat</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-700">
                {visits.map((v, i) => (
                  <tr key={v.id || i} className="hover:bg-gray-700/50 transition-colors">
                    <td className="px-4 py-3">
                      <span className={`inline-flex items-center px-2 py-1 rounded text-xs font-medium ${
                        v.username === 'Anonim' ? 'bg-gray-700 text-gray-300' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                      }`}>
                        {v.username}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-gray-300 font-mono text-xs">{v.ip}</td>
                    <td className="px-4 py-3 text-gray-400 truncate max-w-[200px]" title={v.url}>
                      {v.url.split('/').slice(-2).join('/') || '/'}
                    </td>
                    <td className="px-4 py-3 text-gray-300 whitespace-nowrap">{v.time}</td>
                  </tr>
                ))}
                {visits.length === 0 && (
                  <tr>
                    <td colSpan="4" className="px-4 py-8 text-center text-gray-500">
                      Hələ ki, heç bir ziyarət qeydə alınmayıb.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
        
      </div>
    </div>
  );
}
