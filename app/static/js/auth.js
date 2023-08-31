$(document).ready(function() {
	$('#loginSubmit').on('click', function(e) {
		e.preventDefault();
		
		var email = $('#email').val();
		var pwd = $('#password').val();
		
		var regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/i;
		
		if(email != "" && pwd != "" ) {
			if(!regex.test(email)) {
		console.log(email)
				$('#msg').html('<span style="color: red;">Invalid email address</span>');
			} else {
		$.ajax({
			method: "POST",
			url: '/login',
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({'email': email, 'password': pwd}),
			dataType: "json",
			success: function(data) {
				//$('#msg').html('<span style="color: green;">Welcome</span>');
				var housesUrl = document.getElementById('houses-url').value;
				window.location.href = housesUrl;
			},
			statusCode: {
				400: function() {
					$('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
				}
			},
			error: function(xhr, textStatus, errorThrown) {
				console.log("Error:", textStatus, errorThrown);
				var errorMsg = "Invalid email/username or password.";
				$('#msg').html('<span style="color: red;">' + errorMsg + '</span>');
			}
		});
		}
	}
	});
	
	$('#logout').on('click', function(e) {
		e.preventDefault();
		
		$.ajax({
			url: '/logout',
			dataType: 'html',
			success: function(data) {
				//$('#msg').html('<span style="color: green;">You are logged off</span>');
				var logoutUrl = document.getElementById('logout-url').value;
				window.location.href = logoutUrl;
			},
			error: function(jqXHR, textStatus, errorThrown) {
				console.log("Got an error:");
				console.log("Status: " + textStatus);
				console.log("Error thrown: " + errorThrown);
				console.log("Response text: " + jqXHR.responseText);
			}
			//error: function(xhr, textStatus, errorThrown) {
			//	console.log("Error:", textStatus, errorThrown);
			//	var errorMsg = "Problem Logging out.";
			//	$('#msg').html('<span style="color: red;">' + errorMsg + '</span>');
			//}
		});
	});
});