---
title: "UniSpace — Campus Room Booking"
excerpt: "Real-time room availability and booking for ESIEE Paris. 🏆 *Coup de Cœur* award<br/><img src='/images/portfolio/unispace-stand.jpg'>"
collection: portfolio
---

**UniSpace** is a mobile & web app that lets ESIEE students and faculty see **real-time room availability**, **book rooms** with guardrails, and manage **office-hour slots**.

- **🏆 Award:** *Coup de Cœur* — ESIEE “Jour des Projets”
- **Code:** [github.com/nikxo/unispace](https://github.com/nikxo/unispace)  
- **Report (PDF):** [/files/rapport_unispace.pdf](/files/rapport_unispace.pdf)

### Why
Finding an open room was slow (ADE views are per-room, no fast filtering or booking). UniSpace gives a single place to **search, filter, and reserve** in seconds.

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
<img src="/images/portfolio/unispace-mockup.png" alt="UniSpace mockups" width="900"/>

---

*Photos: stand above; award badge below.*

<img src="/images/portfolio/unispace-award.jpg" alt="UniSpace — Coup de Cœur award" width="420"/>
