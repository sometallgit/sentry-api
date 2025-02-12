from typing import Any

class SentryIssueEvent:
    def __init__(self, json_obj: dict[str, Any]):
        self.json: dict[str, Any] = json_obj


    def get_event_id(self) -> str:
        return self.json['id']

    def get_event_error_message(self) -> str:
        return self.json['context']['errorMessage']