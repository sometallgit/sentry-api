from abc import ABC, abstractmethod
from requests import Response

class Api(ABC):
    @abstractmethod
    def get_issues(cls) -> Response:
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def get_issue_events(cls, issue_id: str) -> Response:
        raise NotImplementedError('Not implemented')
    
    @abstractmethod
    def get_issue_event_attachments(cls, event_id: str) -> Response:
        raise NotImplementedError('Not implemented')
    
    @abstractmethod
    def get_issue_event_attachment(cls, event_id: str, attachment_id: str) -> Response:
        raise NotImplementedError('Not implemented')