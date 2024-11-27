import pytest
from .context import sentry_analytics

api = sentry_analytics.sentry_api.sentry_api_builder

def test_apibuilder():
	url = api.get_projects('test')
	expected: str = "https://sentry.io/api/0/organizations/test/projects/"
	assert url == expected