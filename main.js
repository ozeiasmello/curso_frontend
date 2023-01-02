$(document).ready(function() {
  // Adiciona uma nova tarefa à lista quando o formulário é enviado
$('#form-tarefa').submit(function(event) {
    event.preventDefault(); // Previne o envio do formulário
    var tarefa = $('#tarefa').val(); // Obtém o valor do campo de entrada
    $('#lista-tarefas').append('<li>' + tarefa + '</li>'); // Adiciona um novo item à lista
    $('#tarefa').val(''); // Limpa o campo de entrada
});

  // Adiciona um evento de clique a cada item da lista
$('#lista-tarefas').on('click', 'li', function() {
    // Aplica o efeito de linha através do texto quando o item é clicado
    $(this).css('text-decoration', 'line-through');
});
});