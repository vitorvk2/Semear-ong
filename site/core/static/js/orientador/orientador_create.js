document.querySelector("#create").addEventListener("click", () => {
    let data = {
        voluntario: document.querySelector("#voluntario").checked,
        username: document.querySelector("#username").value,
        nome: document.querySelector("#nome").value,
        senha: document.querySelector("#senha").value,
        cpf: document.querySelector("#cpf").value,
        data_nasc: document.querySelector("#dtnasc").value,
        endereco: document.querySelector("#endereco").value,
        bairro: document.querySelector("#bairro").value,
        cidade: document.querySelector("#cidade").value,
        numero: document.querySelector("#numero").value,
        uf: document.querySelector("#uf").value,
        cep: document.querySelector("#cep").value
    }

    request_auth(`/api/orientador/create/`, "POST", data)
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            window.location.href = `/orientador/listagem/`
        } else {
            document.querySelector("#error").innerHTML = re.msg
        }
    })
})  