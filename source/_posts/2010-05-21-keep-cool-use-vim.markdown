---
layout: post
title: Keep cool, use vim
categories: [vim]
---

Fed up by using Eclipse (So slow) and Netbeans (always crashing), some
folks at Sensio Labs told me to start using Vim. At first, I said: “Just
the name makes me want to puke, but why not.”. A few weeks later, guess
which tool I used to edit my code? Yes, Vim. No, I didn’t even puke!

VIM does not stand for “VIM Is Magic” but it could. It’s lightweight and
usable everywhere. Whether you’re editing code, writing a blogpost in
markdown or configuring an apache vhost over an ssh connection, it’s a
wonderful tool to do the job.

[The hard part with vim is the
learning.](<http://urban.homelinux.org/wp-content/vim_learning.jpg>) It
will take you some time... But it worth it.

The exquise beauty of vim is that it’s nearly entirely customizable. If
you’re not satisfied with keyboards shortcut, change them! Do you want
to have the key F10 do something when you type it, you can! I configured
this key to remove spaces filled lines in my code with a simple regular
expression.

VIM is so customizable and extendable that with installing a few plugins
and tools, you can transform it in a full featured blazing-fast IDE.

The first thing you need to do is to install "exuberant-ctags". Without
it, vim cannot auto-complete from files you didn’t open or jump to
another method in other files. Once your tags are generated, the
method-hop won’t be as good as eclipse because it’s not contextual, but
it’s pretty acurate and it’s DAMN FAST!

Then I use these plugin to give an “IDE” feel to my vim:

-   NERDTree: A file explorer in your vim? yay!
-   minibufexplorer: Switch between buffers easily!
-   NERDCommenter: (Un)/Comment your code quickly
-   snipMate: I can haz Textmate styles snippets!
-   surround: Tired of navigating through your code to change double
    quote to simple quote? Surround do it with only a few strokes.
-   php-doc: Speed up the phpDoc editing
-   Align: Align your code in a few strokes!
-   matchit: Navigate in control structures or html tags, only with the
    % key.

Also, one of the more important point of using vim: It’s available
anywhere.

But be warned, once you’ll get used to the vim philosophy, it will be
difficult to switch back to an other IDE. ;)

If you’re curious and want to give a try without searching and
installing the plugin by yourself, [clone my vim
config](<http://github.com/marcw/vim-config>). But you’ll still have to
read the docs ;)
