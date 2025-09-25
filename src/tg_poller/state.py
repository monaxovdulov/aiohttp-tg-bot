from dataclasses import dataclass


@dataclass
class Update:
    update_id: int
  

def next_offset(updates: list[Update], prev_offset: int | None = None) -> int:
    base = 0 if prev_offset is None else prev_offset
    if not updates:
        return base
    max_id = max(update.update_id for update in updates)
    if max_id < base:
        return base
    return max_id + 1