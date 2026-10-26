---
title: "UniSpace: Campus Room Booking"
excerpt: "Flutter and Firebase room-booking app. Jury’s Choice (Coup de Cœur) at ESIEE Paris’s Jour des Projets."
collection: portfolio
featured: true
order: 4
category_label: "Software engineering · Team project · 2025"
permalink: /portfolio/unispace/
---

**UniSpace** is a mobile and web app to check **real-time room availability**, **book rooms** with guardrails, and manage **office-hour slots**.  
🏆 **Award:** **Jury’s Choice (Coup de Cœur)** at the **20th ESIEE “Jour des Projets”**, an annual showcase where student teams present engineering projects to a professional jury.  
👨‍🏫 **Supervisor:** Prof. **Hassane Mimoun**.  
👥 **Built with:** **Melchior Laurens**, **Nicolas Beaudet**, **Vadim Leupe**.  

<p>
  <a class="btn btn--primary" href="/files/rapport_unispace.pdf" target="_blank" rel="noopener">Report (PDF, in French)</a>
</p>

## Why
Finding an open room was slow (ADE views are per room, no fast filtering or booking). UniSpace provides one place to **search, filter, and reserve** in seconds.

## What it does
- **Live availability** with fast filters (type, location, time window)  
- **Booking** with fair-use limits plus automatic end-of-booking jobs  
- **Office hours:** teachers publish slots; students get **notifications**  
- **Favorites** for quick access to rooms or teachers

## How it works
- **Frontend:** Flutter (mobile and web)  
- **Backend:** Firebase (**Auth**, **Firestore**, **Cloud Functions**, **Cloud Storage**, **Cloud Tasks**)  
- **Timetables:** ADE iCal import → normalized events  
- **Security:** Firestore rules (role-based access, weekly booking caps)

## My role
Backend and data model (**Firestore schema**), **Cloud Functions** (availability, booking lifecycle, reminders, iCal import), auth/roles, and filtering/performance.

## Screens
<img src="/images/unispace-mockup.png" alt="UniSpace mockups" width="701" height="570" loading="lazy" decoding="async">

---

*Award received at ESIEE Paris’s Jour des Projets.*

<img src="/images/unispace-award.jpeg" alt="UniSpace - Coup de Cœur award (20th ESIEE Jour des Projets)" width="1600" height="903" loading="lazy" decoding="async">
