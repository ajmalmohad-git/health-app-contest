var display = document.getElementById('display')

//extracting and converting it into json
var table = infos
if(table.synopsis != "")
{	
	
	table = JSON.parse(infos)	
	//bmi status
	var condition = table['synopsis'][0]

	//extracting meal
	var meals = table['synopsis'][1]

	var bmi = document.createElement('div')
	bmi.innerHTML = condition

	display.appendChild(bmi)

	var head = document.createElement('div')
	head.innerHTML = "sample meal suggestion  : "
	display.appendChild(head)
	for(var i in meals){

		//to display meals
		var display_meals = document.createElement('div')
		display_meals.innerHTML = i + "=>"+ meals[i]
		display.appendChild(display_meals)
		// console.log(i, " ",meals[i])
	}


}

var text_field = document.getElementById('calories')
var check = document.getElementById('check')

//place to display nutrients details
var display_nutrients = document.getElementById('display_nutrients')

//kinda like reverse proxy, fetching the results from the 
//backend
check.addEventListener('click',async () => {
	display_nutrients.innerHTML = ""
	const aal = await fetch(`/${text_field.value}`)
	var resp = await aal.json()
	var nutree_info = JSON.parse(resp)

	// console.log(nutree_info["items"])
	//looping through the response
	for(var i in nutree_info["items"][0]){
		// console.log(i)
		
		var display_info = document.createElement('div')
		display_info.innerHTML = i + " : " + nutree_info['items'][0][i]
		display_nutrients.appendChild(display_info)
	}

})

var height_measurment = document.getElementById('height_measurment')
var option = document.getElementById('my_option')
option.addEventListener('click',() => {

	if(option.value === 'feet'){
		height_measurment.innerHTML = " "
		var feet = document.createElement('input')
		feet.setAttribute('type','text')
		feet.setAttribute('placeholder','feet')
		feet.setAttribute('name','feet')

		var inch = document.createElement('input')
		inch.setAttribute('type','text')
		inch.setAttribute('placeholder','inch')
		inch.setAttribute('name','inch')

		height_measurment.appendChild(feet)
		height_measurment.appendChild(inch)

	}
	else
	{
		height_measurment.innerHTML = " "
		var text_field = document.createElement('input')
		text_field.setAttribute('type','text')
		text_field.setAttribute('placeholder','Height in cm')
		text_field.setAttribute('name','height')
		height_measurment.appendChild(text_field)
	}
})



// var jam = {sugar_g: 0, fiber_g: 0, serving_size_g: 100, sodium_mg: 695}

// for(i in jam){
// 	console.log(i)
// }
// console.log("workging")






// async function njan(){

// const aal = await fetch('/hello')
// var resp = await aal.json()
// console.log(resp)

// }

// window.onload = njan