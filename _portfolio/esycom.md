---
title: "CNRS / ESYCOM: Energy harvesting with TENG"
excerpt: "Conditioning a triboelectric nanogenerator (TENG) to power a BLE node: Bennet doubler → hysteresis switch → DC-DC → regulator.<br/><img src='/images/esycom-schematic.png' alt='ESYCOM schematic' width='520'/>"
collection: portfolio
permalink: /portfolio/esycom-teng/
---

**Role.** 4-week research intern at **CNRS / ESYCOM (UMR 9007)**  
**Supervisor.** [Prof. Philippe Basset](https://perso.esiee.fr/~bassetp/)
**Goal.** Simulate and validate a **conditioning chain** for a **Triboelectric Nanogenerator (TENG)** that harvests mechanical energy (vehicle pass) and **powers a BLE transmission** to a smartphone.

**Reference.** Nature Communications — *Employing a MEMS plasma switch for conditioning high-voltage kinetic energy harvesters*  
<p>
  <a class="btn btn--primary" href="https://www.nature.com/articles/s41467-020-17019-5" target="_blank" rel="noopener">Nature article</a>
  <a class="btn" href="/files/rapport_esycom.pdf" target="_blank" rel="noopener">Report (PDF, FR)</a>
  <a class="btn" href="/files/presentation_esycom.pptx" target="_blank" rel="noopener">Slides (PPTX)</a>
  <!-- Optional if available -->
  <!-- <a class="btn" href="/files/teng-ltspice.zip" target="_blank" rel="noopener">LTspice project</a>
  <a class="btn" href="/files/teng-measurements.csv" target="_blank" rel="noopener">Measurements (CSV)</a> -->
</p>

---

### Problem
TENGs output **high-voltage, low-current, pulsed** waveforms, not directly usable by electronics. We adapt a two-stage architecture to reach a regulated **≈3.3–3.6 V** for BLE.

**Chain.** **Bennet doubler → hysteresis switch → step-down DC-DC → regulator → load**

---

### Contributions
- **Modeled** the full path in **LTspice** with parametric sweeps:
  - Bennet doubler: diode type and capacitance vs. charging efficiency
  - Hysteresis thresholds: switching stability and burst timing
  - Storage & DC-DC: ripple vs. **time-to-start**
- **Built** a bench prototype; **probed** nodes **M, N, P, Q**; captured oscilloscope traces
- **Ran field tests** with **vehicle pass**; tuned alignment/pressure for repeatability
- **Derived operating windows** to meet the **3.3 V** BLE boot requirement
- **Recommended**: improved mechanical fixture, lower-drop diodes, DC-DC **soft-start**

---

### Results (selected)
- **Node N** shows **sawtooth charge** then **burst discharge** at hysteresis trigger, matching the target switching envelope.  
- **Output Q** stabilizes at **≈3.3 V** under representative BLE load, sufficient for bring-up.  
- **Variance driver** is **mechanical coupling**: small ramp pressure/position changes markedly affect harvested energy.  
- **Trade-off** documented between storage sizing and start-up latency; guidance provided for capacitor ranges.

> Replication details, LTspice schematics, and measurement tables are in the report; downloadable assets can be added above if allowed.

---

### Approach
1) **Modeling** — End-to-end LTspice with sweeps  
2) **Measurement** — Bench prototype, scope at **M/N/P/Q**  
3) **Field test** — Vehicle pass over ramp, repeatability tuning

---

<figure>
  <img src="/images/esycom-schematic.png" alt="Conditioning chain: Bennet doubler → hysteresis switch → step-down DC-DC → regulator → load" width="980">
  <figcaption><strong>Figure 1.</strong> Conditioning chain with probe nodes <em>M, N, P, Q</em>.</figcaption>
</figure>

<figure>
  <img src="/images/esycom-device.png" alt="Energy-harvesting ramp used for vehicle pass tests" width="980">
  <figcaption><strong>Figure 2.</strong> Energy-harvesting ramp for vehicle-pass tests.</figcaption>
</figure>

<figure>
  <img src="/images/esycom-nodeN.png" alt="LTspice: voltage at node N" width="980">
  <figcaption><strong>Figure 3.</strong> LTspice — Node <em>N</em> sawtooth charge prior to switching.</figcaption>
</figure>

<figure>
  <img src="/images/esycom-output.png" alt="LTspice: regulated output Q ≈ 3.3 V" width="980">
  <figcaption><strong>Figure 4.</strong> LTspice — Regulated output <em>Q</em> ≈ 3.3 V for BLE node.</figcaption>
</figure>

<figure>
  <img src="/images/esycom-bench.png" alt="Bench prototype of the conditioning circuit" width="980">
  <figcaption><strong>Figure 5.</strong> Bench prototype and scope captures.</figcaption>
</figure>

<figure>
  <img src="/images/esycom-teng.png" alt="Triboelectric Nanogenerator (TENG) element" width="980">
  <figcaption><strong>Figure 6.</strong> Triboelectric Nanogenerator (TENG) element.</figcaption>
</figure>
