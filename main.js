document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault(); // impede o envio do formulário

    // obtém os valores dos campos A e B
    let campoA = parseInt(document.getElementById("campoA").value);
    let campoB = parseInt(document.getElementById("campoB").value);
    

    let campo = parseInt(campoA);
    let campo2 = parseInt(campoB);



// verifica se o valor do campo B é maior que o valor do campo A
    if (campo2 > campo) {
        alert("Formulário válido!");
    } else {
        (campo2 < campo) 
            alert("Formulário inválido!");
}});

