import logging
from abc import ABC, abstractmethod

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class AbstractRoute(ABC):
    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def report_route(self, dataToLog):
        pass

    def report_route_error(self, dataToLog):
        pass
