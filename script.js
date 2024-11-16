document.addEventListener('DOMContentLoaded', function() {
    const actionBtns = document.querySelectorAll('.action-btn');
    const containers = document.querySelectorAll('.container');
    const closeBtns = document.querySelectorAll('.fechar');
    // Selecionando os itens de cada classe

    // Adiciona um evento de clique a cada botão de ação
    actionBtns.forEach(function(button, index) {
        button.addEventListener('click', function() {
            // Quando o botão for clicado, adiciona a classe 'show' ao container correspondente
            containers[index].classList.add('show');
        });
    });

    // Adiciona um evento de clique a cada botão de fechamento
    closeBtns.forEach(function(button, index) {
        button.addEventListener('click', function() {
            // Quando o botão de fechar for clicado, remove a classe 'show' do container correspondente
            containers[index].classList.remove('show');
        });
    });
});
