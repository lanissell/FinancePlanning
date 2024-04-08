from abc import ABC, abstractmethod
from dataclasses import dataclass


class DomainObject(ABC):

    def __init__(self, object_id):
        self.object_id = object_id


@dataclass(frozen=True)
class DomainDataClass(ABC):
    object_id: int
