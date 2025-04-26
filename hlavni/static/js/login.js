document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Zastaví normální odeslání formuláře

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'admin') {
        window.location.href = '/admin_dashboard.html'; // Přesměrování na admin dashboard
    } else {
        alert('Špatné jméno nebo heslo!');
    }
});
