const get_oficinas = () => {
    request_auth("/api/oficinas/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__3")

            for (const i of re.oficina) {
                let el = document.createElement("div")
                el.className = "card__grid"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                header.innerHTML = `
                    <span>
                        <a href="/oficinas/detail/${i.id}/">${i.nome}</a><br>
                        <span class="orientador__name">Orientador ${i.orientador__user__nome}</span>
                        <br><br>
                        <p class="desc">${i.descricao}</p>
                    </span>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                el.appendChild(card_content)
                content.appendChild(el)
            }
        }
    })
}

get_oficinas()