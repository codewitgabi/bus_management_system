// Mobile nav bar toggler

let navLinks = document.getElementsByClassName("links");
function cls() {
	navLinks[0].style.right = "-200px";
}
function opn() {
	navLinks[0].style.right = "0";
}


// Phone number validation

function validate () {
	var form = document.getElementById("form");
	const phone1 = document.getElementById("phone1");
	
	const phone1Error = document.getElementById("phone1Error");
		
	const p1 = /^0\d{10}$/g;
	const p2 = /^0\d{10}$/g;
	
	if (p1.test(phone1.value)) {
		var bookingData = {
			"first_name": form.fName.value,
			"last_name": form.lName.value,
			"phone": form.phone.value,
			"destination": form.destination.value,
			"departure": form.departure.value
		}

		var datalist = document.getElementById("location");
		var input = document.getElementById("input-destination");
		
		alert(input.value)
		
		for (let i=0; i<datalist.options.length; i++) {
			if (input.value === datalist.options[i].value) {
				var price = datalist.options[i].dataset.price
				break
			}
		}
		
		form.classList.add("hide");
		document.getElementById("payment-id").classList.remove("hide");
		
		alert("Working")
		alert(price)
		
		//sendBookingData(bookingData, price)
		
		paypal.Buttons({
			createOrder: (data, actions) => {
				return actions.order.create({
					purchase_units: [{
						amount: {
							value: price
						}
					}]
				});
			},
			onApprove: (data, actions) => {
				return actions.order.capture().then(function(orderData) {
					console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
					const transaction = orderData.purchase_units[0].payments.captures[0];
					sendBookingData(bookingData, price)
				});
			}
		}).render('#paypal-button-container');
		
		return false

	} else {
		phone1.style.border = "1px solid red";
		phone1Error.style.visibility = "visible";
		phone1Error.innerHTML = "phone number must have a minimum length of 11 0xxxxxxxxxx";
		return false;
	}
}


function sendBookingData (bookingData, price) {
	alert("Working")
	fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken
		},
		body: JSON.stringify({"bookingData": bookingData, "price": price})
	})
	.then(response => {
		return response.json()
	})
	.then(data => {
		alert(data)
		window.location = homepage
	})
	.catch(error => {
		alert(error)
	})
}