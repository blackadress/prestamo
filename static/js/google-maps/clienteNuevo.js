var mapa, infoWindow, marker;

function initMap() {
	mapa = new google.maps.Map(document.getElementById('mapa'), {
		center: { lat: -13.15878, lng: -74.22321 },
		zoom: 17
	});

	infoWindow = new google.maps.InfoWindow;

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			const pos = {
				lat: position.coords.latitude,
				lng: position.coords.longitude
			};

			document.getElementById('latitud').value = pos.lat;
			document.getElementById('longitud').value = pos.lng;

			const config = {
				position: pos
			};

			marker = new google.maps.Marker({
				position: config.position,
				map: mapa,
				draggable: true
			});

			marker.addListener('dragend', function () {
				document.getElementById("latitud").value = this.getPosition().lat();
				document.getElementById("longitud").value = this.getPosition().lng();
			});

			mapa.setCenter(pos);
		}, function () {
			handleLocationError(true, infoWindow, mapa.getCenter());
		});
	} else {
		handleLocationError(false, infoWindow, mapa.getCenter());
	}
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
	marker = new google.maps.Marker({
		position: pos,
		map: mapa,
		draggable: true
	});
	marker.addListener('dragend', function () {
		document.getElementById("latitud").value = this.getPosition().lat();
		document.getElementById("longitud").value = this.getPosition().lng();
	});
	infoWindow.setPosition(pos);
	infoWindow.setContent(browserHasGeolocation ?
		'Error: El servicio de geolocalización no funcionó.' :
		'Error: Tu navegador no posee servicio de geolocalización, utiliza Google Chrome en su lugar.'
	)
	infoWindow.open(mapa)
}

let botonGuardar = document.getElementById('guardar');
botonGuardar.addEventListener('click', () => {
	const nombres = document.getElementById('nombres').value;
	const apPat = document.getElementById('apPat').value;
	const apMat = document.getElementById('apMat').value;
	const dni = document.getElementById('dni').value;
	const direccion = document.getElementById('direccion').value;
	const latitud = document.getElementById('latitud').value;
	const longitud = document.getElementById('longitud').value;

	let data = {
		nombres: nombres,
		apPat: apPat,
		apMat: apMat,
		dni: dni,
		direccion: direccion,
		latitud: latitud,
		longitud: longitud
	}
	console.log(data);

	// let form = document.getElementsByTagName('form')[0];

	// nuevoClientePOST('/clientes/api-nuevo/', data);
	nuevoClienteJQuery('/clientes/api-nuevo/', data);

});

function nuevoClientePOST(url, data) {
	let request = new XMLHttpRequest();
	request.open('POST', url, true);
	request.setRequestHeader('X-CSRFToken', csrfmiddlewaretoken);
	// request.setRequestHeader('Content-Type', 'aplication/json')
	request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	request.send(JSON.stringify({data: data}));
}

function nuevoClienteJQuery(url, data) {
	$.ajax({
		type: 'POST',
		dataType: 'json',
		url: url,
		data: {
			'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
			'data': JSON.stringify(data)
		},
		success: function() {
			console.log('exito');
		},

	})
}
