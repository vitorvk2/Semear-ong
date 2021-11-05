const get_oficinas = () => {
    fetch(
        `/api/oficinasfive/`, 
        {
            method: "GET"
        }
    )
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__5")
            content.innerHTML = ''
            
            for (const i of re.oficina) {
                let el = document.createElement("div")
                el.className = "card__grid"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                header.innerHTML = `<span><a>${i.nome}</a></span>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                card_content.innerHTML = `<span>Orientador ${i.orientador__user__nome}</span><br><br><p>${i.descricao}</p>`

                el.appendChild(card_content)
                content.appendChild(el)
            }
        }
    })
}

get_oficinas()