/** Server-side navigation and disclosure sections for trusted Astro-rendered Markdown. */
const HEADING = /<h2\b([^>]*)>([\s\S]*?)<\/h2>/gi;
const SUBHEADING = /<h3\b([^>]*)>([\s\S]*?)<\/h3>/gi;
const ID = /\bid\s*=\s*(["'])(.*?)\1/i;
const NAMED = {amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' '};

export function headingText(html) {
  return html.replace(/<[^>]+>/g, '')
    .replace(/&(#(?:x[0-9a-f]+|[0-9]+)|[a-z]+);/gi, (full, entity) => {
      if (entity.startsWith('#')) {
        const hex = /^#x/i.test(entity);
        const point = Number.parseInt(entity.slice(hex ? 2 : 1), hex ? 16 : 10);
        return Number.isFinite(point) && point > 0 && point <= 0x10ffff
          ? String.fromCodePoint(point) : full;
      }
      return NAMED[entity.toLowerCase()] ?? full;
    })
    .replace(/\s+/g, ' ').trim();
}

function slugify(label) {
  return label.normalize('NFKD').toLowerCase()
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim().replace(/\s+/g, '-').replace(/-+/g, '-') || 'section';
}

function headings(html, pattern) {
  const re = new RegExp(pattern.source, pattern.flags);
  const matches = [];
  for (const match of html.matchAll(re)) {
    matches.push({ full: match[0], attrs: match[1], inner: match[2], index: match.index,
      title: headingText(match[2]), id: match[1].match(ID)?.[2] ?? null });
  }
  return matches;
}

/** Keeps original headings and body HTML intact; wraps H2 chapters with <details>. */
export function sectionize(html) {
  const top = headings(html, HEADING);
  if (!top.length) return { intro: html, sections: [], collapsible: false };
  const used = new Set(top.map(item => item.id).filter(Boolean));
  const sections = top.map((item, i) => {
    let id = item.id;
    if (!id) {
      const slug = slugify(item.title);
      id = slug;
      for (let suffix = 2; used.has(id); suffix++) id = slug + '-' + suffix;
      used.add(id);
    }
    const end = top[i + 1]?.index ?? html.length;
    const body = html.slice(item.index + item.full.length, end);
    const subs = headings(body, SUBHEADING).filter(child => child.id)
      .map(child => ({ id: child.id, title: child.title }));
    const cleanAttrs = item.attrs.replace(ID, '').trim();
    const headingHtml = '<h2' + (cleanAttrs ? ' ' + cleanAttrs : '') + '>' + item.inner + '</h2>';
    return { id, title: item.title, headingHtml, contentHtml: body, subsections: subs };
  });
  return { intro: html.slice(0, top[0].index), sections, collapsible: sections.length >= 3 };
}
