from dataclasses import dataclass
import enum

class LevelType(enum.Enum):
    WARNING = enum.auto()
    INFO = enum.auto()
    FAIL = enum.auto()
    SUCCESS = enum.auto()

level_emoji_map = {
    LevelType.WARNING: "⚠️", 
    LevelType.INFO: "ℹ️",
    LevelType.FAIL: "❌", 
    LevelType.SUCCESS: "✅"
}

@dataclass
class Message():
    text: str 
    level : LevelType = LevelType.INFO
