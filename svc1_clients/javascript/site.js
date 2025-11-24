$(document).ready(function() {
  var frm = $('form')

  frm.submit(function (e) {

    loadCarDetails()

    e.preventDefault()
    return false
  })
})

function loadCarDetails() {
  // get car id
  var car_id = $('input').val()

  // todo: build url
  var url = 'http://localhost:6543/api/autos/' + car_id

  $.get(url).done( function (results){
    populateCarData(results)
  }).fail(function (e){
    if (e.error){
      alert("Error contacting service:")
    }
    else{
      alert("fail: " + e)
    }
  })

}

function populateCarData(car) {
  $('#car_details').fadeout(function(){
    $("#name").text(car.name)
    $("#price").text(car.price)
    $("#year").text(car.year)
    $("#damage").text(car.damage)
    $("#last_seen").text(car.last_seen)
    
    $("#car_details").fadeIn('slow')
  })
}