from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateOrientador:
    id: int
    data_nasc: str
    endereco: str
    bairro: str
    cidade: str
    numero: int
    uf: str
    cep: int
    voluntario: bool