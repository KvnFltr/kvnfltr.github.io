---
title: "Environmental Data Pipeline & Dashboard"
excerpt: "Python ingestion, geospatial joins and a Plotly Dash interface for 171,545 environmental measurements across 395 municipalities."
collection: portfolio
permalink: /portfolio/rain-gamma-spikes/
---

A **Data Engineering & Scientific Computing** team project at **ESIEE Paris**. We built a pipeline and dashboard to explore environmental radioactivity measurements alongside rainfall data in metropolitan France.

<p>
  <a class="btn btn--primary" href="https://github.com/KvnFltr/rain-gamma-spikes-france" target="_blank" rel="noopener">Source code &amp; setup</a>
  <a class="btn" href="https://drive.google.com/file/d/1WO46rHsxPQDHV1-Di-vbB5CeSbxnhrkD/view" target="_blank" rel="noopener">Video walkthrough</a>
</p>

### Data and implementation

The project combines **RNM/ASNR soil and water sample measurements**, **Météo-France precipitation data**, and a **municipality gazetteer**. The documented cleaned dataset contains **171,545 records across 395 municipalities**, from January 2020 to January 2025.

Three CLI commands separate ingestion, transformation and presentation:

1. **Download:** Playwright-based collection and CSV ingestion into a raw-data directory.
2. **Clean:** municipality-name normalization, Lambert-93 to WGS84 coordinate conversion with pyproj, and nearest-neighbor spatial joins with scikit-learn’s BallTree.
3. **Dashboard:** a Plotly Dash application with maps, date filters, distributions and measurement-count views.

### My contribution

I designed the CLI and repository structure, implemented the data ingestion and cleaning pipeline, and contributed to the dashboard layout and callbacks.

### Interpretation limits

This is an exploratory data-engineering project. Radioactivity results must be compared within compatible **units, radionuclides and sample media**: Bq/kg and Bq/L are activity concentrations, not radiation doses. Sampling campaigns and the distance between weather and sample locations also affect interpretation. The dashboard does not establish that rainfall causes changes in radioactivity.

<figure>
  <img src="/images/rain-spikes-count.png" alt="Dashboard time series showing the number of environmental measurements collected over time" width="712" height="472" loading="lazy" decoding="async">
  <figcaption>Measurement coverage varies over time; the dashboard makes that sampling pattern visible.</figcaption>
</figure>

**Tools:** Python, pandas, NumPy, Playwright, pyproj, scikit-learn, Plotly Dash.
