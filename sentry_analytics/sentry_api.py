import requests
import json

class sentry_api_builder():
	endpoint_baseurl: str = "https://sentry.io/api/0/"
	organisations: str = "organizations/"
	projects: str = "projects/"
	issues: str = "issues/"
	events: str = "events/"
	

	@classmethod
	def get_projects(self, org_slug: str) -> str:
		return f"{self.endpoint_baseurl}{self.organisations}{org_slug}/{self.projects}"

	@classmethod
	def get_issue_event(self, issue_id: str, event_id: str) -> str:
		# https://sentry.io/api/0/issues/{issue_id}/events/{event_id}/
		return f"{self.endpoint_baseurl}{self.issues}{issue_id}/{self.events}{event_id}"

	@classmethod
	def get_issue_events(self, issue_id: str) -> str:
		# /api/0/issues/{issue_id}/events/
		return f"{self.endpoint_baseurl}{self.issues}{issue_id}/{self.events}" #?&cursor=0:100:0

