### JavaScript Utilites

- Show Alert
Takes success:Boolean & msg:string. Shows alert with id `addItemAlert`.
Uses Bootstrap classes

    function showAlert(success, msg) {
        let alertItem = window.document.getElementById("addItemAlert");
        if (success) {
            alertItem.innerText = msg
            alertItem.classList.add('text-success')
        } else {
            alertItem.innerText = msg
            alertItem.classList.add('text-danger')
        };

        setTimeout(() => {
            alertItem.innerText = ""
            alertItem.className = "text-center mb-3"
        }, 5000);
    }

***

- Set String to ProperCase
Adds prototype function to String object for making strings propercase

    String.prototype.toProperCase = function () {
        return this.replace(/(^|\s)\S/g, function (t) { return t.toUpperCase() });
    };