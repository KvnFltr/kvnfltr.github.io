---
title: "Rain & Dust Spikes Dashboard"
excerpt: "Interactive event-study of gamma-dose spikes after rainfall in metropolitan France (2020–2025).<br/><img src='/images/rain-spikes-hist.png' alt='Radioactivity vs rainfall histogram' width='500'/>"
collection: portfolio
permalink: /portfolio/rain-gamma-spikes/
---

Project in **Data Engineering & Scientific Computing** at **ESIEE Paris**, co-authored with two classmates.  
We built an end-to-end pipeline and dashboard to study how rainfall is associated with gamma-radiation “spikes” across metropolitan France.

<p>
  <a class="btn btn--primary" href="https://github.com/KvnFltr/rain-gamma-spikes-france" target="_blank" rel="noopener">GitHub code</a>
</p>

<figure class="video">
  <video controls width="980" poster="/images/rain-spikes-hist.png">
    <source src="/videos/rain-gamma-spikes-demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <figcaption><strong>Demo.</strong> Walkthrough of the Rain &amp; Dust Spikes Dashboard.</figcaption>
</figure>

### Problem & data

Goal: analyse whether **rain events** (mm/day) correlate with **higher gamma doses** measured by the French monitoring network.

We combined three open datasets:

- **Gamma radiation (ASNR / mesure-radioactivite.fr)** – soil and water samples with radionuclide, unit, environment and GPS coordinates.  
- **Weather (Météo-France SYNOP)** – daily precipitation totals (rain/snow), originally in **Lambert-93** coordinates.  
- **Municipality gazetteer** – commune names, population and fallback coordinates to complete missing metadata.

After cleaning and joins, the final dataset contains **171,545 measurements** between **2020-01-01** and **2025-01-01** over **395 municipalities**.

### Pipeline & architecture

The repository is organised around a small **CLI**:

1. `python main.py download`  
   Scrape ASNR with **Playwright** (headless Chromium) and download the SYNOP + gazetteer CSVs into `data/raw/`.

2. `python main.py clean`  
   - Project Lambert-93 → WGS84 with **pyproj**.  
   - Standardise municipality names (unidecode).  
   - Join radiation and weather with a **BallTree** nearest-neighbour search (scikit-learn).  
   - Export a single cleaned file `data/cleaned/data.csv` (16 columns).

3. `python main.py dashboard`  
   Start the **Plotly Dash** server, load the cleaned dataset once, serialise it, then build all views and callbacks.

The app can run locally or on a remote VM (port 8050, static assets in `src/assets`, layouts/components in `src/dashboard` and `src/components`).

### Dashboard (what the user sees)

Key interactive views:

- **Radioactivity distribution: dry vs rainy days**  
  Histograms comparing soil / water gamma doses on dry days vs days above a configurable rainfall threshold.

- **Rainfall vs radioactivity scatterplot**  
  Log-scale scatter of daily rainfall vs gamma result (soil or water), with unit and Y-scale toggles.

- **Geolocated monitoring stations map**  
  All stations plotted over France with markers coloured by gamma dose, filterable by year and month.

- **Radioactivity by rainfall class (boxplot)**  
  Dose distributions for rainfall classes (0 / 1–5 / 5–10 / >10 mm).

- **Daily measurements count**  
  Time-series of the number of radiation measurements collected each day from 2020 to 2025.

---

<figure>
  <img src="/images/rain-spikes-hist.png" alt="Radioactivity distribution on dry vs rainy days" width="980">
  <figcaption><strong>Figure 1.</strong> Histogram of soil/water radioactivity on dry vs rainy days with adjustable rainfall threshold.</figcaption>
</figure>

---

<figure>
  <img src="/images/rain-spikes-scatter.png" alt="Scatterplot of rainfall vs radioactivity" width="980">
  <figcaption><strong>Figure 2.</strong> Scatter of daily rainfall vs gamma dose (log scale), revealing moderate correlation but strong local variability.</figcaption>
</figure>

---

<figure>
  <img src="/images/rain-spikes-map.png" alt="Geolocated monitoring stations in France" width="980">
  <figcaption><strong>Figure 3.</strong> Map of monitoring stations coloured by gamma dose, with filters by year and month.</figcaption>
</figure>

---

<figure>
  <img src="/images/rain-spikes-boxplot.png" alt="Boxplot of radioactivity by rainfall class" width="980">
  <figcaption><strong>Figure 4.</strong> Boxplots of gamma dose for rainfall classes (0 / 1–5 / 5–10 / &gt;10 mm).</figcaption>
</figure>

---

<figure>
  <img src="/images/rain-spikes-count.png" alt="Daily measurement counts over time" width="980">
  <figcaption><strong>Figure 5.</strong> Daily number of measurements between 2020 and 2025, showing campaign intensity over time.</figcaption>
</figure>

### Main findings

- Heavy rain events (≥5 mm/day) are relatively rare (~14% of observations) but show a **slightly higher median gamma dose** (~1.1 Bq vs 0.94 Bq on drier days).  
- **Soil** samples have higher median doses (~1.4 Bq/kg dry) than **water** (~0.52 Bq/L), consistent with stronger radionuclide retention in soil.  
- The top decile of radioactivity measurements occurs on rainy days in roughly the same proportion as overall rain frequency (~31%), suggesting that **extreme spikes** depend more on local site characteristics than on rainfall alone.

### My role & tech stack

**My contributions**

- Designed the overall **CLI architecture** (`download → clean → dashboard`) and repository structure.  
- Implemented most of the **data engineering pipeline** (Playwright scraping, coordinate projection, BallTree joins, cleaning logic).  
- Co-designed the **Dash layout and callbacks**, including the rainfall-class boxplots and dry vs rainy histograms.  
- Wrote the final **analysis summary** and interpretation used in the report and presentation.

**Technologies**

- Python 3.11, pandas, numpy, scikit-learn (BallTree), pyproj, Playwright  
- Plotly Dash, HTML/CSS for layout  
- Git, virtual environments, CLI tooling
