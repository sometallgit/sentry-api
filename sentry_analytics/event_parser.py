import json

def parse_event(json_file: str) -> list[str]:
	event_ids: list[str] = []
	with open(json_file) as json_data:
		d = json.load(json_data)
		for event in d:
			event_ids.append(event['id'])
			print(event['id'])
			# break

	return event_ids