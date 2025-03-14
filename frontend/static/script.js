document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("predict-form").addEventListener("submit", function (event) {
        event.preventDefault(); 

        let formData = new FormData(this);

        fetch(window.URL_S, { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            document.getElementById("prediction-result").innerText = "Predicted Price: " + data.prediction;
        })
        .catch(error => console.error("Error:", error));
    });


    var map = L.map('map').setView([52.2298, 21.0118], 12);

    // OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    var marker;

    function onMapClick(e) {
        var lat = e.latlng.lat.toFixed(6);
        var lng = e.latlng.lng.toFixed(6);

        document.getElementById("latitude").value = lat;
        document.getElementById("longitude").value = lng;

        if (marker) {
            map.removeLayer(marker);
        }

        marker = L.marker([lat, lng]).addTo(map)
            .bindPopup("Selected: " + lat + ", " + lng)
            .openPopup();
    }

    map.on('click', onMapClick);

});

