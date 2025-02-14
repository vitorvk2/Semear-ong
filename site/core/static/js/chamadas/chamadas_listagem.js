const id = document.querySelector("#uid").value

const make_action = (e, data) => {
    switch (e.target.value) {
        case "1":
            window.location.href = `/chamada/${data.id}/alunos/`
            break;
    
        default:
            break;
    }
}

const get_chamadas = (id) => {
    request_auth(`/api/chamada/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let body = document.querySelector("table.table tbody")
            
            for (const i of re.chamadas) {
                let tr = document.createElement("tr")

                let td1 = document.createElement("td")
                td1.innerHTML = i.id
                tr.appendChild(td1)

                let td2 = document.createElement("td")
                td2.innerHTML = i.decricao
                tr.appendChild(td2)

                let td3 = document.createElement("td")
                td3.innerHTML = new Date(i.created_at).toLocaleString()
                tr.appendChild(td3)

                let td4 = document.createElement("td")
                let select = document.createElement("select")

                select.className = "input"
                select.onchange = (e) => {
                    make_action(e, i)
                }

                select.innerHTML = `
                    <option value="">Ação</option>
                    <option value="1">Lista de alunos</option>
                    `
                // <option value="2">Editar</option>
                // <option value="3">Apagar</option>

                td4.appendChild(select)
                tr.appendChild(td4)
                body.appendChild(tr)
            }
        }
    })
}

get_chamadas(id)