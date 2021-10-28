const id = document.querySelector("#uid").value

document.querySelector("#create").addEventListener("click", () => {
    let data = {
        "nome": document.querySelector("#nome").value,
        "cpf": document.querySelector("#cpf").value,
        "data_nasc": document.querySelector("#date").value,
        "tel": document.querySelector("#inputs").value,
    }

    let statuus = document.querySelector(".status");
    statuus.innerHTML = ''

    request_auth(`/api/responsavel/create/`, "POST", data)
        .then(re => re.json())
        .then(re => {
            if (re.success) {
                window.location.href = "/alunos/responsavel/list/"
            }
            else {
                statuus.innerHTML = re.msg
            }
        })
})
