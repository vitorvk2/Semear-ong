const is_admin = document.querySelector("#adm__ff").value

const get_alunos = () => {
    request_auth("/api/aluno/", "GET")
    .then(re => re.json())
    .then(re => {
        if (re.success) {
            
            let body = document.querySelector("table.table tbody")
            
            for (const i of re.alunos) {
                let tr = document.createElement("tr")
                
                let td1 = document.createElement("td")
                td1.innerHTML = i.id
                tr.appendChild(td1)

                let td2 = document.createElement("td")
                td2.innerHTML = i.user__nome
                tr.appendChild(td2)

                let td3 = document.createElement("td")
                td3.innerHTML = i.user__endereco + ", " + i.user__numero + " - " + i.user__bairro + " - " + i.user__cidade + "/" + i.user__uf 
                tr.appendChild(td3)

                let td5 = document.createElement("td")
                td5.innerHTML = DataFormate(i.created_at)
                tr.appendChild(td5)

                let td6 = document.createElement("td")
                let select = document.createElement("select")

                select.className = "input"
                select.onchange = (e) => {
                    if ((e.target.value == 2) && (is_admin == "True")){
                        window.location.assign("/alunos/detail/"+i.id+"/");
                    } else if (( e.target.value == 3) && (is_admin == "True")){
                        if (confirm('Você realmente deseja excluir este aluno?')) {
                            // Try para insersão via API
                            request_auth(`/api/aluno/delete/`, "DELETE", {
                                "id": i.id
                            });
                            alert('Deletado com sucesso!')
                            window.location.assign("/alunos/list/");
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

                td6.appendChild(select)
                tr.appendChild(td6)
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


get_alunos()
