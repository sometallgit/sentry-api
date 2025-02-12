import json
from sentry_analytics.api.sentry_issue_event import SentryIssueEvent


def parse_events(json_file: str) -> list[SentryIssueEvent]:
    event_ids: list[SentryIssueEvent] = []
    j = json.loads(json_file)
    for event in j:
        event_ids.append(SentryIssueEvent(event))

    return event_ids

def parse_event(json_file: str) -> SentryIssueEvent:
    return SentryIssueEvent(json.loads(json_file))

def parse_events_from_file(json_file: str) -> list[SentryIssueEvent]:
    with open(json_file) as json_data:
        return parse_events(json_data.read())

# Parses a JSON string containing a list of issues and returns a dictionary mapping issue IDs to their titles.
def parse_issues(json_str: str) -> dict[str,str]:
    issue_ids: dict[str,str] = {}
    j = json.loads(json_str)
    for issue in j:
        id = issue['id']
        title = issue['title']
        issue_ids[id] = title
    return issue_ids

def parse_issues_from_file(json_file: str) -> dict[str,str]:
    with open(json_file) as json_data:
        return parse_issues(json_data.read())
    

def parse_attachments(json_str: str) -> list[str]:
    attachments: list[str] = []
    j = json.loads(json_str)
    
    if len(j) > 1:
        raise NotImplementedError('Multiple attachments are not yet supported.')

    for attachment in j:
        attachments.append(attachment['id'])
    return attachments

def parse_attachments_from_file(json_file: str) -> list[str]:
    with open(json_file) as json_data:
        return parse_attachments(json_data.read())
