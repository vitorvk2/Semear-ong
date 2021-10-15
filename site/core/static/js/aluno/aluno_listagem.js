const get_alunos = () => {
    request_auth("/api/aluno/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__3")
            content.innerHTML = ''
            
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
        }
    })
}

const get_responsavel = () => {
    request_auth("/api/responsavel/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__3")
            content.innerHTML = ''

            for (const i of re.Responsavel) {
                let el = document.createElement("div")
                el.className = "card__grid"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                header.innerHTML = `<span><a href="/alunos/detailResp/${i.id}/">${i.nome}</a></span><i class="fas fa-pen"></i>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                card_content.innerHTML = `<p>${i.id}</p><span>Responsaveis</span>`

                el.appendChild(card_content)
                content.appendChild(el)
            }
        }
    })
}


function buscarelemento(event) {
    input = event.target.value;
    let from = document.querySelector(".button_select")

    if (input == 1){
        from.innerHTML = `<a href="/alunos/create/"><button class="main__button">Criar Aluno</button></a>`
        get_alunos()
    } else {
        from.innerHTML = `<a href="/responsavel/create/"><button class="main__button">Criar Responsavel</button></a>`
        get_responsavel()
    }
}


let input = 1