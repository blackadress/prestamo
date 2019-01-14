var mapa, infoWindow, marker

function initMap() {
    mapa = new google.maps.Map(document.getElementById('mapa'),{
        center: {lat: -13.15878, lng: -74.22321},
        zoom: 15
    });

    console.log(mapa)
    infoWindow = new google.maps.InfoWindow;

    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            console.log(pos);

            const config = {
                position: pos
            };

            marker = new google.maps.Marker({
                position: config.position,
                map: mapa,
                draggable: true
            });

            mapa.setCenter(pos);
        }, function() {
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
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: El servicio de geolocalización no funcionó.' :
        'Error: Tu navegador no posee servicio de geolocalización, utiliza Google Chrome en su lugar.'
        )
    infoWindow.open(mapa)
}

marker.addListener('dragend', function(event){
    document.getElementById("latitud").value=this.getPosition().lat();
    document.getElementById("longitud").value=this.getPosition().lng();
});