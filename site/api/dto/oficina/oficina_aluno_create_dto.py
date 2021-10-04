from dataclasses import dataclass

@dataclass(frozen=True)
class CreateOficinaAluno:
    aluno_id: int
    oficina_id: int
