/* JHsun TechDocs — Theme toggle v1.0 */
(function () {
  'use strict';
  const STORAGE_KEY = 'jhsun-theme';
  const ICONS = { light: '☀', dark: '☾', system: '◐' };
  const LABELS = { light: 'Light', dark: 'Dark', system: 'System' };
  function getStored() { try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; } }
  function setStored(v) { try { if (v === 'system' || v == null) localStorage.removeItem(STORAGE_KEY); else localStorage.setItem(STORAGE_KEY, v); } catch (_) {} }
  function systemPref() { return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'; }
  function effective(mode) { return mode === 'system' ? systemPref() : mode; }
  function applyTheme(mode) {
    const eff = effective(mode);
    document.documentElement.dataset.theme = eff;
    document.documentElement.dataset.themeMode = mode;
    updateButtons(mode);
    window.dispatchEvent(new CustomEvent('jhsun:theme-changed', { detail: { theme: eff, mode } }));
  }
  function updateButtons(mode) {
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.dataset.themeMode = mode;
      btn.setAttribute('aria-label', `Theme: ${LABELS[mode]} (click to change)`);
      btn.title = `Theme: ${LABELS[mode]}`;
      if (!btn.dataset.themeToggleStyled) {
        btn.innerHTML = `<span class="theme-icon">${ICONS[mode]}</span><span class="theme-label">${LABELS[mode]}</span>`;
      }
    });
  }
  function cycle(current) { return current === 'light' ? 'dark' : current === 'dark' ? 'system' : 'light'; }
  function getCurrentMode() { return getStored() || 'system'; }
  function init() {
    applyTheme(getCurrentMode());
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', () => {
        const next = cycle(getCurrentMode());
        setStored(next);
        applyTheme(next);
      });
    });
    const mq = window.matchMedia('(prefers-color-scheme: dark)');
    mq.addEventListener('change', () => { if (getCurrentMode() === 'system') applyTheme('system'); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  window.JHsunTheme = {
    get: getCurrentMode,
    set: (m) => { setStored(m); applyTheme(m); },
    toggle: () => { const next = cycle(getCurrentMode()); setStored(next); applyTheme(next); },
  };
})();
