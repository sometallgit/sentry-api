from abc import ABC, abstractmethod
from requests import Response

from .api_config import ApiConfig

class Api(ABC):
    @abstractmethod
    #pragma: no cover
    def __init__(self, config: ApiConfig) -> None:
        raise NotImplementedError('Not implemented')

    @abstractmethod
    #pragma: no cover
    def get_issues(cls) -> Response:
        raise NotImplementedError('Not implemented')

    @abstractmethod
    #pragma: no cover
    def get_issue_events(cls, issue_id: str) -> Response:
        raise NotImplementedError('Not implemented')
    
    @abstractmethod
    #pragma: no cover
    def get_issue_event_attachments(cls, event_id: str) -> Response:
        raise NotImplementedError('Not implemented')
    
    @abstractmethod
    #pragma: no cover
    def get_issue_event_attachment(cls, event_id: str, attachment_id: str) -> Response:
        raise NotImplementedError('Not implemented')

    @abstractmethod
    #pragma: no cover
    def get_issue_event(cls, issue_id: str, event_id: str) -> Response:
        raise NotImplementedError('Not implemented')