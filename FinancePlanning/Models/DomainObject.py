from dataclasses import dataclass


@dataclass(frozen=False)
class DomainObject:
    object_id: int


@dataclass(frozen=True)
class DomainFrozen:
    object_id: int
