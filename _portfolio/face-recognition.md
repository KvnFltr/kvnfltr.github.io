---
title: "Supervised Face Recognition"
excerpt: "Full pipeline: detection → alignment → encoding → classification (97% test accuracy).<br/><img src='/images/face-extract.png' alt='Face extraction example' width='500'/>"
collection: portfolio
permalink: /portfolio/face-recognition/
---

Course project in **AI & Deep Learning** at **ESIEE Paris**, co-authored with **Lubin Benoit** and supervised by **Prof. Laurent Najman**.  
We built an end-to-end **face recognition** pipeline—from raw images to identities—then measured the impact of each stage.

<p>
  <a class="btn btn--primary" href="https://github.com/KvnFltr/face-recognition" target="_blank" rel="noopener">GitHub code</a>
  <a class="btn" href="/files/rapport_face_recognition.pdf" target="_blank" rel="noopener">Project report (PDF, fr)</a>
</p>

### Problem & data
Two datasets:
- **Jurassic Park characters** (≈218 images) used to design and ablate the pipeline.  
- A **personal dataset** (10 people, 50–110 photos each) to check generalization and bias.

### Pipeline (what we compared)
1. **Detection** — dlib HOG vs **CNN** detector; we crop and resize faces to **128×128**.  
2. **Pose/Alignment** — facial **landmarks** (5/68 pts) + affine align; reduces pose variance.  
3. **Encoding** — 128-D **embeddings** (OpenFace-style) for compact, robust features.  
4. **Classification** — **Logistic Regression**, **Linear SVM**, **kNN**, and a small **NN**.

**Headline result:** with embeddings, several classifiers reach **~97% accuracy** on test;  
**Logistic Regression** and **Linear SVM** are the **fastest** at inference (ms range).

---

<figure>
  <img src="/images/face-extract.png" alt="Face detection and crop" width="980">
  <figcaption><strong>Figure 1.</strong> Detection & crop before any alignment.</figcaption>
</figure>

---

<figure>
  <img src="/images/conv-4vs1.png" alt="CNN depth ablation: 4 conv layers vs 1" width="980">
  <figcaption><strong>Figure 2.</strong> Ablation on CNN depth (without encoding). Fewer layers converged faster on this small dataset.</figcaption>
</figure>

---

<figure>
  <img src="/images/align-before-after.png" alt="Alignment via facial landmarks" width="980">
  <figcaption><strong>Figure 3.</strong> Alignment with landmarks—reduces pose variance before training.</figcaption>
</figure>

---

<figure>
  <img src="/images/align-vs-noalign.png" alt="Effect of alignment on validation curves" width="980">
  <figcaption><strong>Figure 4.</strong> With alignment (right) vs without (left): cleaner validation dynamics.</figcaption>
</figure>

---

<figure>
  <img src="/images/encode-vs-not.png" alt="Embeddings vs raw pixels" width="980">
  <figcaption><strong>Figure 5.</strong> Using 128-D embeddings pushes test accuracy to ~97% and stabilizes training.</figcaption>
</figure>

---

<figure>
  <img src="/images/models-compare.png" alt="Classifier comparison: Logistic, SVM, kNN, NN" width="980">
  <figcaption><strong>Figure 6.</strong> Classifier comparison (same embeddings): all ~97% accuracy; Logistic/SVM are the quickest.</figcaption>
</figure>

---

<figure>
  <img src="/images/f1-per-class.png" alt="Per-class F1 scores on personal dataset" width="980">
  <figcaption><strong>Figure 7.</strong> Per-class F1 on the personal dataset—balanced scores, no obvious single-class collapse.</figcaption>
</figure>

### Notes & takeaways
- **Alignment** helps shallow convnets; deep models were already robust on this scale.  
- **Embeddings** remove background/lighting noise and make simple classifiers shine.  
- **Speed matters:** for deployment, **LogReg/SVM** give near-NN accuracy with far lower latency.  
- **Bias check:** with a more varied personal set, accuracy stays high (≈94–98%), but performance depends on data quality and diversity—worth monitoring if scaled.

