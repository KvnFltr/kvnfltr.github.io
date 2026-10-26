---
title: "morseq — Topological image segmentation"
permalink: /portfolio/morseq/
excerpt: "Single-pass basin labeling in discrete Morse sequences, with a pure-Python implementation and 623 automated tests."
description: "Research at LIGM–CNRS: one-pass basin labeling, grayscale cuts and a tested Python library."
featured: true
order: 1
category_label: "Research · LIGM, CNRS UMR 8049 · 2026"
---

Research at **LIGM, CNRS UMR 8049**, with Laurent Najman, Gilles Bertrand and Jean Cousty. The project studies image segmentation through **discrete Morse sequences**: a representation that connects a cell complex, its gradient field and its critical cells.

[Source code and documentation](https://github.com/KvnFltr/morseq)

## Contribution

I developed a **single-pass basin-labeling algorithm**. Instead of repeatedly expanding each basin, the algorithm scans a Morse sequence once. The required faces of a regular pair precede it in the sequence, so labels can be propagated in order.

The labeling pass is **linear in the incidence structure**, given a Morse sequence. For suitable flooding sequences, the labels restrict consistently to grayscale cuts. Plateaus are handled without perturbing the image values.

## Implementation & verification

The public **morseq** library implements cubical and simplicial complexes, gradient fields, stable and unstable sets, basins and cuts in Python, with no core runtime dependencies. It includes a command-line interface and 2D/3D image-segmentation examples.

The **623-test suite** checks the implementation against definitions and structural properties, including:

- Agreement between one-pass basin labeling and explicit closure.
- Independence from the order of allowed expansions.
- Basin disjointness and consistency under prefixes and cuts.
- Boundary composition, path parity and Euler-characteristic identities.

Tests cover cubical and simplicial examples and randomly generated acyclic fields. They check implementation behavior and complement the mathematical reasoning.

## Scope

The focus is algorithmic correctness and the structure of discrete Morse sequences. Quantitative benchmarking against learned segmentation models remains a separate evaluation task. The repository includes runnable examples and references to the underlying theory.

