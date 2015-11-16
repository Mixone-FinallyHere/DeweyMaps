var map = L.map('map').setView([50.83906, 4.35308], 13);
L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
  maxZoom: 18,
  id: 'c4ptaincrunch.ka5engdh',
  accessToken: 'pk.eyJ1IjoiYzRwdGFpbmNydW5jaCIsImEiOiJUdWVRSENNIn0.qssi5TBLeBinBsXkZKiI6Q'
}).addTo(map);

if(navigator.geolocation) {

  // success
  function displayPos(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    map.setView([lat,lon], 15);
    var icon = L.MakiMarkers.icon({color: "#0033ff", size: "l", icon: "building"});
    L.marker([lat, lon], {icon: icon}).bindPopup("Vous êtes ici").addTo(map);
    var circle = L.circle([lat,lon], 50, {
        fillOpacity: 0.5
    }).addTo(map);

  }

  // error
  function posError(error) {
    //todo?
  }

  navigator.geolocation.getCurrentPosition(displayPos,posError);
}

$(document).ready(function () {
  var tooltip = $('a[title]').qtip({
    position:{
        my: 'left bottom',
        at: 'top right',
        corner:{target:'leftMiddle',tooltip:'rightMiddle'}, //instead of corner:{target:'rightMiddle',tooltip:'leftMiddle'},
        adjust:{screen:true, resize:true}
      },
      show: 'click',
      hide: {
        event: 'unfocus'
    },
});
  var ttapi = tooltips.qtip('api');
});

var json_markers = [];
var markers_group = new L.FeatureGroup();
var shown_subcat = [];
var categories = {};
var color_mapping = {};


map.addLayer(markers_group);

$.ajax({
  url: "/api/markers"
}).done(function(response) {
  json_markers = response;
});


$.ajax({
  url: "/api/categories"
}).done(function(response) {
  for (var i = 0; i < response.length; i++) {
    var cat = response[i];
    categories[cat.id] = cat;
    $('.category[data-id=' + cat.id + ']').click(function() {
      show_cat($(this).attr('data-id'));
      return false;
    })
    for (var j =  0; j < cat.subcategories.length; j++) {
      cat.subcategories[j].color = cat.color;
      color_mapping[cat.subcategories[j].id] = cat.color;
    }
  }
});


$('#subcatcheck input').hide();
$('#subcatcheck label').hide();
$('select[name=category]').change(update_selected_cat_form);
update_selected_cat_form();

$('#errorsuggest').click(error_suggest);

$('#addpoint').submit(submit_form);
