// Shared mermaid initializer for proxy-guide
// Usage: include AFTER mermaid.min.js, then call renderMermaid() on init and on theme toggle.
// Source-of-truth for HTML labels: write entities (e.g. &lt;br/&gt;) inside <pre class="mermaid">,
// because textContent reading will strip live HTML elements.
(function(){
  function getMermaidConfig(theme){
    var isDark = theme === 'dark';
    return {
      startOnLoad: false,
      theme: 'base',
      securityLevel: 'loose',
      fontFamily: '"Inter","Noto Serif TC",sans-serif',
      flowchart: { htmlLabels: true, curve: 'basis' },
      sequence: { useMaxWidth: true, wrap: true },
      themeVariables: isDark ? {
        primaryColor:'#211c19', primaryTextColor:'#e7e5e4', primaryBorderColor:'#fb923c',
        lineColor:'#fb923c', secondaryColor:'#25201d', tertiaryColor:'#1f1a17',
        background:'#1f1a17', mainBkg:'#211c19', secondBkg:'#25201d',
        textColor:'#e7e5e4', labelTextColor:'#e7e5e4',
        edgeLabelBackground:'#1f1a17',
        clusterBkg:'#25201d', clusterBorder:'#4a4138',
        // sequenceDiagram-specific
        actorBorder:'#fb923c', actorBkg:'#211c19', actorTextColor:'#e7e5e4', actorLineColor:'#fb923c',
        signalColor:'#fb923c', signalTextColor:'#e7e5e4',
        labelBoxBkgColor:'#25201d', labelBoxBorderColor:'#fb923c', loopTextColor:'#e7e5e4',
        noteBkgColor:'rgba(251,146,60,0.10)', noteBorderColor:'#fb923c', noteTextColor:'#e7e5e4',
        activationBkgColor:'#fb923c', activationBorderColor:'#fbbf24', sequenceNumberColor:'#1a1614'
      } : {
        primaryColor:'#fef0e6', primaryTextColor:'#1c1917', primaryBorderColor:'#7c2d12',
        lineColor:'#7c2d12', secondaryColor:'#f3efe6', tertiaryColor:'#fbfaf6',
        background:'#fbfaf6', mainBkg:'#ffffff', secondBkg:'#f3efe6',
        textColor:'#1c1917', labelTextColor:'#1c1917',
        edgeLabelBackground:'#fbfaf6',
        clusterBkg:'#f3efe6', clusterBorder:'#b8ad95',
        actorBorder:'#7c2d12', actorBkg:'#ffffff', actorTextColor:'#1c1917', actorLineColor:'#7c2d12',
        signalColor:'#7c2d12', signalTextColor:'#1c1917',
        labelBoxBkgColor:'#fef0e6', labelBoxBorderColor:'#7c2d12', loopTextColor:'#1c1917',
        noteBkgColor:'#fef0e6', noteBorderColor:'#7c2d12', noteTextColor:'#1c1917',
        activationBkgColor:'#7c2d12', activationBorderColor:'#d97706', sequenceNumberColor:'#faf8f3'
      }
    };
  }

  async function renderMermaid(){
    if (typeof mermaid === 'undefined') return;
    var theme = document.documentElement.getAttribute('data-theme');
    mermaid.initialize(getMermaidConfig(theme));
    var blocks = document.querySelectorAll('.mermaid');
    blocks.forEach(function(b){
      if (b.dataset.source) {
        b.textContent = b.dataset.source;
        b.removeAttribute('data-processed');
      } else {
        b.dataset.source = b.textContent;
      }
    });
    await mermaid.run({ querySelector: '.mermaid' });
  }

  window.renderMermaid = renderMermaid;
  window.getMermaidConfig = getMermaidConfig;
})();
