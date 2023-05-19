const paginaInicial = document.getElementById("voltarInicio");

document.addEventListener("keyup", (event)=>{
    
  if (event.code == 'Backspace') {
    paginaInicial.click();
  }
})
