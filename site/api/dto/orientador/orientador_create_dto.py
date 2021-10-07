from dataclasses import dataclass

@dataclass(frozen=True)
class CreateOrientador:
    voluntario: bool
    username: str
    nome: str
    cpf: str
    data_nasc: str
    endereco: str
    bairro: str
    cidade: str
    numero: int
    uf: str
    cep: int
