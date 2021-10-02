from dataclasses import dataclass

@dataclass(frozen=True)
class CreateChamadaAluno:
    aluno_id: int
    chamada_id: int
    presente: bool