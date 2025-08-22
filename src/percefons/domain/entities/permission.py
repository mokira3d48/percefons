from dataclasses import dataclass


@dataclass
class Permission:
    name: str
    code_name: str
    id: int = None
