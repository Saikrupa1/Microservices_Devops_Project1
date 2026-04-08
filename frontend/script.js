function loadProducts() {
    fetch("http://product-service:5000/products")
        .then(res => res.json())
        .then(data => {
            let list = document.getElementById("product-list");
            list.innerHTML = "";

            data.forEach(p => {
                let li = document.createElement("li");
                li.innerText = p.name;
                list.appendChild(li);
            });
        });
}
