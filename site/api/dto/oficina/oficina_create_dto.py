from dataclasses import dataclass

@dataclass(frozen=True)
class CreateOficina:
    nome: str
    descricao: str
    horario_aula: str
    orientador: int
    local: str = ''
    link: str = '' 
    
