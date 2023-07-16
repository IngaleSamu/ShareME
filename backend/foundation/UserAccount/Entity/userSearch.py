from dataclasses import dataclass

@dataclass
class SearchParameter:
    name = str
    isActive = bool
    userId = int