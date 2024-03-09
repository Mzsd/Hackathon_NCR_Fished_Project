
// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13); // Centered at latitude 51.505 and longitude -0.09 with zoom level 13

// Fetch the JSON data
fetch('HSBC_atms.json')
    .then(response => response.json())
    .then(data => {
        // Iterate over the points and add markers
        data.forEach(point => {
            var marker = L.marker([point.latitude, point.longitude]).addTo(map);
            marker.bindPopup(`<b>${point.name}</b><br>${point.address}`).openPopup();
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });

// Add base layer (optional)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


// Add a marker
var marker = L.marker([51.5, -0.09]).addTo(map); // Adds a marker at latitude 51.5 and longitude -0.09
marker.bindPopup("<b>Hello world!</b><br>This is a Leaflet map.").openPopup(); // Adds a popup to the marker and opens it by default