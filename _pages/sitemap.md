---
title: "Sitemap"
permalink: /sitemap/
---

- [About](/)
- [Selected work](/portfolio/)
- [CV](/cv/)

## Projects

{% for project in site.portfolio %}
- [{{ project.title }}]({{ project.url }})
{% endfor %}
