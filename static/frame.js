var map;
var data;
var frame_id = $('body').attr('frame_id');

$.ajax({
  url: "/api/iframes/" + frame_id
}).done(function(response) {
  data = response;

  map = L.map('map').setView([data.center_lat, data.center_lon], data.zoom);
  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    minZoom: 6,
    id: 'c4ptaincrunch.ka5engdh',
    accessToken: 'pk.eyJ1IjoiYzRwdGFpbmNydW5jaCIsImEiOiJUdWVRSENNIn0.qssi5TBLeBinBsXkZKiI6Q'
  }).addTo(map);

  for (var i=0; i < data.points.length; i++) {
    var point = data.points[i];
    L.marker([point.lat, point.lon])
      .bindPopup(point.popup)
      .on("click", function(e) {
        map.panTo(e.latlng);
      })
      .addTo(map);
  };
});
