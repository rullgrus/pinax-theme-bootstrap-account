Twitter Bootstrap Theme, for Pinax
==================================

A theme for Pinax 0.9 based on Twitter's open source Bootstrap framework.


Quick Start
-----------

This templates extend https://github.com/pinax/pinax-theme-bootstrap, and can be used
in conjuction with https://github.com/pinax/django-user-accounts.

To have this package working you need:

1. Include `pinax-theme-bootstrap-account` in your requirements file and 
   `pinax_theme_bootstrap_account` in your INSTALLED APPS.

2. Include "account.context_processors.account" in your `TEMPLATE_CONTEXT_PROCESSORS`

3. Define a `THEME_ACCOUNT_CONTACT_EMAIL` email address in your settings. This e-mail is 
   displayed on the website to users as the e-mail to write when something does not work,
   so set to one that someone reads.

Requirements
------------

This theme is officially supported when used in conjuction with Pinax 0.9.
If using the theme with Django < 1.4, you will need to install a recent
version of django-staticfiles as we use the `{% render %}` template tag.
