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
            let content = document.querySelector(".content .grid__4")
            content.innerHTML = ''
            
            for (const i of re.oficina) {
                let imgs = `
                    <div class="img__crop">
                    </div>
                `
                let el = document.createElement("div")
                el.className = "card__grid"

                let header = document.createElement("header")
                header.className = "header__card__grid"

                if (i.imagens.length) {
                    imgs = `
                        <div class="img__crop">
                            <img src="${i.imagens[0]}">
                        </div>
                    `
                }

                header.innerHTML = `<span>
                    <a href="#">${i.nome}</a> <br>
                    <span class="orientador__name">
                        Orientador ${i.orientador__user__nome}
                    </span>
                    <br><br>
                    <p class="desc">${i.descricao}</p>
                </span>`

                el.innerHTML = imgs
                el.appendChild(header)
                content.appendChild(el)
            }
        }
    })
}

get_oficinas()