from abc import ABC, abstractmethod
from typing import Optional

from .dto import GeocodeResponse


class IGeocoder(ABC):
    @abstractmethod
    def geocode(self, q: str) -> Optional[GeocodeResponse]:
        ...
