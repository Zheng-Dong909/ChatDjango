document.querySelector('#username-input').focus();

document.querySelector('#login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var username = document.querySelector('#username-input').value;
    var password = document.querySelector('#password-input').value;
    // TODO: send login request to server
});
