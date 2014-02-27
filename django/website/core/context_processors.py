from django.conf import settings
from django.core.urlresolvers import reverse


def core_values(request):
    """
    A nice pun. But this is how we stick handy data everywhere.
    """

    data = {
        'SITE_TITLE': getattr(settings, "SITE_TITLE", "Open Data Comparison"),
        'FRAMEWORK_TITLE': getattr(settings, "FRAMEWORK_TITLE", "Open Data"),
    }
    return data


def current_path(request):
    """Adds the path of the current page to template context, but only
    if it's not the path to the logout page. This allows us to redirect
    user's back to the page they were viewing before they logged in,
    while making sure we never redirect them back to the logout page!

    """
    context = {}
    if request.path.strip() != reverse('logout'):
        context['current_path'] = request.path
    return context