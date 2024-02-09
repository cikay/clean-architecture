from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class BaseCreateEntity:
    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)
