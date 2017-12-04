var options = {
  zoom: 2,
  center: {lat: 0, lng: 0},
  styles: [
    {
      featureType: 'water',
      elementType: 'all',
      stylers: [
        { hue: '#5C97BF' },
        { saturation: 66 },
        { visibility: 'on' }
      ]
    },{
      featureType: 'transit',
      elementType: 'all',
      stylers: [
        { hue: '#444444' },
        { saturation: 0 },
        { lightness: -64 },
        { visibility: 'off' }
      ]
    },{
      featureType: 'road.arterial',
      elementType: 'all',
      stylers: [
        { hue: '#444444' },
        { saturation: -100 },
        { lightness: -65 },
        { visibility: 'off' }
      ]
    },{
      featureType: 'road.highway',
      elementType: 'all',
      stylers: [
        { hue: '#bbbbbb' },
        { saturation: -100 },
        { lightness: 26 },
        { visibility: 'simplified' }
      ]
    },{
      featureType: 'road.local',
      elementType: 'all',
      stylers: [
        { hue: '#bbbbbb' },
        { saturation: -100 },
        { lightness: -27 },
        { visibility: 'on' }
      ]
    },{
      featureType: 'water',
      elementType: 'all',
      stylers: [
  
      ]
    },{
      featureType: 'poi',
      elementType: 'all',
      stylers: [
        { hue: '#444444' },
        { saturation: -100 },
        { lightness: -66 },
        { visibility: 'off' }
      ]
    },{
      featureType: 'landscape',
      elementType: 'all',
      stylers: [
        { hue: '#f2f2f2' },
        { saturation: -100 },
        { lightness: 54 },
        { visibility: 'on' }
      ]
    },
  ]
}

function initMap(){
  var master_object = {};
  var mapData = window.mapData;
  console.log('map data', mapData);
  console.log('map running');
  var map = new google.maps.Map(document.getElementById('map'), options);

  let infowindow = new google.maps.InfoWindow()

  function setMarker(loc) {
    let latLng = new google.maps.LatLng(loc.fields.lat, loc.fields.lng)
    let marker = new google.maps.Marker({
      position: latLng,
      map: map,
    });

    let note = '<h2>' + loc.fields.title  + '</h2><p>'+ loc.fields.note +'</p>'

    google.maps.event.addListener(marker, 'click', function(){
      infowindow.close();
      infowindow.setContent(note);
      infowindow.open(map, marker)
    });
  }

  for(let loc in mapData){
    setMarker(mapData[loc]);
  }
}