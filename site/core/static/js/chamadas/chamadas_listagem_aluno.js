const get_chamadas = (id) => {
    request_auth(`/api/chamadaaluno/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let body = document.querySelector("table.table tbody")
            
            for (const i of re.chamada_alunos) {
                let tr = document.createElement("tr")

                let td1 = document.createElement("td")
                td1.innerHTML = i.id
                tr.appendChild(td1)

                let td2 = document.createElement("td")
                td2.innerHTML = i.aluno__user__nome
                tr.appendChild(td2)

                let td3 = document.createElement("td")
                td3.innerHTML = i.chamada__oficina__nome
                tr.appendChild(td3)

                let td4 = document.createElement("td")
                td4.innerHTML = new Date(i.created_at).toLocaleString()
                tr.appendChild(td4)

                let td5 = document.createElement("td")
                td5.innerHTML = i.presente ? "Presente" : "Ausente"
                tr.appendChild(td5)

                body.appendChild(tr)
            }
        }
    })
}


const id = document.querySelector("#uid").value
get_chamadas(id)