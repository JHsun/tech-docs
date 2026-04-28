/* ============================================================
   JHsun TechDocs — Mermaid theme integration
   v1.0 · Calm Teal

   USAGE:
     <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
     <script src="shared/mermaid-init.js"></script>

   Mermaid will auto-init with the current theme, follow theme-toggle
   changes, and re-render all .mermaid blocks on theme switch.
   ============================================================ */
(function () {
  'use strict';

  /**
   * Resolve current OKLCH primary as a hex string for Mermaid.
   * Mermaid's themeVariables only accept hex/rgb, not OKLCH — we sample
   * the live computed style of a hidden probe element.
   */
  function readToken(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }

  // Canvas-based color resolver — forces the browser to perform OKLCH→sRGB
  // conversion and reads back actual pixel bytes. Reliable across Chrome
  // (which preserves "oklch(...)" in getComputedStyle().color) and other
  // engines. Mermaid only accepts hex/rgb, so we MUST resolve here.
  let _ctx;
  function getCtx() {
    if (_ctx) return _ctx;
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 1;
    _ctx = canvas.getContext('2d', { willReadFrequently: true });
    return _ctx;
  }
  function oklchToHex(colorStr) {
    const ctx = getCtx();
    // Reset to a known transparent state so previous fills don't bleed
    ctx.clearRect(0, 0, 1, 1);
    ctx.fillStyle = '#000000';     // fallback if assignment below silently fails
    ctx.fillStyle = colorStr;       // browser parses + converts oklch() here
    ctx.fillRect(0, 0, 1, 1);
    const [r, g, b] = ctx.getImageData(0, 0, 1, 1).data;
    return '#' + [r, g, b].map(v => v.toString(16).padStart(2, '0')).join('');
  }

  function token(name) {
    const v = readToken(name);
    if (!v) return '#000000';
    if (v.startsWith('#')) return v;
    return oklchToHex(v);
  }

  /**
   * Build Mermaid themeVariables from the current CSS token layer.
   * Re-evaluates on every call, so it picks up theme-toggle changes.
   */
  function getMermaidConfig(theme) {
    const isDark = theme === 'dark' || document.documentElement.dataset.theme === 'dark';
    return {
      startOnLoad: false,
      theme: 'base',
      fontFamily: readToken('--font-sans') || 'DM Sans, Inter, sans-serif',
      themeVariables: {
        // Core
        primaryColor:       token('--color-primary-soft'),
        primaryTextColor:   token('--text-primary'),
        primaryBorderColor: token('--color-primary'),
        lineColor:          token('--border-mid'),
        secondaryColor:     token('--bg-muted'),
        tertiaryColor:      token('--bg-surface'),
        // Backgrounds
        background:         token('--bg-canvas'),
        mainBkg:            token('--color-primary-soft'),
        secondBkg:          token('--bg-muted'),
        // Notes / clusters
        noteBkgColor:       token('--color-warning-soft'),
        noteTextColor:      token('--text-primary'),
        noteBorderColor:    token('--color-warning'),
        // Sequence
        actorBkg:           token('--color-primary-soft'),
        actorBorder:        token('--color-primary'),
        actorTextColor:     token('--text-primary'),
        actorLineColor:     token('--border-mid'),
        signalColor:        token('--text-secondary'),
        signalTextColor:    token('--text-primary'),
        labelBoxBkgColor:   token('--bg-surface'),
        labelBoxBorderColor:token('--border-mid'),
        labelTextColor:     token('--text-primary'),
        // State / flowchart
        nodeBorder:         token('--color-primary'),
        clusterBkg:         token('--bg-muted'),
        clusterBorder:      token('--border-soft'),
        defaultLinkColor:   token('--text-secondary'),
        edgeLabelBackground:token('--bg-surface'),
        // Text
        textColor:          token('--text-primary'),
        // Dark-aware tweaks
        ...(isDark && {
          mainBkg: token('--color-primary-soft'),
        }),
      },
      flowchart:  { htmlLabels: true, curve: 'basis', padding: 16 },
      sequence:   { mirrorActors: false, actorMargin: 60, messageMargin: 40 },
      gantt:      { fontSize: 13 },
      securityLevel: 'loose',
    };
  }

  /**
   * Re-render every .mermaid element on the page with the current theme.
   * Stores the original source text in data-mermaid-src so re-rendering
   * works after the first pass replaces innerHTML with SVG.
   */
  async function renderAll() {
    if (typeof mermaid === 'undefined') return;
    const blocks = document.querySelectorAll('.mermaid');
    blocks.forEach(el => {
      if (!el.dataset.mermaidSrc) {
        el.dataset.mermaidSrc = el.textContent.trim();
      }
      el.innerHTML = el.dataset.mermaidSrc;
      el.removeAttribute('data-processed');
    });
    mermaid.initialize(getMermaidConfig());
    await mermaid.run({ querySelector: '.mermaid' });
  }

  // Initial render once DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderAll);
  } else {
    renderAll();
  }

  // Re-render whenever theme-toggle.js fires this event
  window.addEventListener('jhsun:theme-changed', renderAll);

  // Public API
  window.JHsunMermaid = {
    getMermaidConfig,
    renderAll,
  };
})();
