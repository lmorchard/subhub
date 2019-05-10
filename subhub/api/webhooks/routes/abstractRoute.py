import logging
from abc import ABC, abstractmethod

from flask import g
from subhub.subhub_dynamodb import WebHookEvent

logger = logging.getLogger('abstract_route')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)

class AbstractRoute(ABC):
    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload


    def report_route(self, dataToLog: object, sent_system: str):
        logger.info(f"data {dataToLog['event_id']} system {sent_system}")
        existing_event = g.webhook_table.get_event(dataToLog["event_id"])
        logger.info(f"existing event {existing_event}")
        if not existing_event:
            logger.info('no existing event')
            new_event = g.webhook_table.new_event(event_id=dataToLog["event_id"], sent_system=sent_system)
            logger.info(f"new event {new_event}")
            saved_event = g.webhook_table.save_event(new_event)
            logger.info(f"new event {dataToLog['event_id']} {saved_event}")
        else:
            logger.info('yes exisiting event')
            update_event = g.webhook_table.append_event(event_id=dataToLog["event_id"], sent_system=sent_system)
            logger.info(f"updated event {dataToLog['event_id']} {update_event}")

    def report_route_error(self, dataToLog):
        pass
