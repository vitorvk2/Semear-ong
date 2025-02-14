document.querySelector("#make__login").addEventListener('click', (e) => {
    e.preventDefault()

    fetch("/api/login_interno/", {
        method: "POST",
        body: JSON.stringify({
            username: document.querySelector("#user").value,
            password: document.querySelector("#password").value
        })
    })
    .then(re => re.json())
    .then(re => {
        console.log(re);
        if (!re.success) {
            document.querySelector("#error").innerHTML = re.msg
            return
        }

        localStorage.setItem('token', re.token)
        localStorage.setItem('validate', re.validate)
        localStorage.setItem('data', JSON.stringify(re.data))

        document.cookie = `token=${re.token}; path=/`
        document.cookie = `validate=${re.validate}; path=/`

        window.location.href = "/oficinas/list/"
    })
})