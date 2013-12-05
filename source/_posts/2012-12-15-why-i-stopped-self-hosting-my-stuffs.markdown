---
categories: [self-hosting]
title: Why I Stopped self-hosting my mails, IM and website
layout: post
---

A year ago, I started an experiment. I wanted to quit gmail and gtalk services
and prove me that I could host my emails and my IM myself.  It went quite well
but I decided to stop and subscribed to [fastmail.fm](http://fastmail.fm) and
to [hosted.im](http://hosted.im).

## Installation

A year ago, I spent some days installing a fully functionnal mail/web/jabber
server. Hopefully, I had some [good tutorials](http://flurdy.com/docs/postfix/)
about setting up a mail server. On the jabber side, it was quite easy even if
sometime, my WTF-o-meter level was really high. I blame my totally absent
knowledge of erlang and mnesia here.

The easiest part was to set-up varnish and nginx on the server.  This is
because I use these technologies every day. I still think that serving static
files with a reverse proxy could be much more easier and quicker to setup.

Backuping is easy and cheap, thanks to Amazon S3. I did not suffer any crash
and did not have to restore my data. I think I would have cried if I had to do
that because of the time needed to set-up the server again.  The pain would
have been bearable thanks to the EBS (if it doesn't fail).

My final set-up used these technologies: Amazon EC2, Amazon S3, Amazon
CloudFront, Amazon Elastic Block Storage, Postfix, Dovecot, Sieve, Varnish,
Postgrey, Spamassassin, Nginx and Ejabberd.

## Running it

Here is what I learned:

-   SMTP servers obey Murphy's Law. If you have an important mail to send, it
    will fail. Fallbacking to gmail happened too many time.

-   ejabberd is stable. In a year of operation, it failed once and restarting
    it made did the trick. The [guys behind
    ejabberd](http://www.process-one.net/en/) did a really great job.

-   Spam was virtually absent from my mail. Spamassasin and postgrey worked
    well.

-   [Sieve](http://en.wikipedia.org/wiki/Sieve_%28mail_filtering_language%29)
    is great. I mean really really GREAT. Filtering mail in gmail is a pain.

-   Mail clients all suck. Sparrow was an exception.

-   I'm not nerdy enough to use [Mutt](http://www.mutt.org/).

-   I should have used a configuration management system like Chef, Puppet or
    CFEngine to create the server. It would have doubled/tripled the time
    required to configure it properly, but it would have been an asset if I
    wanted to migrate my services to another host, which I considered at some
    point.

## Now

Yesterday, and after too many problem with my SMTP server, I decided to end
this experiment and started looking for a reliable mail provider. I chose
fastmail.fm because of the price, migrations processes and the Sieve support.

This website is now hosted by Amazon S3. The only cron job that I had is now
run on heroku. My jabber service is being migrated to hosted.im.

This will costs me around 50$ a year and this is definitely worth the time I
won't put in managing a server.

Creating, installing and configuring software is easy. Achieving reliability is
hard.
