# Arbuzova Beauty — Next Steps

## Context

We have 32,814 deep-parsed keywords from Yandex Wordstat (via XMLRiver API) categorized into 10 categories. We built initial sitemaps for service pages (29 pages), shape pages (9), color pages (18), design pages (24), and homepage/geo pages (10). However, the current data has a critical limitation: **Wordstat search volumes represent the keyword + all its variations combined, not exact match searches**. This inflates volumes and makes it impossible to accurately assess individual keyword demand.

Files in `/Users/egordriagin/Dev/arbuzova-beauty/`:
- `deep_parse_results.xlsx` — 32,814 keywords with categories (column C)
- `wordstat_top_queries.xlsx` — original 2,001 seed queries
- `sitemap_service_pages.xlsx` — 29 service pages, 882 keywords
- `sitemap_homepage_geo.xlsx` — 10 pages
- `sitemap_shape_pages.xlsx` — 9 pages (needs rebuild with full keyword lists)
- `sitemap_color_pages.xlsx` — 18 pages (needs rebuild with full keyword lists)
- `sitemap_design_pages.xlsx` — 24 pages (needs rebuild with full keyword lists)
- `negative_keywords.txt` — 393 negative keywords

API credentials: XMLRiver key=`bce323aab1cfc1fc05e7e7bb46cdd1c12082e84d`, user=`14967`

## Step 1 — Get exact match search volumes from Yandex Direct

**Problem:** Wordstat volumes are "broad match" — "маникюр" shows ~3M because it includes every query containing that word. We need exact match frequencies to know how many people actually search for "маникюр" specifically vs "маникюр на короткие ногти".

**Action:** Use Yandex Direct API (or a service that wraps it) to pull exact match search volumes for all 32,814 keywords. Yandex Direct's keyword forecasting tool provides exact phrase frequency data. This will give us accurate demand numbers per keyword.

**Outcome:** Updated `deep_parse_results.xlsx` with a new column for exact match volume alongside the current broad match volume.

## Step 2 — Analyze top 10 SERP to classify commercial vs informational intent

**Problem:** We currently guess intent from keyword text alone. "Маникюр фото" could be commercial (gallery on a salon site) or informational (Pinterest browsing). The actual SERP tells the truth — if 8/10 results are salon websites, it's commercial; if 8/10 are blogs/Pinterest/YouTube, it's informational.

**Action:** For each keyword (or at least the top ~2,000-3,000 by exact volume), fetch the top 10 Yandex SERP results and analyze:
- What types of pages rank: commercial (salon sites, aggregators like profi.ru, zoon.ru) vs informational (blogs, Pinterest, YouTube, forums)
- The ratio determines intent classification: commercial, informational, or mixed
- Note which specific URLs/domains appear

**Options:**
- Use an existing SERP analysis service (e.g., SEMrush, Ahrefs, or Russian equivalents like Serpstat, Keys.so, Topvisor)
- Build our own tool: scrape Yandex SERPs via API or proxy, classify each result by domain type

**Outcome:** Each keyword gets an intent label (commercial / informational / mixed) based on real SERP data, not guesswork.

## Step 3 — Identify top competitor websites from SERP data

**Problem:** We don't know which real competitors dominate the маникюр search space in SPB, what their site structure looks like, or what services they offer.

**Action:** From the SERP data collected in Step 2:
- Count which commercial domains appear most frequently across all queries
- Filter out aggregators (profi.ru, zoon.ru, yandex maps, etc.) — focus on real salon/beauty service websites
- For the top 5-10 competitor sites, analyze:
  - Their sitemap / site structure (what pages they have)
  - What services they list
  - How they group content (service pages vs blog vs gallery vs geo pages)
  - Their URL structure and page hierarchy

**Outcome:** A competitor analysis document listing the top competitors, their site structures, and what we can learn from them for our own architecture.

## Step 4 — Rebuild keyword grouping and sitemap using real data

**Problem:** Our current groupings were built on broad match volumes and text-based intent guessing. With exact volumes, SERP-based intent classification, and competitor site structures, we can build a much more accurate sitemap.

**Action:**
- Split the keyword set into commercial and informational:
  - **Commercial keywords** → map to service/product pages on the website
  - **Informational keywords** → map to blog posts, guides, FAQ pages
- Use competitor sitemaps as reference for page structure and hierarchy
- Group commercial keywords into pages based on:
  - Actual search demand (exact match volumes)
  - SERP similarity (keywords that show the same top results belong on the same page)
  - Competitor page structure (if competitors have a dedicated page for X, we probably need one too)
- Group informational keywords into content clusters for the blog

**Outcome:** Final sitemap with:
- Commercial pages (services, geo, pricing) backed by real demand data
- Blog/content pages for informational queries
- Each page mapped to its exact-match keywords with verified intent
- Priority based on actual search volume, not inflated broad match numbers
