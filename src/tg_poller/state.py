from dataclasses import dataclass


@dataclass
class Update:
    update_id: int
  

def next_offset(updates: list[Update], prev_offset: int | None = None) -> int:
    base = 0 if prev_offset is None else prev_offset
    if not updates:
        return base
    return max(update.update_id for update in updates) + 1