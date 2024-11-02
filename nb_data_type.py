import dataclasses
import enum
#notecontraption: the contraption that plays the same note multiple times
(True, 1)
class EnemyId(enum.Enum):
    pass
@dataclasses.dataclass(slots = True)
class MM_notecontraption:
    pitch: int
    instrument: int
    rhythm: list[int]