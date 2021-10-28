const get_responsavel= (id) => {
    request_auth(`/api/responsavel/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        document.querySelector(".infos__nome").innerHTML = re.responsavel.nome
        document.querySelector(".infos__cpf").innerHTML = re.responsavel.cpf
        document.querySelector(".infos__datanasc").innerHTML = re.responsavel.data_nasc
        document.querySelector(".infos__tel").innerHTML = re.responsavel.tel
    })
}

const id = document.querySelector("#uid").value
get_responsavel(id)

document.querySelector("#delete").addEventListener("click", () => {
    if (confirm('Você realmente deseja excluir este responsavel?')) {
        // Try para insersão via API
        request_auth(`/api/responsavel/delete/`, "DELETE", {
            "id": id
        });
        alert('Deletado com sucesso!')
        window.location.assign("/alunos/list/");
    } else {
        return
    }
    
    
})