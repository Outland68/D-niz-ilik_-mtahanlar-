const BASE_URL = 'http://127.0.0.1:8000/api';

// ─── Token helpers ───────────────────────────────────
export const getAccessToken = () => localStorage.getItem('access_token');
export const getRefreshToken = () => localStorage.getItem('refresh_token');

export const saveTokens = (access, refresh) => {
  localStorage.setItem('access_token', access);
  if (refresh) localStorage.setItem('refresh_token', refresh);
};

export const clearTokens = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user');
};

// ─── Auth header ─────────────────────────────────────
const authHeaders = () => ({
  'Content-Type': 'application/json',
  'Authorization': `Bearer ${getAccessToken()}`,
});

// ─── Try to refresh token silently ───────────────────
const tryRefresh = async () => {
  const refresh = getRefreshToken();
  if (!refresh) return false;
  try {
    const res = await fetch(`${BASE_URL}/auth/refresh/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh }),
    });
    if (res.ok) {
      const data = await res.json();
      saveTokens(data.access, null);
      return true;
    }
  } catch (_) {}
  return false;
};

// ─── Authenticated fetch (auto-refreshes on 401) ─────
export const authFetch = async (url, options = {}) => {
  const fullUrl = url.startsWith('http') ? url : `${BASE_URL}${url}`;
  let res = await fetch(fullUrl, {
    ...options,
    headers: { ...authHeaders(), ...(options.headers || {}) },
  });

  if (res.status === 401) {
    const refreshed = await tryRefresh();
    if (refreshed) {
      res = await fetch(fullUrl, {
        ...options,
        headers: { ...authHeaders(), ...(options.headers || {}) },
      });
    } else {
      clearTokens();
      window.location.href = '/login';
      return null;
    }
  }
  return res;
};

// ─── Public fetch (no auth) ──────────────────────────
export const publicFetch = (path, options = {}) =>
  fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });

// ─── Auth API calls ──────────────────────────────────
export const apiLogin = (username, password) =>
  publicFetch('/auth/login/', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
  });

export const apiRegister = (username, email, password) =>
  publicFetch('/auth/register/', {
    method: 'POST',
    body: JSON.stringify({ username, email, password }),
  });

export const apiSendResetCode = (email) =>
  publicFetch('/auth/send-reset-code/', {
    method: 'POST',
    body: JSON.stringify({ email }),
  });

export const apiVerifyResetCode = (email, code, new_password) =>
  publicFetch('/auth/verify-reset-code/', {
    method: 'POST',
    body: JSON.stringify({ email, code, new_password }),
  });

export const apiLogout = async () => {
  const refresh = getRefreshToken();
  if (refresh) {
    await authFetch('/auth/logout/', {
      method: 'POST',
      body: JSON.stringify({ refresh }),
    });
  }
  clearTokens();
};

export const apiChangePassword = (old_password, new_password) =>
  authFetch('/auth/change-password/', {
    method: 'POST',
    body: JSON.stringify({ old_password, new_password }),
  });

// ─── Data API calls ──────────────────────────────────
export const apiGetCategories = () => publicFetch('/categories/');
export const apiGetCertificates = (categoryId) =>
  publicFetch(categoryId ? `/certificates/?category=${categoryId}` : '/certificates/');

export const apiGetQuestions = (certificateId) =>
  authFetch(`/certificates/${certificateId}/questions/`);
