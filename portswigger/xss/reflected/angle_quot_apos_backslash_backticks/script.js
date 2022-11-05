
function encodePayload(payloadString)
{
    let encodedPayload = ""
    for(let i = 0; i < payloadString; i++){
        encodedPayload += payloadString.charCodeAt(i);
    }
    return encodePayload;
}

function preparePayload(encodedPayload){
    return 'String.fromCharCode('+encodedPayload+')';
}

// String.fromCharCode(encodedPayload)