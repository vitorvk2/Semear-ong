const request_auth = (url, type, data) => {
    const token = localStorage.getItem('token')
    const validate = localStorage.getItem('validate')

    return fetch(url, {
        method: type,
        body: JSON.stringify(data),
        headers: {
            'Authorization': `Bearer ${token}`,
            'validate': `Bearer ${validate}`,
        }
    })
}

const request_auth_for_files = (url, type, data) => {
    const token = localStorage.getItem('token')
    const validate = localStorage.getItem('validate')

    return fetch(url, {
        method: type,
        body: data,
        headers: {
            'Authorization': `Bearer ${token}`,
            'validate': `Bearer ${validate}`,
        }
    })
} 

const logout = () => {
    localStorage.clear()
    document.cookie = "validate=; Max-Age=-99999999;"
    document.cookie = "token=; Max-Age=-99999999;"
    window.location = "/"
}

const toggle_menu = () => {
    document.querySelector("nav.menu").classList.toggle('active')
}