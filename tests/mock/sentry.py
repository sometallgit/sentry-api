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