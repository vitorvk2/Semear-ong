const id = document.querySelector("#uid").value
const is_admin = document.querySelector("#adm__ff").value

const get_aluno = (id,edit) => {
    request_auth(`/api/aluno/${id}/`, "GET")
    .then(re => re.json())
    .then(re => {
        document.querySelector(".infos__nome").innerHTML = re.aluno.user__nome

        if (is_admin == "True") {
            document.querySelector(".infos__cpf").innerHTML = re.aluno.user__cpf
        }

        if (edit == 0){
            if (is_admin == "True") {
                document.querySelector(".infos__logra").innerHTML = re.aluno.user__endereco
                document.querySelector(".infos__bairro").innerHTML = re.aluno.user__bairro
                document.querySelector(".infos__num").innerHTML = re.aluno.user__numero
                document.querySelector(".infos__cep").innerHTML = re.aluno.user__cep
                document.querySelector(".cancel_save").style.display = "none"
                document.querySelector(".edit_delet").style.display = "inline"
            }
            document.querySelector(".infos__cidade").innerHTML = re.aluno.user__cidade
            document.querySelector(".infos__datanasc").innerHTML = new Date(re.aluno.user__data_nasc).toLocaleDateString()
            document.querySelector(".infos__uf").innerHTML = re.aluno.user__uf
        } else {
            document.querySelector(".infos__datanasc").innerHTML = `<input class="input" style="width: 320px;" type="date" value="`+re.aluno.user__data_nasc+`"  name="data_nasc">`
            document.querySelector(".infos__cep").innerHTML = `<input type="number" style="width: 320px;" class="input" id="inputs" name="cep" onfocusout="buscarCep(event)" value="`+re.aluno.user__cep+`" required>`
            document.querySelector(".infos__cidade").innerHTML = `<input type="text" style="width: 320px;" class="input" id="inputs" name="cidade" value="`+re.aluno.user__cidade+`" required>`
            document.querySelector(".infos__logra").innerHTML = `<input type="text" style="width: 320px;" class="input" id="inputs" name="logradouro" value="`+re.aluno.user__endereco+`" required>`
            document.querySelector(".infos__bairro").innerHTML = `<input type="text" style="width: 320px;" class="input" id="inputs" name="bairro" value="`+re.aluno.user__bairro+`" required>`
            document.querySelector(".infos__num").innerHTML = `<input type="number" style="width: 320px;" class="input" id="inputs" name="numero" value="`+re.aluno.user__numero+`" required>`
            document.querySelector(".infos__uf").innerHTML = `<input type="text" style="width: 320px;" class="input" id="inputs" name="uf" value="`+re.aluno.user__uf+`" required>`
            document.querySelector(".edit_delet").style.display = "none"   
            document.querySelector(".cancel_save").style.display = "inline"
        }
    })
}

if (is_admin == "True") {
    document.querySelector("#edit").addEventListener("click", () => {
        get_aluno(id, 1)
    })
    
    document.querySelector("#cancel").addEventListener("click", () => {
        get_aluno(id, 0)
    })
    
    document.querySelector("#delete").addEventListener("click", () => {
        if (confirm('Você realmente deseja excluir este aluno?')) {
            // Try para insersão via API
            request_auth(`/api/aluno/delete/`, "DELETE", {
                "id": id
            });
            alert('Deletado com sucesso!')
            window.location.assign("/alunos/list/");
        } else {
            return
        }
    })
    
    document.querySelector("#salve").addEventListener("click", () => {
        //coleta de dados
        let data = {
            "id": id,
            "data_nasc": document.querySelector("input[name=data_nasc]").value,
            "cep": parseInt(document.querySelector("input[name=cep]").value),
            "endereco": document.querySelector("input[name=logradouro]").value,
            "numero": parseInt(document.querySelector("input[name=numero]").value),
            "bairro": document.querySelector("input[name=bairro]").value,
            "cidade": document.querySelector("input[name=cidade]").value,
            "uf": document.querySelector("input[name=uf]").value
        }
    
        // Try para insersão via API
        request_auth(`/api/aluno/update/`, "PUT", data);
        alert('Atualizado com sucesso!')
        document.location.reload(true);
    })
}


// Função via CEP
async function buscarCep(event) {
    let cont = 0;
    let input = event.target.value;
    let cep = input.match(/\d+/g).join('');

    let res = await fetch("https://viacep.com.br/ws/" + cep + "/json");
    if (res.status == 200) {
        let endereco = await res.json();
        let cidade = document.querySelector("input[name=cidade]");
        cidade.value = endereco.localidade;
        let uf = document.querySelector("input[name=uf]");
        uf.value = endereco.uf;
        let bairro = document.querySelector("input[name=bairro]");
        bairro.value = endereco.bairro;
        let logradouro = document.querySelector("input[name=logradouro]");
        logradouro.value = endereco.logradouro;
        let numero = document.querySelector("input[name=numero]");

        if (bairro.value == "") {
            bairro.focus();
        } else if (logradouro.value == "") {
            logradouro.focus();
        } else if (numero.value == "") {
            numero.focus();
        }
    }
}

//Main
get_aluno(id,0)
