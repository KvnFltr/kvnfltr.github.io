---
title: "Supervised Face Recognition"
excerpt: "Detection, alignment and embedding ablations; approximately 97% test accuracy on a small coursework dataset."
collection: portfolio
permalink: /portfolio/face-recognition/
---

An **AI & Deep Learning** project at **ESIEE Paris**, built with **Lubin Benoit** and supervised by **Prof. Laurent Najman**. We compared the stages of a face-recognition pipeline and their effect on classification accuracy and inference time.

<p>
  <a class="btn btn--primary" href="https://github.com/KvnFltr/face-recognition" target="_blank" rel="noopener">Source code</a>
  <a class="btn" href="/files/rapport_face_recognition.pdf" target="_blank" rel="noopener">Report (PDF, French)</a>
</p>

### Approach

- Compared **dlib HOG and CNN detection**, followed by 128 × 128 face crops.
- Evaluated facial-landmark alignment and **128-dimensional pretrained embeddings** against image-based classifiers.
- Compared **logistic regression, linear SVM, k-nearest neighbors and a neural network** on the same encoded data.

The first dataset contains approximately **218 images of Jurassic Park characters**. A second dataset contains **10 identities with 50–110 images each**, used to examine performance under more varied imaging conditions.

### Results and limitations

The report records approximately **97% test accuracy** with embeddings on the first dataset. Logistic regression and linear SVM achieved similar accuracy to the neural classifier with lower measured inference time in these experiments.

On the second dataset, logistic regression obtained **94–98% test accuracy across random splits**. The report notes that the highest test scores coincided with lower validation performance, suggesting sensitivity to which examples entered each split. These are small, closed-set coursework experiments, not evidence of generalization to unseen identities or of demographic fairness.

<figure>
  <img src="/images/models-compare.png" alt="Reported accuracy and inference-time comparison for four classifiers using the same face embeddings" width="1006" height="168" loading="lazy" decoding="async">
  <figcaption>Classifier comparison from the project report.</figcaption>
</figure>

<figure>
  <img src="/images/align-before-after.png" alt="Face crops before and after landmark-based alignment" width="1040" height="552" loading="lazy" decoding="async">
  <figcaption>Landmark-based alignment, one of the pipeline stages evaluated.</figcaption>
</figure>

**Tools:** Python, dlib, neural networks, scikit-learn.
