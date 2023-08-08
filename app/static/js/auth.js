$(document).ready(function() {
	$('#loginSubmit').on('click', function(e) {
		var email = $("#email").val();
		var password = $("#password").val();

		var jsonData = JSON.stringify({
			email: email,
			password: password
		});

		$.ajax({
			type: "POST",
			url: "/login.html",
			data: jsonData,
			headers: {
				'Content-Type': 'application/json'
			},
			success: function(response) {
				if (response === "Successful login!") {
					$('#msg').text("Login Successful!");
				}
				else {
					$('#msg').text("Invalid credentials!");
				}
			},
			error: function(xhr, status, error) {
				console.error("AJAX Error" + status + " - " + error);
			}
		})
	});
});