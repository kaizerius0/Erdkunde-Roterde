from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update CSS
css_old_slide = """    .slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      padding: var(--layout-pad-y) var(--layout-pad-x);
      padding-top: 100px;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.5s ease, transform 0.5s ease;
      transform: translateX(40px);
    }"""
css_new_slide = """    .slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      padding: 60px var(--layout-pad-x) 40px var(--layout-pad-x);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.5s ease, transform 0.5s ease;
      transform: translateX(40px);
    }"""
html_content = html_content.replace(css_old_slide, css_new_slide)

css_old_inner = """    .slide-inner {
      max-width: var(--layout-max-width);
      width: 100%;
    }"""
css_new_inner = """    .slide-inner {
      max-width: var(--layout-max-width);
      width: 100%;
      height: 100%;
      display: grid;
      grid-template-rows: 40px 100px 1fr;
      grid-template-areas: "zone-a" "zone-b" "zone-c";
      row-gap: 16px;
      align-items: start;
    }
    
    .slide.title-center .slide-inner {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    
    .zone-a {
      grid-area: zone-a;
      display: flex;
      align-items: flex-start;
    }
    .zone-b {
      grid-area: zone-b;
      display: flex;
      align-items: flex-start;
    }
    .zone-c {
      grid-area: zone-c;
      width: 100%;
      height: 100%;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }
    .zone-c.center-v {
      justify-content: center;
    }"""
html_content = html_content.replace(css_old_inner, css_new_inner)

css_old_badge = """    .section-badge {
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: var(--accent-soft);
      background: var(--accent-glow);
      border: 1px solid rgba(192, 57, 43, 0.4);
      padding: 6px 18px;
      border-radius: 20px;
      margin-bottom: var(--spacing-badge-to-title);
    }"""
css_new_badge = """    .section-badge {
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: var(--accent-soft);
      background: var(--accent-glow);
      border: 1px solid rgba(192, 57, 43, 0.4);
      padding: 6px 18px;
      border-radius: 20px;
      margin-bottom: 0;
    }"""
html_content = html_content.replace(css_old_badge, css_new_badge)

css_old_h2 = """    .slide h2 {
      font-size: 2.2rem;
      font-weight: 600;
      line-height: 1.25;
      margin-bottom: var(--spacing-title-to-content);
      color: var(--text);
    }"""
css_new_h2 = """    .slide h2 {
      font-size: 2.2rem;
      font-weight: 600;
      line-height: 1.25;
      margin-bottom: 0;
      color: var(--text);
    }"""
html_content = html_content.replace(css_old_h2, css_new_h2)

css_old_grid2 = """    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
    }"""
css_new_grid2 = """    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
      height: 100%;
      align-items: stretch;
    }"""
html_content = html_content.replace(css_old_grid2, css_new_grid2)

css_old_grid3 = """    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
    }"""
css_new_grid3 = """    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
      height: 100%;
      align-items: stretch;
    }"""
html_content = html_content.replace(css_old_grid3, css_new_grid3)

css_old_gridcards = """    .grid-3 .card,
    .grid-2 .card {
      background: var(--surface);
      border-radius: var(--card-radius);
      padding: var(--card-padding);
      text-align: center;
    }"""
css_new_gridcards = """    .grid-3 .card,
    .grid-2 .card {
      background: var(--surface);
      border-radius: var(--card-radius);
      padding: var(--card-padding);
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      height: 100%;
    }"""
html_content = html_content.replace(css_old_gridcards, css_new_gridcards)

css_old_compare = """    .compare {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
    }"""
css_new_compare = """    .compare {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-content-gap);
      width: 100%;
      height: 100%;
      align-items: stretch;
    }"""
html_content = html_content.replace(css_old_compare, css_new_compare)

css_old_compare_card = """    .compare-card {
      background: var(--surface);
      border-radius: var(--card-radius);
      padding: var(--card-padding);
      border-top: 3px solid var(--accent);
    }"""
css_new_compare_card = """    .compare-card {
      background: var(--surface);
      border-radius: var(--card-radius);
      padding: var(--card-padding);
      border-top: 3px solid var(--accent);
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      height: 100%;
    }"""
html_content = html_content.replace(css_old_compare_card, css_new_compare_card)

css_old_layout_split = """    .layout-split {
      display: flex;
      gap: var(--spacing-columns-gap);
      align-items: center;
      width: 100%;
    }"""
css_new_layout_split = """    .layout-split {
      display: flex;
      gap: var(--spacing-columns-gap);
      align-items: flex-start;
      width: 100%;
      height: 100%;
      flex-direction: row;
    }"""
html_content = html_content.replace(css_old_layout_split, css_new_layout_split)

css_old_layout_split_rev = """    .layout-split-reverse {
      display: flex;
      gap: var(--spacing-columns-gap);
      align-items: center;
      width: 100%;
      flex-direction: row-reverse;
    }"""
css_new_layout_split_rev = """    .layout-split-reverse {
      display: flex;
      gap: var(--spacing-columns-gap);
      align-items: flex-start;
      width: 100%;
      height: 100%;
      flex-direction: row-reverse;
    }"""
html_content = html_content.replace(css_old_layout_split_rev, css_new_layout_split_rev)

css_old_layout_centered = """    /* Centered content blocks keep left-aligned text for bullets */
    .layout-centered .bullets,
    .content-centered.bullets {
      text-align: left;
      margin-bottom: var(--spacing-content-gap);
    }"""
css_new_layout_centered = """    /* Centered content blocks keep left-aligned text for bullets */
    .layout-centered .bullets,
    .content-centered.bullets {
      text-align: left;
      margin-bottom: var(--spacing-content-gap);
    }
    
    .zone-c > .content-centered {
      margin-left: auto;
      margin-right: auto;
      width: 100%;
      max-width: 800px;
    }
    
    .zone-c > .cycle {
      margin-bottom: 30px;
    }"""
html_content = html_content.replace(css_old_layout_centered, css_new_layout_centered)

css_old_image_zone = """    .image-zone {
      text-align: center;
    }"""
css_new_image_zone = """    .image-zone {
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      height: 100%;
    }"""
html_content = html_content.replace(css_old_image_zone, css_new_image_zone)

css_old_img = """    .image-zone img {
      width: 100%;
      border-radius: var(--card-radius);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }"""
css_new_img = """    .image-zone img {
      width: 100%;
      max-height: 480px;
      object-fit: contain;
      border-radius: var(--card-radius);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }"""
html_content = html_content.replace(css_old_img, css_new_img)

# Parsing with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

slides = soup.find_all('div', class_='slide')

for slide in slides:
    slide_inner = slide.find('div', class_='slide-inner')
    if not slide_inner: continue
    
    # We only want to restructure content slides, not the title slide
    if 'title-center' in slide.get('class', []):
        continue

    # Create the zone tags using bs4
    zone_a = soup.new_tag('div', attrs={'class': 'zone-a'})
    zone_b = soup.new_tag('div', attrs={'class': 'zone-b'})
    
    c_classes = ['zone-c']
    if 'layout-centered' in slide_inner.get('class', []):
        c_classes.append('center-v')
    zone_c = soup.new_tag('div', attrs={'class': ' '.join(c_classes)})
    
    # We will extract all elements inside slide_inner
    elements = []
    
    # Because iterating and modifying children is tricky, we extract them first
    # We find immediate children
    for child in list(slide_inner.children):
        elements.append(child)
        child.extract()
    
    for child in elements:
        # Check if it's whitespace string
        if isinstance(child, str) and not child.strip():
            continue
            
        # Put <span class="section-badge"> into zone_a
        if getattr(child, 'name', None) == 'span' and 'section-badge' in child.get('class', []):
            zone_a.append(child)
        # Put <h2> into zone_b
        elif getattr(child, 'name', None) == 'h2':
            zone_b.append(child)
        # Everything else goes into zone_c
        else:
            zone_c.append(child)
            
    slide_inner.append(zone_a)
    slide_inner.append(zone_b)
    slide_inner.append(zone_c)

# We want to format HTML slightly nicer without altering `pre`/`code` behaviors, bs4 `.prettify()` sometimes breaks spacing
# Since we just used html.parser, str(soup) is mostly identical to source for un-modified blocks.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("DOM restructuring successfully done with BeautifulSoup.")
