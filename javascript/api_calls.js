async function fetchCallWithTryCatch() {
    subobj = new Object();
    try {
        const resp = await fetch("/", {
            method: "post",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify(subObj)
        })
        const rJson = await resp.json()
        setMessage(true, rJson.status_message, 10000);
        resetInputs();
    }
    catch (err) {
        setMessage(false, err.toString(), 10000)
    };
}

async function fetchCallThenCatch() {
    subobj = new Object();
    fetch('/', {
        method: 'post',
        headers: {"content-Type": "application/json"},
        body: JSON.stringify(subObj)
    })
    .then((response) => {
        if (!response.ok) {
            return new Promise.reject(response.text);
        }
    })
    .then((resp) => {
        return resp.json;
    })
    .catch((err) => {
        return err.text;
    })
}