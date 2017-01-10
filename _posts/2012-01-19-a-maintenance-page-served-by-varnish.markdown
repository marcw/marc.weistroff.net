---
layout: post
categories: [varnish, vcl]
title: Serving a maintenance page with varnish
---

Yesterday during the SOPA Blackout, this website was on strike. The
billions of readers of this blog had a static page explaining why this
website was offline instead of the normal content. As a good nerd, I
turned this operation into a technological one and instead of serving a
static html with nginx, I decided to use
[varnish](https://www.varnish-cache.org/). Yes, varnish. I never wrote
anything about the absolutely amazing architecture of this blog but
basically, static files are generated from
[RestructuredText](http://docutils.sourceforge.net/rst.html), served by
[nginx](http://nginx.org/) and cached by varnish. Let's get back to the
point. I wanted varnish to serve a static page with a 503 status code
(for SEO purpose). It took a bit of VCL knowledge and here is how to do
it:

``` text /etc/varnish/maintenance.vcl
backend default {
    .host = "127.0.0.1";
    .port = "8080";
}

sub vcl_recv {
    error 503;
}

sub vcl_error {
    set obj.http.Content-Type = "text/html; charset=utf-8";
    # you can put absolutely what you want
    synthetic {"
        <html>
            <head>
            <title>My maintenance page</title>
            </head>
            <body>
            <h1>This website is under maintenance.</h1>
            </body>
            </html>
            "};
    return (deliver);
}
```

The trick here is the `synthetic` keyword which is described in the
varnish documentation like this:

> The synthetic keyword is used to produce a synthetic response body in
> `vcl_error`. It takes a single string as argument.

Now that you have a cool VCL for your maintenance page, you can load
this vcl in varnish like this:

``` bash
varnishadm -T 127.0.0.1:6082 -S /etc/varnish/secret "vcl.load maintenance /etc/varnish/maintenance.vcl"
```

and to replace the original rules by those described in maintenance.vcl

``` bash
varnishadm -T 127.0.0.1:6082 -S /etc/varnish/secret "vcl.use maintenance"
```

And varnish will serve the maintenance page. Like a boss.
