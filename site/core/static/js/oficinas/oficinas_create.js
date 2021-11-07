document.querySelector("#create").addEventListener("click", () => {
    let imgs = document.querySelector("#f_imgs").files

    let data = {
        nome: document.querySelector("#nome").value,
        descricao: document.querySelector("#descricao").value,
        horario_aula: document.querySelector("#horario").value,
        orientador: document.querySelector("#orientador").value,
        local: document.querySelector("#local").value,
        link: document.querySelector("#link").value,
    }

    request_auth(`/api/oficinas/create/`, "POST", data)
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            for (const i of imgs) {
                let form = new FormData()

                form.append('id', re.id)
                form.append('img', i)

                request_auth_for_files(`/api/oficinasimg/add/`, "POST", form)
            }
            window.location.href = `/oficinas/list/`
        } else {
            document.querySelector("#error").innerHTML = re.msg
        }
    })
})  