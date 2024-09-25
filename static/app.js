const $cupcakeList = $('#cupcake_list');
const $submitBtn = $('#submit-btn');
const $cupcakeForm = $('#cupcake-form');

// create html display for cupcakes
async function showCupcakes() {
  console.log('in show cupcakes')
  let data = await getCupcakes()
  $cupcakeList.html('');
  $.each(data.cupcakes, function(index, val) {
    $cupcakeList.append('<li>' + val.flavor + '</li>');
  });
}

//get cupcakes from api
async function getCupcakes() {
  const response = await axios({
    url: '/api/cupcakes',
    method: "GET"
  })
  console.log(response)
  return response.data
}

//send post request to create new cupcake data
async function createCupcakes() {
  const dataObj = {'flavor':$('#flavor').val(),'size':$('#size').val(),'rating':$('#rating').val(),'image':$('#image').val()}
  const response = await axios({
    url: '/api/cupcakes',
    method: "POST",
    data: dataObj
  })
  console.log(response)
  return response.data
}

//submit handler for form
async function submitEventHandler(e) {
  e.preventDefault()
  console.log('in event handler')
  await createCupcakes()
  await showCupcakes()
}



//update html list when new cupcake is added through form
$cupcakeForm.on('submit',submitEventHandler)


showCupcakes()






