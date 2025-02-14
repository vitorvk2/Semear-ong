const is_admin = document.querySelector("#adm__ff").value

const get_responsavel = () => {
    request_auth("/api/responsavel/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            let body = document.querySelector("table.table tbody")
            
            for (const i of re.Responsavel) {
                let tr = document.createElement("tr")
                
                let td1 = document.createElement("td")
                td1.innerHTML = i.id
                tr.appendChild(td1)

                let td2 = document.createElement("td")
                td2.innerHTML = i.nome
                tr.appendChild(td2)

                let td3 = document.createElement("td")
                td3.innerHTML = DataFormate(i.created_at)
                tr.appendChild(td3)

                let td4 = document.createElement("td")
                let select = document.createElement("select")

                select.className = "input"
                select.onchange = (e) => {
                    if ((e.target.value == 2) && (is_admin == "True")){
                        window.location.assign("/alunos/detailresp/"+i.id+"/");
                    } else if(( e.target.value == 3) && (is_admin == "True")){
                        if (confirm('Você realmente deseja excluir este aluno?')) {
                            // Try para insersão via API
                            request_auth(`/api/responsavel/delete/`, "DELETE", {
                                "id": i.id
                            });
                            alert('Deletado com sucesso!')
                            window.location.assign("/alunos/responsavel/list/");
                        } else {
                            return
                        }
                    }
                }

                select.innerHTML = `
                    <option value="" selected disabled>Ação</option>
                    {% if admin %}
                        <option value="2">Editar</option>
                        <option value="3">Apagar</option>
                    {% endif %}
                    `

                td4.appendChild(select)
                tr.appendChild(td4)
                body.appendChild(tr)
            }
        }
    })
}

function DataFormate(datapure){
    data = new Date(datapure);
    dataFormatada = data.toLocaleDateString('pt-BR', {timeZone: 'UTC'});
    return dataFormatada;
}



get_responsavel()