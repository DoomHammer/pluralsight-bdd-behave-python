from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict

class WorkoutKind(Enum):
    RUNNING = "running"
    JUMPING = "jumping"
    SWIMMING = "swimming"


@dataclass
class Workout:
    kind: WorkoutKind

    @classmethod
    def from_dict(cls, d: Dict) -> "Workout":
        kind = d.pop("kind")
        if kind not in set(map(lambda e: e[1].value, dict(WorkoutKind.__members__).items())):
            raise ValueError("'{}' is not a WorkoutKind".format(kind))

        return cls(kind=kind)


def do_some_work(x):
    """
    Efficiently computes a simple polynomial

    5 + 3x + 4x^2
    """
    return 5 + x * (3 + x * 4)