const id = document.querySelector("#uid").value

document.querySelector("#create").addEventListener("click", () => {
    //Status e Iniciação par retorno
    let status = document.querySelector(".status");
    status.innerHTML = ''

    //Confirmação de Senha
    let senha = document.querySelector("form input[name=password]").value
    let senhaconf = document.querySelector("form input[name=confirmPassword]").value
    
    if (senha != senhaconf){
        status.innerHTML = '<a style="color:red">Erro! Senhas não coincidem</a>'
        jumpScroll()
        return
    }     
    
    //coleta de dados
    let data = {
        "responsavel": parseInt(document.querySelector("form input[name=responsavel]").value),
        "username": document.querySelector("form input[name=username]").value,
        "nome": document.querySelector("form input[name=nome]").value,
        "cpf": document.querySelector("form input[name=cpf]").value,
        "data_nasc": document.querySelector("form input[name=data_nasc]").value,
        "senha": senhaconf,
        "cep": parseInt(document.querySelector("form input[name=cep]").value),
        "endereco": document.querySelector("form input[name=logradouro]").value,
        "numero": parseInt(document.querySelector("form input[name=numero]").value),
        "bairro": document.querySelector("form input[name=bairro]").value,
        "cidade": document.querySelector("form input[name=cidade]").value,
        "uf": document.querySelector("form input[name=uf]").value
    }

    // Try para insersão via API
    let res = request_auth(`/api/aluno/create/`, "POST", data);
    if (res.status == 200) {
        status.innerHTML = '<a style="color:green">Cadastrado com sucesso!</a>'
        jumpScroll()
    } else {
        status.innerHTML = '<a style="color:red">Erro! Revise os dados.</a>'
        jumpScroll()
    }
})

// Função via CEP
async function buscarCep(event) {
    let cont = 0;
    let input = event.target.value;
    let cep = input.match(/\d+/g).join('');

    let res = await fetch("https://viacep.com.br/ws/" + cep + "/json");
    if (res.status == 200) {
        let endereco = await res.json();
        let cidade = document.querySelector("form input[name=cidade]");
        cidade.value = endereco.localidade;
        let uf = document.querySelector("form input[name=uf]");
        uf.value = endereco.uf;
        let bairro = document.querySelector("form input[name=bairro]");
        bairro.value = endereco.bairro;
        let logradouro = document.querySelector("form input[name=logradouro]");
        logradouro.value = endereco.logradouro;
        let numero = document.querySelector("form input[name=numero]");

        if (bairro.value == "") {
            bairro.focus();
        } else if (logradouro.value == "") {
            logradouro.focus();
        } else if (numero.value == "") {
            numero.focus();
        }
    }
}

// Direciona o usuário para o TOP da page
function jumpScroll() {
    window.scrollTo(0, 0);
}