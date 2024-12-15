import time
import os

from api import sentry_api
from api import api
from api import api_config
import event_parser
import crash_scraper
def run():
    # init config
    dir: str = os.path.dirname(__file__)
    dir = os.path.join(dir, "../config/api_config.json")
    config = api_config.ApiConfigFile(dir)
    # init api
    api: sentry_api.Sentry_Api = sentry_api.Sentry_Api(config)

    get_project_issues(api)

def get_project_issues(api: api.Api):
    response = api.get_issues()
    # print(response.text)
    # iterate through the issues
    issue_ids: dict[str,str] = event_parser.parse_issues(response.text)

    for issue_id in issue_ids:
        if issue_ids[issue_id] not in whitelist:
            continue
        get_issue_events(api, issue_id)

def get_issue_events(api: api.Api, issue_id: str):
    # get the events for the issue
    response = api.get_issue_events(issue_id)
    # parse the event ids
    event_ids = event_parser.parse_events(response.text)
    # for each event id, get the attachments
    for event_id in event_ids:
        # get the attachments
        get_event_attachments(api, event_id)


def get_event_attachments(api: api.Api, event_id: str):
    response = api.get_issue_event_attachments(event_id)
    # parse the attachments
    attachments = event_parser.parse_attachments(response.text)
    # for each attachment, download the attachment
    for attachment in attachments:
        response = api.get_issue_event_attachment(event_id, attachment)
        print(response.text)

def get_project():
	print("hello world")
if __name__ == "__main__":
    run()