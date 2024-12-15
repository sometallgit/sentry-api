import requests
import json

class sentry_api_builder():
	endpoint_baseurl: str = "https://sentry.io/api/0/"
	organisations: str = "organizations/"
	projects: str = "projects/"
	issues: str = "issues/"
	events: str = "events/"
	

	@classmethod
	def get_projects(cls, org_slug: str) -> str:
		return f"{cls.endpoint_baseurl}{cls.organisations}{org_slug}/{cls.projects}"
	
	@classmethod
	def get_issues(cls, org_slug: str, project_name: str) -> str:
		# https://sentry.io/api/0/projects/{org_slug}/{project_name}/issues/
		return f"{cls.endpoint_baseurl}{cls.projects}{org_slug}/{project_name}/{cls.issues}"

	@classmethod
	def get_issue_event(cls, issue_id: str, event_id: str) -> str:
		# https://sentry.io/api/0/issues/{issue_id}/events/{event_id}/
		return f"{cls.endpoint_baseurl}{cls.issues}{issue_id}/{cls.events}{event_id}/"

	@classmethod
	def get_issue_attachments(cls, org_slug: str, project_name: str, event_id: str) -> str:
		# https://{org_slug}.sentry.io/api/0/projects/{org_slug}/{project_id}/events/{event_id}/attachments/
		return f"https://{org_slug}.sentry.io/api/0/projects/{org_slug}/{project_name}/events/{event_id}/attachments/"

	@classmethod
	def get_issue_attachment(cls, org_slug: str, project_name: str, event_id: str, attachment_id: str) -> str:
		#https://{org_slug}.sentry.io/api/0/projects/{org_slug}/{project_name}/events/{event_id}/attachments/{attachment_id}/?download=1
		return f"{sentry_api_builder.get_issue_attachments(org_slug,project_name,event_id)}{attachment_id}/?download=1"

	@classmethod
	def get_issue_events(cls, issue_id: str) -> str:
		# /api/0/issues/{issue_id}/events/
		return f"{cls.endpoint_baseurl}{cls.issues}{issue_id}/{cls.events}" #?&cursor=0:100:0

class Sentry_Api():
	def __init__(self, auth_token: str, org_slug: str, project_name: str) -> None:
		self.auth_token: str = auth_token
		self.org_slug: str = org_slug
		self.project_name: str = project_name

	def build_header(self, custom_header: dict[str, str]):
		header: dict[str, str] = {}
		auth_header: dict[str, str] = {"Authorization": f"Bearer {self.auth_token}"}
		header.update(auth_header)
		if custom_header:
			header.update(custom_header)

		return header

	def do_get(self, 
            url: str, 
            custom_header: dict[str, str] = {}) -> requests.Response:
		header = self.build_header(custom_header)

		response: requests.Response = requests.get(url, headers=header)
		print(f"GET {url}")

		if response.status_code != 200:
			raise ValueError(f"GET returned {response.status_code} with error: {response.text}")

		return response

	def get_projects(self, org_slug: str) -> requests.Response:
		url: str = sentry_api_builder.get_projects(org_slug)
		response: requests.Response = self.do_get(url)
		return response

	def get_issues(self) -> requests.Response:
		url: str = sentry_api_builder.get_issues(self.org_slug, self.project_name)
		response: requests.Response = self.do_get(url)
		return response

	def get_issue_events(self, issue_id: str) -> requests.Response:
		url: str = sentry_api_builder.get_issue_events(issue_id)
		response: requests.Response = self.do_get(url)
		return response

	def get_issue_event_attachments(self, event_id: str) -> requests.Response:
		url: str = sentry_api_builder.get_issue_attachments(self.org_slug, self.project_name, event_id)
		response: requests.Response = self.do_get(url)
		return response

	def get_issue_event_attachment(self, event_id: str, attachment_id: str) -> requests.Response:
		url: str = sentry_api_builder.get_issue_attachment(self.org_slug, self.project_name, event_id, attachment_id)
		response: requests.Response = self.do_get(url)
		return response

	def get_issue_event(self, issue_id: str, event_id: str) -> requests.Response:
		url: str = sentry_api_builder.get_issue_event(issue_id, event_id)
		response: requests.Response = self.do_get(url)
		return response

