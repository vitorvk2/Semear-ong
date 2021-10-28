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

                header.innerHTML = `<span><a href="/alunos/detailresp/${i.id}/">${i.nome}</a></span><i class="fas fa-pen"></i>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                el.appendChild(card_content)
                content.appendChild(el)
            }
        }
    })
}

get_responsavel()