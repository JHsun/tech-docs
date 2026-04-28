/* ============================================================
   JHsun TechDocs — Theme toggle
   v1.0 · light / dark with localStorage + prefers-color-scheme

   USAGE:
     <button data-theme-toggle aria-label="Toggle theme"></button>
     <script src="shared/theme-toggle.js"></script>

   Any element with [data-theme-toggle] becomes a button that cycles
   light → dark → system. The icon updates automatically.
   Also listens for OS-level prefers-color-scheme changes when in
   "system" mode.

   Fires window event "jhsun:theme-changed" with { detail: { theme } }
   on every change — mermaid-init.js subscribes to this.
   ============================================================ */
(function () {
  'use strict';

  const STORAGE_KEY = 'jhsun-theme';
  const ICONS = {
    light:  '☀',
    dark:   '☾',
    system: '◐',
  };
  const LABELS = {
    light:  'Light',
    dark:   'Dark',
    system: 'System',
  };

  function getStored() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; }
  }
  function setStored(v) {
    try {
      if (v === 'system' || v == null) localStorage.removeItem(STORAGE_KEY);
      else localStorage.setItem(STORAGE_KEY, v);
    } catch (_) { /* ignore */ }
  }

  function systemPref() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  /** Resolve the *effective* theme actually applied to <html>. */
  function effective(mode) {
    return mode === 'system' ? systemPref() : mode;
  }

  /** Apply a mode to <html> and notify subscribers. */
  function applyTheme(mode) {
    const eff = effective(mode);
    document.documentElement.dataset.theme = eff;
    document.documentElement.dataset.themeMode = mode; // for debugging
    updateButtons(mode);
    window.dispatchEvent(new CustomEvent('jhsun:theme-changed', {
      detail: { theme: eff, mode },
    }));
  }

  function updateButtons(mode) {
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.dataset.themeMode = mode;
      btn.setAttribute('aria-label', `Theme: ${LABELS[mode]} (click to change)`);
      btn.title = `Theme: ${LABELS[mode]}`;
      // Only fill content if button is empty — let users style their own
      if (!btn.dataset.themeToggleStyled) {
        btn.innerHTML = `<span class="theme-icon">${ICONS[mode]}</span><span class="theme-label">${LABELS[mode]}</span>`;
      }
    });
  }

  function cycle(current) {
    return current === 'light' ? 'dark' : current === 'dark' ? 'system' : 'light';
  }

  function getCurrentMode() {
    return getStored() || 'system';
  }

  function init() {
    // Apply stored or system preference on load
    applyTheme(getCurrentMode());

    // Wire up all toggle buttons
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', () => {
        const next = cycle(getCurrentMode());
        setStored(next);
        applyTheme(next);
      });
    });

    // Re-evaluate when OS preference changes (only relevant in "system" mode)
    const mq = window.matchMedia('(prefers-color-scheme: dark)');
    mq.addEventListener('change', () => {
      if (getCurrentMode() === 'system') applyTheme('system');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Public API for programmatic access
  window.JHsunTheme = {
    get:    getCurrentMode,
    set:    (m) => { setStored(m); applyTheme(m); },
    toggle: () => { const next = cycle(getCurrentMode()); setStored(next); applyTheme(next); },
  };
})();
