// Python 3.14 快速學習 — 共用腳本

// 複製按鈕功能
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const codeBlock = btn.closest('.code-block').querySelector('pre code');
    const text = codeBlock.innerText;
    navigator.clipboard.writeText(text).then(() => {
      const original = btn.innerText;
      btn.innerText = '已複製 ✓';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.innerText = original;
        btn.classList.remove('copied');
      }, 1500);
    });
  });
});

// 側邊欄依捲動高亮
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.sidebar-nav a');

if (sections.length > 0 && navLinks.length > 0) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, { rootMargin: '-30% 0px -60% 0px' });

  sections.forEach(s => observer.observe(s));
}
