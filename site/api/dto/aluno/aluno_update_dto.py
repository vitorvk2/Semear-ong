from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateAluno:
    id: int
    data_nasc: str
    endereco: str
    bairro: str
    cidade: str
    numero: int
    uf: str
    cep: int