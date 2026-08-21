import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { authFetch } from '../utils/api';
import { Activity, Users, Globe, Clock, ShieldAlert } from 'lucide-react';

export default function AdminDashboard() {
  const [visits, setVisits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    // Ilk olarak superuser mi kontrol et
    authFetch('/auth/me/')
      .then(res => {
        if (!res || !res.ok) throw new Error('Not auth');
        return res.json();
      })
      .then(user => {
        if (!user || !user.is_superuser) {
          navigate('/'); // Eger superuser degilse anasayfaya at
        } else {
          fetchVisits();
        }
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

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6 pb-24">
      <div className="max-w-7xl mx-auto space-y-6">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Activity className="text-blue-500 w-8 h-8" />
            <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
              Admin Analitika Portalı
            </h1>
          </div>
          <button onClick={() => navigate('/menu')} className="px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg transition-colors border border-gray-700">
            Geri Dön
          </button>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-blue-500/20 p-3 rounded-lg">
              <Users className="text-blue-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Ümumi İzlənən Ziyarət</p>
              <h3 className="text-2xl font-bold">{visits.length}</h3>
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-xl p-5 border border-gray-700 flex items-center space-x-4">
            <div className="bg-emerald-500/20 p-3 rounded-lg">
              <Globe className="text-emerald-400 w-6 h-6" />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Son Qeydiyyat</p>
              <h3 className="text-xl font-bold">{visits[0]?.time?.split(' ')[1] || '-'}</h3>
            </div>
          </div>
        </div>

        {/* Table */}
        <div className="bg-gray-800 rounded-xl border border-gray-700 overflow-hidden">
          <div className="p-4 border-b border-gray-700 bg-gray-800/50 flex justify-between items-center">
            <h2 className="text-lg font-semibold flex items-center">
              <Clock className="w-5 h-5 mr-2 text-gray-400" />
              Son Ziyarətlər (Canlı İzləmə)
            </h2>
            <button onClick={fetchVisits} className="text-sm px-3 py-1 bg-blue-600 hover:bg-blue-500 rounded text-white transition">Yenilə</button>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-gray-900/50 text-gray-400">
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
                    <td className="px-4 py-3 text-gray-300">{v.time}</td>
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
