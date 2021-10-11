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