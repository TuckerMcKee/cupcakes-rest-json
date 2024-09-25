const $cupcakeList = $('#cupcake_list');
const $submitBtn = $('#submit-btn');

// create html display for cupcakes
async function showCupcakes() {
  let cupcakes = await getCupcakes();
  $.each(cupcakes, function(val) {
    $cupcakeList.append('<li>' + val.flavor + '</li>');
  });
}

//get cupcakes from api
async function getCupcakes() {
  const response = await axios({
    url: '/api/cupcakes',
    method: "GET"
  })
  return response.json
}

//show cupcakes on dom load
$(showCupcakes)
//update html list when new cupcake is added through form
$submitBtn.click(showCupcakes)






