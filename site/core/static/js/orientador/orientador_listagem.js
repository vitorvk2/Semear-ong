const get_orientador = () => {
    request_auth(`/api/orientador/`, "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let body = document.querySelector("table.table tbody")
            
            for (const i of re.orientadores) {
                let tr = document.createElement("tr")
                
                let td1 = document.createElement("td")
                td1.innerHTML = i.id
                tr.appendChild(td1)

                let td2 = document.createElement("td")
                td2.innerHTML = i.user__nome
                tr.appendChild(td2)

                let td3 = document.createElement("td")
                td3.innerHTML = i.user__endereco + ", " + i.user__numero + " " + i.user__bairro + " - " + i.user__cidade + "/" + i.user__uf 
                tr.appendChild(td3)

                let td4 = document.createElement("td")
                td4.innerHTML = i.voluntario ? "Voluntário" : "Não"
                tr.appendChild(td4)

                let td5 = document.createElement("td")
                td5.innerHTML = i.created_at
                tr.appendChild(td5)

                let td6 = document.createElement("td")
                let select = document.createElement("select")

                select.className = "input"
                // select.onchange = (e) => {
                    // make_action(e, i)
                // }

                select.innerHTML = `
                    <option value="">Ação</option>
                    `
                // <option value="2">Editar</option>
                // <option value="3">Apagar</option>

                td6.appendChild(select)
                tr.appendChild(td6)
                body.appendChild(tr)
            }
        }
    })
}

get_orientador()