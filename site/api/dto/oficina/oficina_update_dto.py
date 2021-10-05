from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateOficina:
    id: int
    nome: str
    descricao: str
    horario_aula: str
    local: str = ''
    link: str = '' 