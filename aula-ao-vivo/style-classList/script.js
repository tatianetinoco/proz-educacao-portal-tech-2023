

// capturando input e mensagem de erro das tags de USERNAME
const usernameInput = document.getElementById('login-usuario');
const usernameErrorMessage = document.getElementsByClassName('error-text')[0];


// Capturando input e mensagem de erro das tags de PASSWORD
const passwordInput = document.getElementById('login-senha')
const passwordErrorMessage = document.getElementsByClassName('error-text')[1]


// Style button e título
const formsTitle = document.getElementsByClassName('forms_title')[0];
const button = document.querySelector('button');

formsTitle.style.color = '#5151c8';

button.style.color = '#5151c8';
button.style.fontWeight = '600'
button.style.backgroundColor = '#b3b3e6';
button.style.borderRadius = "10px";
button.style.width = '130px';
button.style.border = '3px solid #5151c8';
button.style.boxShadow = '2px 1px 15px 1px #ececf9'



// -=-=-=-=-= SIMULANDO INTERAÇÃO DO USUÁRIO

//const ErrorMessage = document.getElementsByClassName('error-text');
//ErrorMessage[0].classList.add('visible')


// usuário inseriu username errado
// mudar estilização do input e mensagem de erro do username sinalizando que ele errou
usernameInput.classList.add('error')
usernameErrorMessage.classList.add('visible')


// usuário acertou o username mas errou a senha
// mudar estilização do input e mensagem de erro das tags de username sinalizando que ele acertou
usernameInput.classList.remove('error')
usernameInput.classList.add('correct')
usernameErrorMessage.classList.remove('visible')

// mudar estilização do input e mensagem de erro das tags de password sinalizando que ele errou
passwordInput.classList.add('error')
passwordErrorMessage.classList.add('visible')


