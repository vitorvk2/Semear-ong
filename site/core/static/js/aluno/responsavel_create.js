const id = document.querySelector("#uid").value

document.querySelector("#create").addEventListener("click", () => {
    let data = {
        "nome": document.querySelector("form input[name=nome]").value,
        "cpf": document.querySelector("form input[name=cpf]").value,
        "data_nasc": document.querySelector("form input[name=data_nasc]").value,
        "tel": document.querySelector("form input[name=numero]").value,
    }

    let statuus = document.querySelector(".status");
    statuus.innerHTML = ''
    let response = request_auth(`/api/responsavel/create/`, "POST", data);
    console.log(response.status)
    if (response.status == 201 || response.status == 200) {
        statuus.innerHTML = '<a style="color:green">Cadastrado com sucesso!</a>'
    } else {
        statuus.innerHTML = '<a style="color:red">Erro! Revise os dados.</a>'
    }
    
})
