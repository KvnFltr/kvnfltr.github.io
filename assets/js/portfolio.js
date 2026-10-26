(() => {
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  let preference;
  try { preference = localStorage.getItem('portfolio-theme'); } catch (_) { /* Optional preference. */ }
  if (preference === 'light' || preference === 'dark') root.dataset.theme = preference;
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  const update = () => {
    button.textContent = isDark() ? 'Light' : 'Dark';
    button.setAttribute('aria-label', `Switch to ${isDark() ? 'light' : 'dark'} theme`);
  };
  button.hidden = false;
  update();
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', update);
  button.addEventListener('click', () => {
    root.dataset.theme = isDark() ? 'light' : 'dark';
    try { localStorage.setItem('portfolio-theme', root.dataset.theme); } catch (_) { /* Works without storage. */ }
    update();
  });
})();
