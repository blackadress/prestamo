// URL en uso: /movimientos/prestamo/nuevo/
// html en uso: /movimientos/prestamo/prestamo-nuevo.html

// AUTOCOMPLETADO
let clienteInput = document.getElementById('cliente');
var respuestaAJAX;
const fechaActual = new Date();
const year = fechaActual.getFullYear();
const month = ('0' + (fechaActual.getMonth() + 1)).slice(-2);
const day = ('0' + fechaActual.getDate()).slice(-2);

window.onload = function() {
  document.getElementById('plazo').value = year + '-' + month + '-' + day;

  let clienteInput = document.getElementById('cliente');
  window.hinterXHR = new XMLHttpRequest();

  clienteInput.addEventListener('keyup', function(event) {
    hinter(event);
  })
}

function hinter(event) {
  var input = event.target;

  var lista = document.getElementById('nombresAutocomp');

  var min_char = 2;

  if (input.value.length < min_char) {
    return;
  } else {
    window.hinterXHR.abort();

    window.hinterXHR.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var response = JSON.parse(JSON.parse(this.responseText));

        lista.innerHTML = "";

        response.forEach(element => {
          var option = document.createElement('option');
          const nombres = element.fields.nombres;
          const apellidoPat = element.fields.apPaterno;
          const apellidoMat = element.fields.apMaterno;
          option.value = nombres + ' ' + apellidoPat + ' ' + apellidoMat;
          option.id = element.fields.dni;
          
          option.addEventListener('click', function() {
            var inptClienteDNI = document.getElementById('clienteId');  
            inptClienteDNI.value = element.fields.dni;
          })
          lista.appendChild(option);
        });
      }
    }
  }
  window.hinterXHR.open('GET', '/clientes/api-buscar/' + input.value, true);
  window.hinterXHR.send();
}

function onInput() {
  var dniInput = document.getElementById('clienteId');
  var val = document.getElementById('cliente').value;
  var opts = document.getElementById('nombresAutocomp').childNodes;

  for (var i = 0; i< opts.length; i++) {
    console.log(opts[i].value);
    if (opts[i].value === val) {
      dniInput.value = opts[i].id;
      break;
    }
  }
}

// GUARDAR
let botonGuardar = document.getElementById('guardar');
botonGuardar.addEventListener('click', () => {
  const cliente = document.getElementById('clienteId').value;
  const monto = document.getElementById('monto').value;
  const caja = document.getElementById('cajaId').value;
  const supervisor = document.getElementById('supervisorId').value;

  let data = {
    cliente: cliente,
    monto: monto,
    caja: caja,
    supervisor: supervisor
  }
  console.log(data);

  nuevoPrestamoPOST('/movimientos/prestamo/api-nuevo/', data);

});

function nuevoPrestamoPOST(url, data) {
  let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  let request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.setRequestHeader('X-CSRFToken', csrfmiddlewaretoken);
  request.send(JSON.stringify(data));

  // window.location.href = '/movimientos/prestamo/listar/'
}