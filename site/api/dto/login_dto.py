from dataclasses import dataclass

@dataclass(frozen=True)
class MakeLogin:
    username: str
    password: str
