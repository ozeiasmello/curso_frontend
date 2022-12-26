
document.getElementById('formulario').addEventListener('submit', function(event) {
    var numeroA = document.getElementById('numeroA').value;
    var numeroB = document.getElementById('numeroB').value;

    if (numeroB >= numeroA) {
    alert('O número B é maior que o número A');
    event.preventDefault();
    } else (numeroB <= numeroA) 
        alert('O número B deve ser maior que o número A');
        event.preventDefault

    }
);
