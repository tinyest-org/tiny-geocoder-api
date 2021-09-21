import logging
from abc import ABC, abstractmethod
from typing import List, Optional

from .dto import GeocodeResponse


class IGeocoder(ABC):
    @abstractmethod
    def geocode(self, q: str) -> Optional[GeocodeResponse]:
        ...



class MultiGeocoder:
    def __init__(self, coders: List[IGeocoder], logger: Optional[logging.Logger] = None) -> None:
        self.coders = coders
        self.logger = logger or logging.getLogger()

    def geocode(self, q: str) -> Optional[GeocodeResponse]:
        resp = None
        for coder in self.coders:
            self.logger.info('coder', coder)
            try:
                resp = coder.geocode(q)
                if resp is not None:
                    break
            except Exception as e:
                self.logger.error(f'Failed to get res with {coder}')
        return resp
