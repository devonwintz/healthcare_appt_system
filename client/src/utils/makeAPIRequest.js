const makeAPIRequest = ({url, method, params, headers, callback}) => 
    fetch(url,{
        method: method,
        headers: headers,
        body: JSON.stringify(params)
    })
    .then((response) => response.json())
    .then((jsonResponse) => callback(jsonResponse))
    .catch((err) => console.log(err));

export default makeAPIRequest
