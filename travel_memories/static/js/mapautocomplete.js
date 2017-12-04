var autocomplete;
var input = $('#location-input')[0];

function initAutocomplete() {
  autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.addListener('place_changed', completeCity)
  
}

function completeCity(){
  let place = autocomplete.getPlace();
  console.log(place);
  $(input).val(place.formatted_address);
  $('#id_lat').val(parseFloat(place.geometry.location.lat().toFixed(6)));
  $('#id_lng').val(parseFloat(place.geometry.location.lng().toFixed(6)));
  
}