const get_oficina = (id) => {
    request_auth(`/api/oficinas/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let [hora, minuto, _] = re.oficina.horario.split(":")

            document.querySelector(".value__tales").innerHTML = re.oficina.nome
            document.querySelector(".infos__hour").innerHTML = `${hora}:${minuto}`
            document.querySelector(".infos__link").innerHTML = re.oficina.link || '---'
            document.querySelector(".infos__location").innerHTML = re.oficina.local || '---'
            document.querySelector(".infos__orie").innerHTML = re.oficina.orientador__user__nome
            document.querySelector(".infos__created").innerHTML = new Date(re.oficina.created_at).toLocaleString()
            document.querySelector(".infos__desc").innerHTML = re.oficina.descricao
            document.querySelector(".infos__status").innerHTML = re.oficina.is_active ? 'Ativa' : 'Inativa'
            document.querySelector(".infos__chamada a").href = "/chamada/" + re.oficina.id + "/"
        }
    })
}

const id = document.querySelector("#uid").value
get_oficina(id)