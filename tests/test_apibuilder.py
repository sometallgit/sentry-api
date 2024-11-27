import pytest
import responses
import json

from .context import sentry_analytics
from .mock import sentry


api_builder = sentry_analytics.sentry_api.sentry_api_builder
auth_token: str = "auth_token123"
api = sentry_analytics.sentry_api.Sentry_Api(auth_token)
issue_id: str = "issue_abc"
event_id: str = "event_def"

def test_apibuilder_get_projects():
	url: str = api_builder.get_projects('test')
	expected: str = "https://sentry.io/api/0/organizations/test/projects/"
	assert url == expected

def test_apibuilder_get_issue_event():
	url: str = api_builder.get_issue_event(issue_id, event_id)
	expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/{event_id}"
	assert url == expected

# def test_get_issue_attachments():
# 	assert False

def test_apibuilder_get_issue_events():
	url: str = api_builder.get_issue_events(issue_id)
	expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/"
	assert url == expected

def test_api_build_header():
	header: str = api.build_header(None)
	expected = {'Authorization': f'Bearer {auth_token}'}
	assert header == expected

@responses.activate
def test_api_get_projects():
	responses.add(**{
		'method'		: responses.GET,
		'url'			: "https://sentry.io/api/0/organizations/foo/projects/",
		'body'			: sentry.sentry_mock,
		'status'		: 200,
		'content_type' 	: "application/json",
		'adding_headers': { 'X-Foo' : 'Bar' }
	})

	# response = requests.get('http://example.com/api/123')
	response = api.get_projects("foo")

	assert json.loads(sentry.sentry_mock) == response.json()
	# assert (403, response.status_code)
	

# @responses.activate
# def test_response():
# 	responses.add(**{
# 		'method'		: responses.GET,
# 		'url'			: "http://example.com/api/123",
# 		'body'			: '{"error": "reason"}',
# 		'status'		: 404,
# 		'content_type' 	: "application/json",
# 		'adding_headers': { 'X-Foo' : 'Bar' }
# 	})

# 	response = requests.get('http://example.com/api/123')

# 	assert ({'error': 'reason'} == response.json())
# 	assert (403, response.status_code)