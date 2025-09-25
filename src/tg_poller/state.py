from dataclasses import dataclass


@dataclass
class Update:
    update_id: int
  

def next_offset(updates: list[Update]) -> int:
    return max(update.update_id for update in updates) + 1