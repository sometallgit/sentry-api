import os
# from .context import sentry_analytics
from sentry_analytics import  event_parser
from .mock import sentry

def current_file_dir():
	return os.path.dirname(__file__)

def make_path(path: str) -> str:
	return os.path.join(current_file_dir(), path)

def test_parse_issues():
	# event_parser.parse_issues_file("tests/mock/issue_ids.json")
	expected = {'1231231231': 'event title', '3213213211': 'event title'}
	issues = event_parser.parse_issues(sentry.sentry_mock_get_issues)
	assert issues == expected

def test_parse_issues_from_file():
	expected = {'1231231231': 'event title', '3213213211': 'event title'}
	issues = event_parser.parse_issues_from_file(make_path("file/issue_ids.json"))
	assert issues == expected

def test_parse_events():
	# event_parser.parse_issues_file("tests/mock/issue_ids.json")
	expected = ['aaaaaaaaaaabbbbbbbbbbbccccccc', 'mmmmmmmmmmmmmccccccccccccc']
	issues = event_parser.parse_events(sentry.sentry_mock_get_events)
	assert issues == expected

def test_parse_events_from_file():
	expected = ['aaaaaaaaaaabbbbbbbbbbbccccccc', 'mmmmmmmmmmmmmccccccccccccc']
	issues = event_parser.parse_events_from_file(make_path("file/events.json"))
	assert issues == expected

def test_parse_attachments():
	# event_parser.parse_issues_file("tests/mock/issue_ids.json")
	expected = ['111111111111']
	issues = event_parser.parse_attachments(sentry.sentry_mock_get_attachments)
	assert issues == expected

def test_parse_attachments_from_file():
	expected = ['111111111111']
	issues = event_parser.parse_attachments_from_file(make_path("file/attachments.json"))
	assert issues == expected