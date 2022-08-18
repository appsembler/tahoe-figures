"""
Tests for the sites backends.
"""
import pytest
from django.contrib.sites.models import Site
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.contrib.sites import shortcuts
from rest_framework.exceptions import PermissionDenied

from tahoe_sites.api import create_tahoe_site

from tahoe_figures_plugins.sites import get_current_site_or_by_uuid


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def fake_current_site(monkeypatch):
    current_site = Site.objects.create(domain='current-site.org')

    def fake_get_current_site(*_args):
        return current_site

    monkeypatch.setattr(shortcuts, 'get_current_site', fake_get_current_site)
    return current_site


@pytest.mark.django_db
def test_no_uuid(request_factory, fake_current_site):
    request = request_factory.get('/figures/api')
    site = get_current_site_or_by_uuid(request)
    assert site == fake_current_site


@pytest.mark.django_db
def test_with_uuid_permitted(request_factory, fake_current_site):
    info = create_tahoe_site(domain='other-site.com', short_name='OSC')
    request = request_factory.get('/figures/api', data={
        'site_uuid': info['site_uuid'],
    })
    request.user = User(is_staff=True, is_active=True)

    site = get_current_site_or_by_uuid(request)
    assert site != fake_current_site
    assert site == info['site']


@pytest.mark.django_db
def test_with_uuid_not_permitted(request_factory):
    request = request_factory.get('/figures/api', data={
        'site_uuid': 'a000000b-1234-11ec-8db5-1cccccccccc2',
    })
    request.user = User(is_staff=False, is_active=True)

    with pytest.raises(PermissionDenied):
        get_current_site_or_by_uuid(request)
