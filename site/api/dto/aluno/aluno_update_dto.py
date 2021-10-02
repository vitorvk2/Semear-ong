from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateChamada:
    id: int
    descricao: str