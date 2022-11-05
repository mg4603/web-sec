
function encodePayload(payloadString)
{
    let encodedPayload = ""
    for(let i = 0; i < payloadString; i++){
        encodedPayload += payloadString.charCodeAt(i);
    }
    return encodePayload;
}

// String.fromCharCode(encodedPayload)