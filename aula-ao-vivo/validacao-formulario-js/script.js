// ---------- VALIDAÇÃO FORMULÁRIO ---------- //
const usernameInput = document.getElementById("username");
const usernameLabel = document.querySelector('label[for="username"]');
const usernameHelper = document.getElementById("username-helper");

const emailInput = document.getElementById('email');
const emailLabel = document.getElementById('emailLabel');
const emailHelper = document.getElementById('email-helper');

const idadeInput = document.getElementById('idade');
const idadeLabel = document.querySelector('label[for="idade"]');
const idadeHelper = document.getElementById('idade-helper');

const senhaInput = document.getElementById('senha');
const senhaLabel = document.querySelector('label[for="senha"]');
const senhaHelper = document.getElementById('senha-helper');

const confirmaSenhaInput = document.getElementById('confirma-senha');
const confirmaSenhaLabel = document.querySelector('label[for="confirma-senha"]');
const confirmaSenhaHelper = document.getElementById('confirma-senha-helper');

const submit = document.getElementById('enviar');



function togglePopup(input, label) {
  input.addEventListener('focus', () => {
    label.classList.add('required-popup');
  })
  
  input.addEventListener('blur', () => {
    label.classList.remove('required-popup');
  })
}

togglePopup(usernameInput, usernameLabel);
togglePopup(emailInput, emailLabel);
togglePopup(idadeInput, idadeLabel);
togglePopup(senhaInput, senhaLabel);
togglePopup(confirmaSenhaInput, confirmaSenhaLabel);



// ---------- VALIDAÇÃO USERNAME ---------- //
usernameInput.addEventListener('input', (event) =>{
  const valueUsername = event.target.value;

  if(valueUsername.length <= 3){
    usernameInput.classList.remove('correct');
    usernameInput.classList.add('error');
    usernameHelper.innerText = 'Username precisa ter mais de 3 caracteres';
    usernameHelper.classList.add('visible');
    inputCorretos.usernameInput = false;
  } else{
    usernameInput.classList.remove('error');
    usernameInput.classList.add('correct');
    usernameHelper.classList.remove('visible');
    inputCorretos.usernameInput = true;
  }
})



// ---------- VALIDAÇÃO EMAIL ---------- //
emailInput.addEventListener('input', (event) => {
  const valueEmail = event.target.value;

  if (valueEmail.includes('@') && valueEmail.includes('.com')){
    emailInput.classList.remove('error');
    emailInput.classList.add('correct');
    emailHelper.classList.remove('visible');
    inputCorretos.emailInput = true;
  } else {
    emailInput.classList.remove('correct');
    emailInput.classList.add('error');
    emailHelper.innerText = 'O email precisa incluir um @ e um .com'
    emailHelper.classList.add('visible');
    inputCorretos.emailInput = false;
  }
})



// ---------- VALIDAÇÃO IDADE ---------- //
idadeInput.addEventListener('input', (event) => {
  const valueIdade = event.target.value;

  if(valueIdade < 18){
    idadeInput.classList.remove('correct');
    idadeInput.classList.add('error');
    idadeHelper.innerText = 'Voçê precisa ser maior de 18 anos';
    idadeHelper.classList.add('visible');
    inputCorretos.idadeInput = false;
  }else {
    idadeInput.classList.remove('error');
    idadeInput.classList.add('correct');
    idadeHelper.classList.remove('visible');
    inputCorretos.idadeInput = true;
  }
})



// ---------- VALIDAÇÃO SENHA ---------- //
senhaInput.addEventListener('blur', (event) =>{
  const valueSenha = event.target.value;

  if(valueSenha === ''){
    senhaInput.classList.remove('correct');
    senhaInput.classList.add('error');
    senhaHelper.innerText = 'O campo não pode estar vazio';
    senhaHelper.classList.add('visible');
    inputCorretos.senhaInput = false;
  }else {
    senhaInput.classList.add('correct');
    senhaInput.classList.remove('error');
    senhaHelper.classList.remove('visible');
    inputCorretos.senhaInput = true;
  }
})



// ---------- CONFIRMAR SENHA ---------- //
confirmaSenhaInput.addEventListener('blur', (event) => {
  const valueConfirma = event.target.value;

  if(valueConfirma === senhaInput.value){
    confirmaSenhaInput.classList.add('correct');
    confirmaSenhaInput.classList.remove('error');
    confirmaSenhaHelper.classList.remove('visible');
    inputCorretos.confirmaSenhaInput = true;
  }else{
    confirmaSenhaInput.classList.remove('correct');
    confirmaSenhaInput.classList.add('error');
    confirmaSenhaHelper.innerText = 'As senhas precisam ser iguais'
    confirmaSenhaHelper.classList.add('visible');
    inputCorretos.confirmaSenhaInput = false;
  }
})



// ---------- ENVIAR FORMULÁRIO---------- //
let btnSubmit = document.querySelector('button[type="submit"]');
let inputCorretos = {
  usernameInput: false,
  emailInput: false,
  idadeInput: false,
  senhaInput: false,
  confirmaSenhaInput: false
}

btnSubmit.addEventListener('click', (e)=> {
  if(inputCorretos.usernameInput == false ||
    inputCorretos.emailInput == false ||
    inputCorretos.senhaInput == false ||
    inputCorretos.confirmaSenhaInput == false){
    e.preventDefault()
    alert('Os campos obrigatórios precisam ser preenchidos corretamente')
  }else{
    alert('Formulário Enviado Com Sucesso')
  }
})