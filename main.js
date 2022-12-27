document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault(); // impede o envio do formulário
  
    // obtém os valores dos campos A e B
    var campoA = document.getElementById("campoA").value;
    var campoB = document.getElementById("campoB").value;
  
    // verifica se o valor do campo B é maior que o valor do campo A
    if (campoB > campoA) {
      alert("Formulário válido!");
    } else {
      alert("Formulário inválido!");
    }
  });
  