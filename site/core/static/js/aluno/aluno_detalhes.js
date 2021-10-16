const get_aluno = (id) => {
    request_auth(`/api/aluno/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        document.querySelector(".infos__nome").innerHTML = re.aluno.user__nome
        document.querySelector(".infos__cpf").innerHTML = re.aluno.user__cpf
        document.querySelector(".infos__cep").innerHTML = re.aluno.user__cep
        document.querySelector(".infos__cidade").innerHTML = re.aluno.user__cidade
        document.querySelector(".infos__logra").innerHTML = re.aluno.user__endereco
        document.querySelector(".infos__bairro").innerHTML = re.aluno.user__bairro
        document.querySelector(".infos__num").innerHTML = re.aluno.user__numero
        document.querySelector(".infos__uf").innerHTML = re.aluno.user__uf
        document.querySelector(".infos__datanasc").innerHTML = re.aluno.user__data_nasc
    })
}

const id = document.querySelector("#uid").value
get_aluno(id)

document.querySelector("#edit").addEventListener("click", () => {
    alert('editar')


})

document.querySelector("#delete").addEventListener("click", () => {
    if (confirm('Você realmente deseja excluir este aluno?')) {
        // Try para insersão via API
        request_auth(`/api/aluno/delete/`, "DELETE", {
            "id": id
        });
        alert('Deletado com sucesso!')
    } else {
        return
    }
})
