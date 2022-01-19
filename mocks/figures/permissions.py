"""
Mock for the figures.permissions model.
"""


def is_active_staff_or_superuser(request):
    """
    Exact copy of Figures=0.4.x `figures.permissions.is_active_staff_or_superuser` helper.
    """
    return request.user and request.user.is_active and (
        request.user.is_staff or request.user.is_superuser)

