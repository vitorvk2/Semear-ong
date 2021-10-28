const get_oficinas = () => {
    fetch(`/api/oficinasfive/`, {method: "GET"} )
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__2")
            content.innerHTML = ''
            
            for (const i of re.oficina) {
                let el = document.createElement("div")
                el.className = "card__grid"
                el.style = "max-width:95%;max-height:95%;"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                header.innerHTML = `<span><a>${i.nome}</a></span>`

                el.appendChild(header)

                let card_content = document.createElement("div")
                card_content.className = "content__card__grid"

                card_content.innerHTML = `<p>${i.descricao}</p><br><span>Orientador ${i.orientador__user__nome}</span>`

                el.appendChild(card_content)
                content.appendChild(el)
            }
        }
    })
}

// Direciona o usuário para o Down da page
function jumpScroll() {
    window.scrollTo(0, 99999);
}

get_oficinas()