---
layout: post
categories: [php, postgresql, linux]
title: Solving segfault issues when using PHP5 and PostgreSQL
---

If your PHP5 installation always segfault when using PostgreSQL, you
might have to change the loading order of your extensions. To be
specific, you'll surely need to load the postgresql extension before the
curl one.
