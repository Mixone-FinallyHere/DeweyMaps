$(document).foundation();


var map = L.map('map').setView([50.83906, 4.35308], 13);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
  maxZoom: 18,
  id: 'c4ptaincrunch.ka5engdh',
  accessToken: 'pk.eyJ1IjoiYzRwdGFpbmNydW5jaCIsImEiOiJUdWVRSENNIn0.qssi5TBLeBinBsXkZKiI6Q'
}).addTo(map);

function remove(arr, item) {
  for(var i = arr.length; i--;) {
    if(arr[i] === item) {
      arr.splice(i, 1);
    }
  }
}

var json_markers = [];
var markers_group = new L.FeatureGroup();
var shown_subcat = [];
map.addLayer(markers_group);

$.ajax({
  url: "/api/markers"
}).done(function(response) {
  json_markers = response;
});

var show_cat = function(cat_id) {
  $('#subcatvav').empty();
  var category = categories[cat_id];
  for (var i = 0; i < category.subcategories.length; i++) {
    subcat = category.subcategories[i];
    $('#subcatvav').append(
      '<div data-id="'
      + subcat.id
      + '" class="subcat">'
      + subcat.name
      + '</div>'
      )

    $('.subcat[data-id="' + subcat.id + '"]').click(function() {
      var id = $(this).attr("data-id");
      if(shown_subcat.indexOf("" + id) >= 0){
        remove(shown_subcat, id);
      }
      else {
        shown_subcat.push(id);
      }
      update_points();
    });
  }

  update_points();
}

var update_points = function() {
  $('.subcat').each(function(i, elem){
    elem = $(elem)
    if(shown_subcat.indexOf(elem.attr('data-id')) >= 0){
      elem.attr('show', "ok")
    }
    else {
      elem.attr('show', "")
    }
  })

  console.log("Updating points. Shown : [" + shown_subcat + "]");
  map.removeLayer(markers_group);
  markers_group = new L.FeatureGroup();
  map.addLayer(markers_group);

    // var icon = L.MakiMarkers.icon({icon: "circle-stroked", color: "#b0b", size: "m"});

    for (var i = 0; i < json_markers.length; i++) {
      marker = json_markers[i];

      var ok = false;
      for (var j = 0; j < marker.subcategories.length; j++) {
        for (var k = 0; k < shown_subcat.length; k++) {
          if (marker.subcategories[j].id == shown_subcat[k]){
            subcat_id = marker.subcategories[j].id;
            ok = true;
          }
        }
      }
      if(ok == true){
        console.log("Adding " + marker.name);
        L.marker([marker.lat, marker.lon])
        .bindPopup(marker.popup)
        .on("click", function(e) {
          map.panTo(e.latlng);
        })
        .addTo(markers_group);
      }
    }
  }

  var categories = {};

  $.ajax({
    url: "/api/categories"
  }).done(function(response) {
    for (var i = 0; i < response.length; i++) {
      var cat = response[i];
      categories[cat.id] = cat;
      $('.category[data-id=' + cat.id + ']').click(function() {
        show_cat($(this).attr('data-id'));
        return false;
      });
      for (var j =  0; j < cat.subcategories.length; j++) {
        console.log(cat.color);
        cat.subcategories[j].color = cat.color;
      };
    }
    // show_cat(1);
  });



  $('#subcatcheck input').hide()
  $('#subcatcheck label').hide()

  var update_selected_cat_form = function() {
    cat_id = $('select[name=category] > option:selected').val();
    $('#subcatcheck input').hide()
    $('#subcatcheck label').hide()
    $('#subcatcheck input[data-cat=' + cat_id + ']').show()
    $('#subcatcheck label[data-cat=' + cat_id + ']').show()
  }

  $('select[name=category]').change(update_selected_cat_form)

  update_selected_cat_form();

  $('#errorsuggest').click(function() {
    $('#pointhelpModal').foundation('reveal', 'open');

    map.once('click', function(e) {
      $('#addPointModal').foundation('reveal', 'open');
      $('input[name=lat]').val(e.latlng.lat);
      $('input[name=lon]').val(e.latlng.lng);
    });
  })

  $('#addpoint').submit(function() {
    $.ajax(
    {
      url: "/addmarker",
      type: "POST",
      data: {
        name: $("#addpoint input[name='name']").val(),
        web: $("#addpoint input[name='web']").val(),
        phone: $("#addpoint input[name='phone']").val(),
        adress: $("#addpoint input[name='adress']").val(),
        lat: $("#addpoint input[name='lat']").val(),
        lon: $("#addpoint input[name='lon']").val(),
        description: $("#addpoint textarea[name='description']").val(),
        subcat: $.map($(':checkbox[name=subcategory\\[\\]]:checked'), function(n, i){
          return n.value;
        }).join(',')
      }
    }
    ).done(function(response){
      $('#addPointModal').foundation('reveal', 'close');
      alert("Votre point a été ajouté !");
    // TODO : reset form
  }).fail(function(r) {
    alert("Le formulaire n'est pas bien rempli");
  });
  return false;
})
