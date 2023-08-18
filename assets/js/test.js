async function request(url, method, data) {
    let options = {
        method: method,
    };

    if (['POST', 'PUT', 'DELETE'].includes(method)) {
        options.body = JSON.stringify(data);
    }

    return await fetch(url, options);
}
