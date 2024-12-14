#The result of a call to get_projects
sentry_mock = """
[
	{
		"team": {
			"id": "1231231",
			"slug": "team-slug",
			"name": "team-slug"
		},
		"teams": [
			{
				"id": "1231231",
				"slug": "team-slug",
				"name": "team-slug"
			}
		],
		"id": "123123123",
		"name": "project-name-a",
		"slug": "project-name-a",
		"isBookmarked": true,
		"isMember": true,
		"access": [
			"team:read",
			"project:read",
			"event:read",
			"event:write",
			"project:releases",
			"alerts:write",
			"project:write",
			"alerts:read",
			"event:admin",
			"member:read",
			"org:read",
			"project:admin",
			"org:integrations",
			"team:write",
			"team:admin"
		],
		"hasAccess": true,
		"dateCreated": "2021-11-22T05:21:35.155732Z",
		"environments": [
			"production"
		],
		"eventProcessing": {
			"symbolicationDegraded": false
		},
		"features": [
			"verbose-test-alert-reporting",
			"data-forwarding",
			"rate-limits",
			"custom-inbound-filters",
			"discard-groups",
			"servicehooks",
			"alert-filters",
			"first-event-severity-new-escalation",
			"minidump",
			"race-free-group-creation",
			"similarity-embeddings-backfill",
			"similarity-indexing",
			"similarity-view",
			"span-metrics-extraction",
			"span-metrics-extraction-addons",
			"releases"
		],
		"firstEvent": "2021-11-22T06:28:14Z",
		"firstTransactionEvent": false,
		"hasSessions": false,
		"hasProfiles": false,
		"hasReplays": false,
		"hasFeedbacks": true,
		"hasNewFeedbacks": false,
		"hasCustomMetrics": false,
		"hasMonitors": false,
		"hasMinifiedStackTrace": false,
		"hasInsightsHttp": false,
		"hasInsightsDb": false,
		"hasInsightsAssets": false,
		"hasInsightsAppStart": false,
		"hasInsightsScreenLoad": false,
		"hasInsightsVitals": false,
		"hasInsightsCaches": false,
		"hasInsightsQueues": false,
		"hasInsightsLlmMonitoring": false,
		"platform": "native",
		"platforms": [
			"native"
		],
		"latestRelease": {
			"version": "project@ver1.2.3"
		},
		"hasUserReports": true,
		"latestDeploys": null
	},
	{
		"team": {
			"id": "1231231",
			"slug": "team-slug",
			"name": "team-slug"
		},
		"teams": [
			{
				"id": "1231231",
				"slug": "team-slug",
				"name": "team-slug"
			}
		],
		"id": "123123123",
		"name": "project-name-b",
		"slug": "project-name-b",
		"isBookmarked": false,
		"isMember": true,
		"access": [
			"team:read",
			"project:read",
			"event:read",
			"event:write",
			"project:releases",
			"alerts:write",
			"project:write",
			"alerts:read",
			"event:admin",
			"member:read",
			"org:read",
			"project:admin",
			"org:integrations",
			"team:write",
			"team:admin"
		],
		"hasAccess": true,
		"dateCreated": "2023-11-06T23:49:46.629726Z",
		"environments": [
			"development",
			"production"
		],
		"eventProcessing": {
			"symbolicationDegraded": false
		},
		"features": [
			"verbose-test-alert-reporting",
			"data-forwarding",
			"rate-limits",
			"custom-inbound-filters",
			"discard-groups",
			"servicehooks",
			"alert-filters",
			"first-event-severity-new-escalation",
			"minidump",
			"race-free-group-creation",
			"similarity-embeddings",
			"similarity-embeddings-backfill",
			"similarity-indexing",
			"similarity-view",
			"span-metrics-extraction",
			"span-metrics-extraction-addons",
			"releases"
		],
		"firstEvent": "2023-11-06T23:53:40.079000Z",
		"firstTransactionEvent": true,
		"hasSessions": true,
		"hasProfiles": false,
		"hasReplays": true,
		"hasFeedbacks": false,
		"hasNewFeedbacks": false,
		"hasCustomMetrics": false,
		"hasMonitors": false,
		"hasMinifiedStackTrace": true,
		"hasInsightsHttp": true,
		"hasInsightsDb": false,
		"hasInsightsAssets": true,
		"hasInsightsAppStart": false,
		"hasInsightsScreenLoad": false,
		"hasInsightsVitals": true,
		"hasInsightsCaches": false,
		"hasInsightsQueues": false,
		"hasInsightsLlmMonitoring": false,
		"platform": "javascript-react",
		"platforms": [
			"javascript"
		],
		"latestRelease": {
			"version": "product@ver1.2.3"
		},
		"hasUserReports": false,
		"latestDeploys": null
	}
]
"""

# Mocked sentry response for events on an issue
sentry_mock_get_events = """
[
	{
		"id": "aaaaaaaaaaabbbbbbbbbbbccccccc",
		"event.type": "default",
		"groupID": "123123123",
		"eventID": "aaaaaaaaaaabbbbbbbbbbbccccccc",
		"projectID": "111111111111111",
		"message": "error message name",
		"title": "error message name",
		"location": null,
		"culprit": "file:///C:/index.html",
		"user": {
			"id": null,
			"email": null,
			"username": null,
			"ip_address": null,
			"name": null,
			"geo": {
				"country_code": "IT",
				"city": "Bergamo",
				"region": "Italy"
			},
			"data": null
		},
		"tags": [
			{
				"key": "browser",
				"value": "Chrome 96.0.4664"
			},
			{
				"key": "browser.name",
				"value": "Chrome"
			},
			{
				"key": "environment",
				"value": "production"
			},
			{
				"key": "level",
				"value": "error"
			},
			{
				"key": "os",
				"value": "Windows >=10"
			},
			{
				"key": "os.name",
				"value": "Windows"
			},
			{
				"key": "release",
				"value": "project@version"
			},
			{
				"key": "url",
				"value": "file:///C:/index.html"
			}
		],
		"platform": "javascript",
		"dateCreated": "2024-11-26T20:36:21Z",
		"crashFile": null,
		"metadata": {
			"title": "error message name"
		}
	},
	{
		"id": "mmmmmmmmmmmmmccccccccccccc",
		"event.type": "default",
		"groupID": "123123123",
		"eventID": "mmmmmmmmmmmmmccccccccccccc",
		"projectID": "111111111111111",
		"message": "error message name",
		"title": "error message name",
		"location": null,
		"culprit": "file:///C:/index.html",
		"user": {
			"id": null,
			"email": null,
			"username": null,
			"ip_address": null,
			"name": null,
			"geo": {
				"country_code": "IT",
				"city": "Bergamo",
				"region": "Italy"
			},
			"data": null
		},
		"tags": [
			{
				"key": "browser",
				"value": "Chrome 96.0.4664"
			},
			{
				"key": "browser.name",
				"value": "Chrome"
			},
			{
				"key": "environment",
				"value": "production"
			},
			{
				"key": "level",
				"value": "error"
			},
			{
				"key": "os",
				"value": "Windows >=10"
			},
			{
				"key": "os.name",
				"value": "Windows"
			},
			{
				"key": "release",
				"value": "project@version"
			},
			{
				"key": "url",
				"value": "file:///C:/index.html"
			}
		],
		"platform": "javascript",
		"dateCreated": "2024-11-26T20:08:22Z",
		"crashFile": null,
		"metadata": {
			"title": "error message name"
		}
	}
]
"""

# An example of a response from Sentry's call to api/0/projects/{org_slug}/{project_name}/issues/
sentry_mock_get_issues = """
[
    {
        "id": "1231231231",
        "shareId": null,
        "shortId": "PROJ-NAME-2S",
        "title": "event title",
        "culprit": "file:///C:/Program%20Files/index.html",
        "permalink": "https://org-slug.sentry.io/issues/1231231231/",
        "logger": null,
        "level": "error",
        "status": "unresolved",
        "statusDetails": {},
        "substatus": "ongoing",
        "isPublic": false,
        "platform": "javascript",
        "project": {
            "id": "2342342342342342",
            "name": "PROJ-NAME",
            "slug": "PROJ-NAME",
            "platform": "javascript-react"
        },
        "type": "default",
        "metadata": {
            "title": "event title",
            "sdk": {
                "name": "sentry.javascript.react",
                "name_normalized": "sentry.javascript.react"
            },
            "severity": 0.0,
            "severity_reason": "ml",
            "initial_priority": 50
        },
        "numComments": 2,
        "assignedTo": null,
        "isBookmarked": false,
        "isSubscribed": false,
        "subscriptionDetails": null,
        "hasSeen": true,
        "annotations": [],
        "issueType": "error",
        "issueCategory": "error",
        "priority": "medium",
        "priorityLockedAt": null,
        "isUnhandled": false,
        "count": "529",
        "userCount": 0,
        "firstSeen": "2024-08-06T06:28:45.231000Z",
        "lastSeen": "2024-12-13T23:40:23.433000Z",
        "stats": {
            "24h": [
                [
                    1734062400,
                    1
                ],
                [
                    1734066000,
                    0
                ],
                [
                    1734069600,
                    0
                ],
                [
                    1734073200,
                    0
                ]
            ]
        }
    },
    {
        "id": "3213213211",
        "shareId": null,
        "shortId": "PROJ-NAME-3S",
        "title": "event title",
        "culprit": "file:///C:/Program%20Files/index.html",
        "permalink": "https://org-slug.sentry.io/issues/3213213211/",
        "logger": null,
        "level": "error",
        "status": "unresolved",
        "statusDetails": {},
        "substatus": "ongoing",
        "isPublic": false,
        "platform": "javascript",
        "project": {
            "id": "2342342342342342",
            "name": "PROJ-NAME",
            "slug": "PROJ-NAME",
            "platform": "javascript-react"
        },
        "type": "default",
        "metadata": {
            "title": "event title",
            "sdk": {
                "name": "sentry.javascript.react",
                "name_normalized": "sentry.javascript.react"
            },
            "initial_priority": 75
        },
        "numComments": 2,
        "assignedTo": null,
        "isBookmarked": false,
        "isSubscribed": false,
        "subscriptionDetails": null,
        "hasSeen": true,
        "annotations": [],
        "issueType": "error",
        "issueCategory": "error",
        "priority": "high",
        "priorityLockedAt": null,
        "isUnhandled": false,
        "count": "116",
        "userCount": 0,
        "firstSeen": "2024-09-06T03:35:12.429000Z",
        "lastSeen": "2024-12-13T16:27:21.411000Z",
        "stats": {
            "24h": [
                [
                    1734062400,
                    1
                ],
                [
                    1734066000,
                    2
                ],
                [
                    1734069600,
                    0
                ]
            ]
        }
    }
]
"""

# An example of a response from Sentry's call to get attachments
sentry_mock_get_attachments = """
[
    {
        "id": "111111111111",
        "event_id": "a5114c24626c4296ba83ce55555555555",
        "type": "event.attachment",
        "name": "file.log",
        "mimetype": "text/plain",
        "dateCreated": "2024-12-13T16:27:28.595876Z",
        "size": 315888,
        "headers": {
            "Content-Type": "text/plain"
        },
        "sha1": "12e920e4c5b584d833e8de20411231231231"
    }
]
"""