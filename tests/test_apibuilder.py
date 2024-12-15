#type: ignore #silence pylance in tests
import responses
import json

# from .context import sentry_analytics
from sentry_analytics.api import sentry_api
from .mock import sentry 

api_builder = sentry_api.sentry_api_builder
auth_token: str = "auth_token123"
org_slug: str = "org_slug"
project_name: str = "project_name"
config = sentry_api.ApiConfig(auth_token, org_slug, project_name)
api = sentry_api.Sentry_Api(config)
issue_id: str = "issue_abc"
event_id: str = "event_def"
attachment_id: str = "attachment_ghi"

def test_apibuilder_get_projects():
    url: str = api_builder.get_projects('test')
    expected: str = "https://sentry.io/api/0/organizations/test/projects/"
    assert url == expected

def test_apibuilder_get_issues():
    url: str = api_builder.get_issues(org_slug, project_name)
    expected: str = f"https://sentry.io/api/0/projects/{org_slug}/{project_name}/issues/"
    assert url == expected

def test_apibuilder_get_issue_event():
    url: str = api_builder.get_issue_event(issue_id, event_id)
    expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/{event_id}/"
    assert url == expected

def test_apibuilder_get_issue_attachments():
    url: str = api_builder.get_issue_attachments(org_slug, issue_id, event_id)
    expected: str = f"https://{org_slug}.sentry.io/api/0/projects/{org_slug}/{issue_id}/events/{event_id}/attachments/"
    assert url == expected

def test_apibuilder_get_issue_attachment():
    attachment_id: str = "attachment_id"
    url: str = api_builder.get_issue_attachment(org_slug, issue_id, event_id, attachment_id)
    expected: str = f"https://{org_slug}.sentry.io/api/0/projects/{org_slug}/{issue_id}/events/{event_id}/attachments/{attachment_id}/?download=1"
    assert url == expected

def test_apibuilder_get_issue_events():
    url: str = api_builder.get_issue_events(issue_id)
    expected: str = f"https://sentry.io/api/0/issues/{issue_id}/events/"
    assert url == expected

def test_api_build_header():
    header: dict[str, str] = api.build_header({})
    expected = {'Authorization': f'Bearer {auth_token}'}
    assert header == expected

def test_api_build_header_with_custom():
    header: dict[str, str] = api.build_header({"key" : "value"})
    expected = {'Authorization': f'Bearer {auth_token}',
                'key' : 'value'}
    assert header == expected

@responses.activate
def test_api_get_projects():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://sentry.io/api/0/organizations/foo/projects/",
        'body'          : sentry.sentry_mock,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    # response = requests.get('http://example.com/api/123')
    response = api.get_projects("foo")

    assert json.loads(sentry.sentry_mock) == response.json()
    # assert (403, response.status_code)

@responses.activate
def test_api_get_issue_events():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://sentry.io/api/0/issues/foo/events/",
        'body'          : sentry.sentry_mock_get_events,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    # response = requests.get('http://example.com/api/123')
    response = api.get_issue_events("foo")

    assert json.loads(sentry.sentry_mock_get_events) == response.json()

@responses.activate
def test_api_get_issues():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://sentry.io/api/0/projects/org_slug/project_name/issues/",
        'body'          : sentry.sentry_mock_get_issues,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    response = api.get_issues()

    assert json.loads(sentry.sentry_mock_get_issues) == response.json()

@responses.activate
def test_api_get_issue_attachments():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://org_slug.sentry.io/api/0/projects/org_slug/project_name/events/event_def/attachments/",
        'body'          : sentry.sentry_mock_get_attachments,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    response = api.get_issue_event_attachments(event_id)

    assert json.loads(sentry.sentry_mock_get_attachments) == response.json()

@responses.activate
def test_api_get_issue_attachment():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://org_slug.sentry.io/api/0/projects/org_slug/project_name/events/event_def/attachments/attachment_ghi/?download=1",
        'body'          : sentry.sentry_mock_get_attachment,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    response = api.get_issue_event_attachment(event_id, attachment_id)

    assert sentry.sentry_mock_get_attachment == response.text

@responses.activate
def test_api_get_issue_event():
    responses.add(**{
        'method'        : responses.GET,
        'url'           : "https://sentry.io/api/0/issues/issue_abc/events/event_def/",
        'body'          : sentry.sentry_mock_get_issue_event,
        'status'        : 200,
        'content_type'  : "application/json",
        'adding_headers': { 'X-Foo' : 'Bar' }
    })

    response = api.get_issue_event(issue_id, event_id)

    assert json.loads(sentry.sentry_mock_get_issue_event) == response.json()

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