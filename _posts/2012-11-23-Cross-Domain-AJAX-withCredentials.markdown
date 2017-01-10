---
layout: post
categories: [AJAX, CORS]
title: Authenticated Cross-Domains AJAX Requests with CORS
---

Yesterday, I lost a significant amount of time dealing with cross-domain
AJAX requests and I thought I might share a bit of what I learned.

1.  jQuery 1.5.0 is BROKEN when it comes to cross-domain AJAX requests.
    Upgrade to at least jQuery 1.5.1.

2.  `Access-Control-Allow-Origin` WON'T accept a wildcard value if your
    XHR's `withCredentials` option is set to `true`. Also, it won't
    accept a list of origin. If you want to accept requests from a lot
    of domains, you can match the `Origin` request header against a set
    of domains and set the `Access-Control-Allow-Origin` accordingly.

3.  `Access-Control-Allow-Headers` and `Access-Control-Allow-Methods`
    CORS header does not support \* as a value. You have to be specific,
    even during your prototyping phase.

Hope it helps.
