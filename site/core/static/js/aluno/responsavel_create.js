const id = document.querySelector("#uid").value

document.querySelector("#create").addEventListener("click", () => {
    let data = {
        "nome": document.querySelector("form input[name=nome]").value,
        "cpf": document.querySelector("form input[name=cpf]").value,
        "data_nasc": document.querySelector("form input[name=data_nasc]").value,
        "tel": document.querySelector("form input[name=numero]").value,
    }

    let status = document.querySelector(".status");
    status.innerHTML = ''
    let res = request_auth(`/api/responsavel/create/`, "POST", data);
    if (res.status == 201) {
        status.innerHTML = '<a style="color:green">Cadastrado com sucesso!</a>'
    } else {
        status.innerHTML = '<a style="color:red">Erro! Revise os dados.</a>'
    }
})
