from dataclasses import dataclass


@dataclass(frozen=True)
class EarningSource:

    earning_source_id: int
    name: str
