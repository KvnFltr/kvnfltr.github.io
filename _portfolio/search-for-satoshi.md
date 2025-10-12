---
title: "The Search for Satoshi: Java Text Adventure"
excerpt: "GUI-based adventure where you hunt Satoshi Nakamoto across a village map. Teleporter, keys, inventory, timer, and a win/lose path.<br/><img src='/images/satoshi-map.png' alt='Game map: \"The Search for Satoshi\"' width='500'/>"
collection: portfolio
permalink: /portfolio/search-for-satoshi/
---

A single-player **Java** adventure game (Zuul variant).  
You play an investigator mandated by the IMF to locate **Satoshi Nakamoto’s HQ** and press the kill-switch to stop Bitcoin before time runs out.

<p>
  <a class="btn btn--primary" href="https://github.com/KvnFltr/search-for-satoshi" target="_blank" rel="noopener">GitHub Repository</a>
  <a class="btn" href="/files/rapport_zuul_satoshi.pdf" target="_blank" rel="noopener">Project Report (PDF, fr)</a>
</p>

### Overview
- **Goal.** Explore the suspects’ houses, collect clues and **three keys**, unlock the trapdoor in Adam’s office, reach the **Bitcoin Temple**, and press the button.
- **Lose condition.** A **move counter** acts as a timer; too many moves → *Game Over*.
- **World.** A compact village with streets, offices, and special rooms (see map).

### Core Mechanics
- **Inventory & weight limit.** Pick up and drop items; capacity can be increased by a **magic cookie**.  
- **Locked doors.** Multi-key door logic (requires 3 keys) with proper messages on failure/success.  
- **Teleporter (Beamer).** Charge in one room, **fire** later to jump back instantly.  
- **Transporter room.** Exits teleport you to a **random** room (room randomizer).  
- **Backtracking.** `back` uses a **stack** to return across multiple steps.  
- **GUI.** Swing UI with command **buttons** (movement, inventory, beamer, stopBTC).  
- **Images & map.** Each room has an illustration; HUD shows remaining moves.

### Map
<figure>
  <img src="/images/satoshi-map.png" alt="Map of the game world with suspects and special rooms" width="980">
  <figcaption><strong>Figure.</strong> World layout: streets, suspects’ homes, HQ, and special rooms.</figcaption>
</figure>

### What I implemented
- Refactoring with **encapsulation**, **HashMap** exits/items, and a clean **Room / Player / Item / ItemList** split.
- Robust command set (`take`, `drop`, `inventory`, `eat`, `back`, `charge`, `fire`, `stopBTC`, …) and **JUnit-style tests + Javadoc**.
- Clear **win/lose** flow and GUI messages; small **scripts** to auto-test command sequences.
