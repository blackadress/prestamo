// URL en uso: /movimientos/prestamo/nuevo/
// html en uso: /movimientos/prestamo/prestamo-nuevo.html

// AUTOCOMPLETADO
let clienteInput = document.getElementById('cliente');
var respuestaAJAX;

clienteInput.addEventListener('keyup', function() {
  if (this.value.length >= 2) {
    let url = '/clientes/api-buscar/' + this.value;
    busquedaClientesGET(url);
  }
  
  console.log(respuestaAJAX);
  let nombres = respuestaAJAX.map(elemento => {
    let nombres = elemento.fields.nombres + ' ' 
        + elemento.fields.apPaterno + ' '
        + elemento.fields.apMaterno;

    return nombres;
  });

  let dnis = respuestaAJAX.map(elemento => elemento.fields.dni);

  autocompletado(this, nombres, dnis);

});


function busquedaClientesGET(url) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    if (request.readyState == 4 && request.status == 200) {
      respuestaAJAX = JSON.parse(request.responseText);
      respuestaAJAX = JSON.parse(respuestaAJAX);      
    }
  }
  request.open('GET', url, true);
  request.send();  
}

function autocompletado(inp, nombres, dnis) {
  var currentFocus;

  inp.addEventListener("input", function(e) {
    var a, b, i, val = this.value;
    closeAllLists();

    if (!val) {return false;}
    currentFocus = -1;

    a = document.createElement('DIV');
    a.setAttribute('id', this.id + 'autocomplete-list');
    a.setAttribute('class', 'autocomplete-items');
    this.parentNode.appendChild(a);

    for (i = 0; i < nombres.length; i++) {
      if (nombres[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
        b = document.createElement('DIV');
        b.innerHTML = '<strong>' + nombres[i].substr(0, val.length) + "</strong>";
        b.innerHTML += nombres[i].substr(val.length);
        b.innerHTML += "<input type='hidden' value '" + nombres[i] + "'>";

        b.addEventListener('click', function(e) {
          inp.value = this.getElementsByTagName('input')[0].value;
          closeAllLists();
        });
        a.appendChild(b);
      }
    }
  });

  inp.addEventListener('keydown', function(e) {
    var x = document.getElementById(this.id + 'autocomplete-list');
    if (x) x = x.getElementsByTagName('div');
    if (e.keyCode == 40) {
      currentFocus++;
      addActive(x);
    } else if (e.keyCode == 13) {
      e.preventDefault();
      if (currentFocus > -1) {
        if (x) x[currentFocus].click();
      }
    }
  });

  function addActive(x) {
    if (!x) return false;
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    console.log('add active', x);
    console.log('current focus', currentFocus);
    x[currentFocus].classList.add('autocomplete-active');
  }

  function removeActive(x) {
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove('autocomplete-active');
    }
  }

  function closeAllLists(elmnt) {
    var x = document.getElementsByClassName('autocomplete-items');
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  document.addEventListener('click', function(e) {
    closeAllLists(e.target)
  })
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