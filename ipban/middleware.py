from models import Ban
from django.shortcuts import render_to_response

class IPBanMiddleware(object):
  """
  Simple middleware for taking care of bans from specific IP's
  Redirects the banned user to a ban-page with an explanation
  """
  def process_request(self, request):
    ip = request.META['REMOTE_ADDR'] # user's IP

    # see if user is banned
    try:
      # if this doesnt throw an exception, user is banned
      ban = Ban.objects.get(ip=ip)
      reason = ban.reason

      # return the "ban page"
      return render_to_response("ban/banned.html",
        {"reason": reason})
    except Ban.DoesNotExist: # not banned! goodie
      pass
