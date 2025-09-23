---
title: "UniSpace — Campus Room Booking"
excerpt: "Real-time room availability and booking for ESIEE Paris. 🏆 *Coup de Cœur* — 20th ESIEE **Jour des Projets**<br/><img src='/images/unispace-stand.jpeg' alt='UniSpace stand' width='360'>"
collection: portfolio
---

**UniSpace** is a mobile & web app to check **real-time room availability**, **book rooms** with guardrails, and manage **office-hour slots**.  
🏆 Award: *Coup de Cœur* — **20th** ESIEE *Jour des Projets*.  
📱 **Coming soon** to the **App Store** and **Google Play**.

<p>
  <a class="btn btn--primary" href="https://github.com/nikxo/unispace" target="_blank" rel="noopener">Source code</a>
  <a class="btn" href="/files/rapport_unispace.pdf" target="_blank" rel="noopener">Report (PDF, in french)</a>
</p>

### Why
Finding an open room was slow (ADE views are per-room, no fast filtering or booking). UniSpace gives one place to **search, filter, and reserve** in seconds.

### What it does
- **Live availability** with fast filters (type, location, time window)  
- **Booking** with fair-use limits + automatic end-of-booking jobs  
- **Office hours**: teachers publish slots; students get **notifications**  
- **Favorites** for quick access to rooms/teachers

### How it works
- **Frontend:** Flutter (mobile + web)  
- **Backend:** Firebase (**Auth**, **Firestore**, **Cloud Functions**, **Cloud Storage**, **Cloud Tasks**)  
- **Timetables:** ADE iCal import → normalized events  
- **Security:** Firestore rules (role-based access, weekly booking caps)

### My role
Backend & data model (**Firestore schema**), **Cloud Functions** (availability, booking lifecycle, reminders, iCal import), auth/roles, and filtering/perf.

### Screens
<img src="/images/unispace-mockup.png" alt="UniSpace mockups" width="900"/>

---

*Photos: stand above; award badge below.*

<img src="/images/unispace-award.jpeg" alt="UniSpace — Coup de Cœur award (20th ESIEE Jour des Projets)" width="900"/>
