---
title: "UniSpace: Campus Room Booking"
excerpt: "Real-time room availability and booking for ESIEE Paris. 🏆 Jury’s Choice (Coup de Cœur) at the 20th ESIEE “Jour des Projets” student engineering expo.<br/><img src='/images/unispace-stand.jpeg' alt='UniSpace stand' width='500'>"
collection: portfolio
---

**UniSpace** is a mobile and web app to check **real-time room availability**, **book rooms** with guardrails, and manage **office-hour slots**.  
🏆 **Award:** **Jury’s Choice (Coup de Cœur)** at the **20th ESIEE “Jour des Projets”**, an annual showcase where student teams present engineering projects to a professional jury.  
👨‍🏫 **Supervisor:** Prof. **Hassane Mimoun**.  
👥 **Built with:** **Melchior Laurens**, **Nicolas Beaudet**, **Vadim Leupe**.  
📱 **Coming soon** to the **App Store** and **Google Play**.

<p>
  <a class="btn btn--primary" href="https://github.com/nikxo/unispace" target="_blank" rel="noopener">Source code</a>
  <a class="btn" href="/files/rapport_unispace.pdf" target="_blank" rel="noopener">Report (PDF, in French)</a>
</p>

### Why
Finding an open room was slow (ADE views are per room, no fast filtering or booking). UniSpace provides one place to **search, filter, and reserve** in seconds.

### What it does
- **Live availability** with fast filters (type, location, time window)  
- **Booking** with fair-use limits plus automatic end-of-booking jobs  
- **Office hours:** teachers publish slots; students get **notifications**  
- **Favorites** for quick access to rooms or teachers

### How it works
- **Frontend:** Flutter (mobile and web)  
- **Backend:** Firebase (**Auth**, **Firestore**, **Cloud Functions**, **Cloud Storage**, **Cloud Tasks**)  
- **Timetables:** ADE iCal import → normalized events  
- **Security:** Firestore rules (role-based access, weekly booking caps)

### My role
Backend and data model (**Firestore schema**), **Cloud Functions** (availability, booking lifecycle, reminders, iCal import), auth/roles, and filtering/performance.

### Screens
<img src="/images/unispace-mockup.png" alt="UniSpace mockups" width="900"/>

---

*Photos: stand above; award badge below.*

<img src="/images/unispace-award.jpeg" alt="UniSpace - Coup de Cœur award (20th ESIEE Jour des Projets)" width="900"/>
