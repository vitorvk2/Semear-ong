from dataclasses import dataclass

@dataclass(frozen=True)
class DeleteAluno:
    id: int