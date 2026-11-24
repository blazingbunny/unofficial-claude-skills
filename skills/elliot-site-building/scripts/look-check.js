// Readability and layout check for the page open in the browser panel. Read-only: it measures, changes nothing.
// Run it with the browser's JavaScript tool (paste the whole file). Set SCOPE to a CSS selector for the part under
// check plus its neighbours (usually the page's main box, for example '#main', or one part such as '.vk-panel'),
// or leave it null for the page's main content. Run it at desktop width and again at phone width (resize_window
// mobile preset). The pages are plain Astro HTML: a <header>, a <main id="main"> and a <footer data-ss-footer>.
// The header and footer are skipped, so the check covers the page body only.
// Thresholds: WCAG 2.2 AA (contrast 4.5:1, 3:1 for large text; touch targets 24px) plus common readability
// guidance (body text 16px or more, line height 1.4 or more, at most about 75 characters per line).
// What the results mean and what to do with them: references/look-and-feel.md.
(() => {
  const SCOPE = null;
  const root = (SCOPE && document.querySelector(SCOPE)) || document.querySelector('main, #main') || document.body;
  const skip = el => el.closest('header, footer, [data-ss-nav], [data-ss-footer], [aria-hidden="true"]');
  const visible = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  // Name shown in the results: the element's first class (for example vk-btn) or its tag, plus its first words.
  const label = el => (el.classList[0] || el.tagName.toLowerCase()) + ' "' + (el.innerText || el.value || '').trim().slice(0, 40) + '"';

  const rgb = c => { const m = c.match(/[\d.]+/g); return m ? m.map(Number) : [0, 0, 0, 1]; };
  const lum = ([r, g, b]) => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  // Background behind an element: the first non-transparent colour up the tree. null over an image (can't measure).
  const bgOf = el => { for (let e = el; e; e = e.parentElement) { const s = getComputedStyle(e); if (s.backgroundImage !== 'none') return null; const c = rgb(s.backgroundColor); if ((c[3] ?? 1) > 0.5) return c; } return [255, 255, 255, 1]; };

  // Text: size, line height, line length, contrast. Only elements that hold text directly.
  const texts = [...root.querySelectorAll('p, li, a, span, h1, h2, h3, h4, h5, h6, label, button, td, th, blockquote, figcaption')]
    .filter(el => !skip(el) && visible(el) && [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 2));
  const small = [], tight = [], longLines = [], lowContrast = [], sizes = {};
  for (const el of texts) {
    const s = getComputedStyle(el), fs = parseFloat(s.fontSize), bold = parseInt(s.fontWeight) >= 700;
    const isHeading = /^H\d$/.test(el.tagName), large = fs >= 24 || (bold && fs >= 18.66);
    sizes[Math.round(fs) + 'px'] = (sizes[Math.round(fs) + 'px'] || 0) + 1;
    if (!isHeading && fs < 16) small.push(`${label(el)} ${fs}px`);
    const lh = s.lineHeight === 'normal' ? fs * 1.2 : parseFloat(s.lineHeight);
    if (!isHeading && lh / fs < 1.4) tight.push(`${label(el)} line height ${(lh / fs).toFixed(2)}`);
    if (['P', 'LI'].includes(el.tagName)) {
      const lines = Math.max(1, Math.round(el.getBoundingClientRect().height / lh)), chars = el.innerText.trim().length;
      if (lines > 1 && chars / lines > 75) longLines.push(`${label(el)} ~${Math.round(chars / lines)} characters per line`);
    }
    const bg = bgOf(el);
    if (bg) {
      const a = lum(rgb(s.color)), b = lum(bg), ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
      if (ratio < (large ? 3 : 4.5)) lowContrast.push(`${label(el)} contrast ${ratio.toFixed(2)}:1 (needs ${large ? 3 : 4.5})`);
    }
  }

  // Touch targets: links, buttons and form fields smaller than 24px (WCAG minimum; 44px is comfortable).
  // Links inside a sentence are exempt, as in WCAG.
  const tiny = [...root.querySelectorAll('a, button, input, select, textarea, [role="button"]')]
    .filter(el => !skip(el) && visible(el) && !(getComputedStyle(el).display === 'inline' && el.closest('p, li')))
    .filter(el => { const r = el.getBoundingClientRect(); return r.width < 24 || r.height < 24; })
    .map(el => { const r = el.getBoundingClientRect(); return `${label(el)} ${Math.round(r.width)}x${Math.round(r.height)}px`; });

  // Sideways scrolling: anything wider than the window.
  const overflow = document.documentElement.scrollWidth > innerWidth + 1
    ? [...root.querySelectorAll('*')].filter(el => !skip(el) && el.getBoundingClientRect().right > innerWidth + 1).slice(0, 5).map(label) : [];

  // Spacing: vertical gaps between the checked area's direct children (descending through single wrappers).
  // Look for uneven gaps between blocks of the same kind, for example before each section heading.
  let box = root;
  while (box.children.length === 1) box = box.children[0];
  const kids = [...box.children].filter(el => !skip(el) && visible(el));
  const gaps = [];
  for (let i = 1; i < kids.length; i++) {
    const g = Math.round(kids[i].getBoundingClientRect().top - kids[i - 1].getBoundingClientRect().bottom);
    gaps.push(`${label(kids[i - 1])} → ${label(kids[i])}: ${g}px`);
  }

  return {
    width: innerWidth, checked: SCOPE || 'main content', textElements: texts.length, fontSizes: sizes,
    textUnder16px: small.slice(0, 10), tightLineHeight: tight.slice(0, 10), longLines: longLines.slice(0, 10),
    lowContrast: lowContrast.slice(0, 10), touchTargetsUnder24px: tiny.slice(0, 10), sidewaysScroll: overflow,
    gaps: gaps.slice(0, 20),
  };
})()
