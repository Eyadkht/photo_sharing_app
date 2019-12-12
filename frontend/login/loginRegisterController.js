loginRegisterModule.controller("loginRegisterController", function ($scope, $http, $log, $window) {

	$scope.title = "Login";

	// Creating constants representing the page state (either a login page or a register page)
	$scope.LOGIN = 0;
	$scope.REGISTER = 1;

	$scope.LoginOrRegister = $scope.LOGIN;

	// This function toggles the page between a login or a register page
	$scope.toggleLoginRegister = function () {
		// Switching to the Register UI
		if ($scope.LoginOrRegister == $scope.LOGIN) {
			$scope.title = "Register";
			document.getElementById('loginForm').style.display = "none";
			document.getElementById('registerForm').style.display = "block";
			document.getElementById('toggleLoginRegisterButton').innerHTML = "Already have an account? Login here.";

			// Indicating that the page is now in register mode
			$scope.LoginOrRegister = $scope.REGISTER;
		}
		// Switching to the Login UI
		else if ($scope.LoginOrRegister == $scope.REGISTER) {
			$scope.title = "Login";
			document.getElementById('loginForm').style.display = "block";
			document.getElementById('registerForm').style.display = "none";
			document.getElementById('toggleLoginRegisterButton').innerHTML = "Don't have an account? Register here.";

			// Indicating that the page is now in login mode
			$scope.LoginOrRegister = $scope.LOGIN;
		}
	}



	$scope.username="";
	$scope.password="";

	// Button Pressed - LOGIN
	$scope.save = function (form) {
		//if (!$scope.contactForm.$valid) return;
		console.log("Register User Details"+$scope.username);
		// 
		$http({
			method: 'POST',
			url: 'https://tallyapp.me/api/v1.1/auth/api-token-auth',
			data: {
				"username": $scope.username,
				"password": $scope.password
			}
		}).then(function successCallback(response) {
			// this callback will be called asynchronously
			// when the response is available
			// change to next url 
			
		}, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		});

		$window.location.href = './adminDashboard';
		//$location.url('')
	}
});