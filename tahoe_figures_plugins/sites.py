"""
Site backends for Figures in Tahoe.
"""

from django.contrib.sites import shortcuts as django_sites_shortcuts
from rest_framework.exceptions import PermissionDenied

from figures import permissions as figures_permissions
from tahoe_sites.api import get_site_by_uuid


def get_current_site_or_by_uuid(request):
    """
    Backend to get the requested site either by Site's UUID or from the `get_current_site()`.
    """
    site_uuid = request.GET.get('site_uuid')
    if site_uuid:
        if figures_permissions.is_active_staff_or_superuser(request):
            site = get_site_by_uuid(site_uuid)
        else:
            raise PermissionDenied('Not permitted to use the `site_uuid` parameter.')
    else:
        site = django_sites_shortcuts.get_current_site(request)
    return site
