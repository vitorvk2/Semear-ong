const get_alunos = () => {
    request_auth("/api/aluno/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__3")
            
            for (const i of re.alunos) {
                let el = document.createElement("div")
                el.className = "card__grid"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                header.innerHTML = `<span><a href="/alunos/detail/${i.id}/">${i.user__nome}</a></span><i class="fas fa-pen"></i>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                card_content.innerHTML = `<p>${i.id}</p><span>Alunos</span>`

                el.appendChild(card_content)
                content.appendChild(el)
            }

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

get_alunos()