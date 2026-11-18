import { test } from 'node:test';
import assert from 'node:assert/strict';
import { sectionize, headingText } from '../src/lib/sectionize.mjs';

test('preserves content, heading links, references and change log', () => {
  const input = '<p>Lead paragraph</p><h2 id="abstract">Abstract</h2><p>One</p>' +
    '<h2 id="company-review">Company Review</h2><h3 id="ownership">Ownership &amp; control</h3><p>Two</p>' +
    '<h2 id="references">References</h2><p>[S01]</p>' +
    '<h2 id="change-log">Change log</h2><ul><li>v1.2</li></ul>';
  const {intro, sections, collapsible} = sectionize(input);
  assert.equal(intro, '<p>Lead paragraph</p>');
  assert.equal(sections.length, 4);
  assert.equal(sections[1].title, 'Company Review');
  assert.deepEqual(sections[1].subsections, [{id:'ownership',title:'Ownership & control'}]);
  assert.equal(sections[2].id,'references');
  assert.equal(sections[3].id,'change-log');
  assert.ok(sections[3].contentHtml.includes('v1.2'));
  assert.equal(collapsible,true);
  assert.ok(!sections[0].headingHtml.includes('id="abstract"'));
  assert.equal(sections.map(s=>s.contentHtml.match(/<p|<ul/g)?.length || 0).reduce((a,b)=>a+b,0),4);
});

test('short content is not collapsed', () => {
  assert.equal(sectionize('<p>hello</p>').intro,'<p>hello</p>');
  assert.equal(sectionize('<h2 id="one">One</h2><h2 id="two">Two</h2>').collapsible,false);
});

test('missing ids get unique slugs, preserving body', () => {
  const x=sectionize('<h2>Results &amp; notes</h2><p>One</p><h2>Results &amp; notes</h2><p>Two</p>');
  assert.deepEqual(x.sections.map(s=>s.id),['results-notes','results-notes-2']);
  assert.ok(x.sections[1].contentHtml.includes('Two'));
});

test('heading text decodes numeric and common entities', () => {
  assert.equal(headingText('Strategy &amp; growth &#8212; <em>notes</em>'),'Strategy & growth — notes');
});
