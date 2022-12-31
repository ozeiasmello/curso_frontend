document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault(); // impede o envio do formulário

    // obtém os valores dos campos A e B
    let campoA = document.getElementById("campoA").value;
    let campoB = document.getElementById("campoB").value;
    let campo = parseInt(campoA, campoB);


// verifica se o valor do campo B é maior que o valor do campo A
    if (campoB > campoA) {
        alert("Formulário válido!");
    } else {
        (campoB < campoA) 
            alert("Formulário inválido!");
}});

