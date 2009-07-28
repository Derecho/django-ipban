django-ipban is a simple middleware application that enables staff users to ban visitors by IP address.
Based upon the code of Björn Kempén on his blog, I made an app out of it that anyone could easily add to their websites.

# Installation:
   - Add ipban to your INSTALLED_APPS.
   - Add ipban.middleware.IPBanMiddleware to your MIDDLEWARE_CLASSES
   - Done!

# Usage:
In your admin panel, you now see a ban page.
Here you can add any bans you may like.
A ban consists of an IP Address and a reason.

# Todo:
   - Add temporary banning
   - Make some translations

# Contact:
You can contact me on krisje8@gmail.com , or by visiting my website (krisje8.com) and leaving a comment.
