// URL en uso: /movimientos/prestamo/nuevo/
// html en uso: /movimientos/prestamo/prestamo-nuevo.html

// AUTOCOMPLETADO
let clienteInput = document.getElementById('cliente');

clienteInput.addEventListener('keyup', function() {
  console.log(this.value);
  if (this.value.length >= 2) {
    let url = '/cliente/api-buscar/' + this.value;
    console.log(url);
  }
});

function busquedaClientesGET(url) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    if (request.readyState == 4 && request.status == 200) {
      console.log(request.response);
    }
  }

  request.open('GET', url, true);
  request.send();
  
}
// GUARDAR
let botonGuardar = document.getElementById('guardar');

