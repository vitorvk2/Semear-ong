const id = document.querySelector("#uid").value

const get_students = (id) => {
    request_auth(`/api/oficinasaluno/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let sts = document.querySelector("table.table tbody")

            for (const i of re.oficina_alunos) {
                let check = document.createElement("input")
                check.type = "checkbox"
                check.className = 'input'

                check.name = i.aluno_id

                let lab = document.createElement('label')
                let ci = document.createElement("div")
                ci.className = "checkbox__input"

                lab.appendChild(check)
                lab.appendChild(ci)

                let td1 = document.createElement("td")
                td1.appendChild(lab)

                let item = document.createElement("tr")
                item.className = "grid__2"

                let el = document.createElement("td")
                el.innerHTML = i.aluno__user__nome

                item.appendChild(el)
                item.appendChild(td1)
                sts.appendChild(item)
            }
        }
    })
}

get_students(id)

document.querySelector("#create").addEventListener("click", () => {
    let data = {
        "descricao": document.querySelector("textarea#desc").value,
        "oficina": parseInt(id)
    }

    request_auth(`/api/chamada/create/`, "POST", data)
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let checks = document.querySelectorAll("table.table tr td input")

            for (const i of checks) {
                let data2 = {
                    "aluno_id": i.name,
                    "chamada_id": re.id,
                    "presente": !i.checked,
                }

                request_auth(`/api/chamadaaluno/create/`, "POST", data2)
            }

            window.location.href = `/chamada/${id}/`
        }
    })
})