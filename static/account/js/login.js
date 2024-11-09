document.querySelector('.login-form').addEventListener('submit', function (e) {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        e.preventDefault();
        alert('Por favor, preencha todos os campos.');
    }
});
