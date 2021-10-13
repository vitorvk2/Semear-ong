document.querySelector("#create").addEventListener("click", () => {
    let data = {
        "descricao": document.querySelector("textarea#desc").value,
        "oficina": parseInt(id)
    }

    request_auth(`/api/orientador/create/`, "POST", data)
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            window.location.href = `/orientador/listagem/`
        }
    })
})  