from dataclasses import dataclass

@dataclass(frozen=True)
class CreateAluno:
    responsavel: int
    username: str
    nome: str
    senha: str
    cpf: str
    data_nasc: str
    endereco: str
    bairro: str
    cidade: str
    numero: int
    uf: str
    cep: int


@dataclass(frozen=True)
class CreateResponsavel:
    nome: str
    cpf: str
    data_nasc: str
    tel: str

