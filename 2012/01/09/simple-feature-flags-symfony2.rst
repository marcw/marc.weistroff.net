public: yes
tags: [php, symfony2, security, features flags]
summary: |
  The one where I teach you how to enable simple feature flags in your Symfony2
  project.

Feature flags with Symfony2
==================================

`Feature flags` is a really common design in modern web applications and is
heavily used by startups. It permits you to enable/disable features
for some users or groups of users. It's really handy if you want to deploy to
production a feature for testing purpose in order to have data on how your infrastructure
reacts in a live environment.

Let's have some fun and try to implements a simple feature flags design in your
Symfony2 project without writing too much lines of PHP. Sure, we will use the as
complex as powerful Security component for that. I won't dig deep inside the
it, so you'll better be well versed about `roles and roles
hierarchy <http://symfony.com/doc/current/book/security.html#roles>`_.

What we want for this project three types of features groups: 'alpha', 'beta'
and 'prod'.  I want the admin of my website to have access to the alpha
unstable features, the beta testing group to the beta features and all the oser
users to all the rest of my application.

We can express this by using role hierarchy:

.. sourcecode:: yaml

    # app/config/security.yml
    security:
        role_hierarchy:
            ROLE_ADMIN: ROLE_USER
            ROLE_SUPER_ADMIN: ROLE_USER,ROLE_ADMIN,ROLE_ALLOWED_TO_SWITCH

            FEATURE_ALPHA: FEATURE_BETA, FEATURE_SUPER_SECRET
            FEATURE_BETA: FEATURE_PROD, FEATURE_FOOBAR
            FEATURE_PROD: FEATURE_FOO, FEATURE_BAR

Thus, anyone whom is granted FEATURE_ALPHA role will have access to all the
features and the other groups won't have access to the "lower" features.

This is a rad way of defining who have access to what, but currently, it's not
supported by the SecurityBundle because only roles prefixed by `ROLE_` are
supported by the current voter.

So, we need to define a new voter that supports the newly created FEATURE_*
roles. Is it complicated ? Hell no. Add this to your bundle xml configuration:

.. sourcecode:: xml

        <!-- Acme/Bundle/AwesomeBundle/Resources/config/config.xml -->
        <service id="awesome.feature_hierarchy.voter" class="%security.access.role_hierarchy_voter.class%">
            <argument type="service" id="security.role_hierarchy" />
            <argument>FEATURE_</argument>
            <tag name="security.voter" />
        </service>

This simple piece of xml will register a new voter based on the actual role
hierarchy. The difference is that this voter will be specialised with the
`FEATURE_` prefixed roles.

Now, we need to specify in our user class how the roles will be distributed:

.. sourcecode:: php

        // User.php
        // You can implement your own logic there, be inventive.
        public function getRoles()
        {
            if ($this->isAdmin) {
                return array('ROLE_ADMIN', 'FEATURE_ALPHA');
            }

            if ($this->isBetaTester) {
                return array('ROLE_ADMIN', 'FEATURE_BETA');
            }

            return array('ROLE_USER', 'FEATURE_PROD');
        }

From now on, the user class will be able to tell wich roles he has, and the
Security context will be able to vote on them. The only thing left to do is to
"secure" parts of your application.

In your templates:

.. sourcecode:: jinja

    {% if app.security.isGranted('FEATURE_SUPER_SECRET')) %}
        {# bla bla bla #}
    {% endif %}

or in your controllers:

.. sourcecode:: php

    public function indexAction()
    {
        // ...
        if ($this->get('security.context')->isGranted('FEATURE_SUPER_SECRET')) {
            // do stuff
        }

        // ...
    }

or your routes thanks to the built-in firewall:

.. sourcecode:: yaml

    # app/config/security.yml
    security:
        access_control:
            -
                path: ^/my/route/to/my/feature.*$
                roles: [FEATURE_SUPER_SECRET]

Here we are! You enabled feature flags in your project with a few lines of PHP
and 5 lines of XML. Have fun!
