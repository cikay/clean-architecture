from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class BaseEntity:
    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)
