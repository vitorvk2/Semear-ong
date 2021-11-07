const get_oficinas = () => {
    request_auth("/api/oficinas/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let content = document.querySelector(".content .grid__3")

            for (const i of re.oficina) {
                let el = document.createElement("div")
                let header = document.createElement("header")
                let imgs = `
                    <div class="img__crop">
                    </div>
                `

                el.className = "card__grid"
                header.className = "header__card__grid"

                if (i.imagens.length) {
                    imgs = `
                        <div class="img__crop">
                            <img src="${i.imagens[0]}">
                        </div>
                    `
                }

                header.innerHTML = `
                    <span>
                        <a href="/oficinas/detail/${i.id}/">${i.nome}</a><br>
                        <span class="orientador__name">Orientador ${i.orientador__user__nome}</span>
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