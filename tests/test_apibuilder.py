import pytest
from .context import sentry_analytics

api = sentry_analytics.sentry_api.sentry_api_builder
issue_id: str = "issue_abc"
event_id: str = "event_def"

def test_apibuilder():
	url: str = api.get_projects('test')
	expected: str = "https://sentry.io/api/0/organizations/test/projects/"
	assert url == expected

def test_get_issue_event():
	url: str = api.get_issue_event(issue_id, event_id)
	expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/{event_id}"
	assert url == expected

# def test_get_issue_attachments():
# 	assert False

def test_get_issue_events():
	url: str = api.get_issue_events(issue_id)
	expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/"
	assert url == expected