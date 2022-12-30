$(document).ready(function() {
    // Adicionar uma tarefa na lista
    $('#form-tarefas').submit(function(event) {
      // Prevenir o comportamento padrão do formulário
      event.preventDefault();
      
      // Obter o valor do campo "tarefa"
      var tarefa = $('#tarefa').val();
      
      // Adicionar um item à lista de tarefas
      $('#lista-tarefas').append('<li>' + tarefa + '</li>');
      
      // Limpar o campo "tarefa"
      $('#tarefa').val('');
    });
    
    // Limpar a lista de tarefas
    $('#btn-limpar').click(function() {
      $('#lista-tarefas').empty();
    });
    
    // Aplicar uma linha em cima do texto dos itens da lista
    $('#lista-tarefas').on('click', 'li', function() {
      $(this).toggleClass('concluido');
  });
});