from dataclasses import dataclass

@dataclass(frozen=True)
class CreateChamada:
    descricao: str
    oficina: int