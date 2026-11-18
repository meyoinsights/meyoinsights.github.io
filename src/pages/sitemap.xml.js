export const prerender = true;
export function GET({site}) {
  const root = site ?? new URL('https://meyoinsights.github.io/');
  const articles = Object.values(import.meta.glob('./blog/*.md',{eager:true}));
  const routes = ['/', '/blog/', '/about/', '/process/', '/behind-the-research/', ...articles.filter(a=>!a.frontmatter?.archived && a.url).map(a=>a.url)];
  const escape = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  return new Response('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+[...new Set(routes)].map(path=>'<url><loc>'+escape(new URL(path,root).href)+'</loc></url>').join('')+'</urlset>',{headers:{'Content-Type':'application/xml'}});
}
