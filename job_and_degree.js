var app = angular.module('app',['ui.bootstrap','ngAnimate'])

app.controller('ctrl', ['$scope', function($scope) {
	console.log('test')
	$scope.step = "one";
	$scope.selected = false;
	$scope.skillnames=['Java','Ruby','C++/C','SQL','ASP.NET','Perl','HTML','CSS','Javascript','AJAX','XML','Server','Objective-C','PHP'];

	// $scope.skillset = [
	// 	{skill:"java",selected:false},
	// 	{skill:"Ruby",selected:false},
	// 	{skill:"C++/C",selected:false}
	// ];

	$scope.addskillnamestoskillset = function(){
		console.log('start_to_add_list');
		var skillset= [];
		for (i = 0; i < $scope.skillnames.length; i++){
			var s = $scope.skillnames[i];

			skillset.push({
		    skill:s,
		    selected: false
			});
		};
		return skillset;
	};

	$scope.ischosen = function(item){
		item.selected = true;
		console.log('settotrue');
	};

	$scope.stepone = function(){
		console.log('1')
		$scope.step = "one";
	};

	$scope.steptwo = function(){
		console.log('2')
		$scope.step = "two";
	};

	$scope.stepthree = function(){
		console.log('3')
		$scope.step = "three";
	};

	$scope.stepfour = function(){
		console.log('4')
		$scope.step = "four";
	};

	$scope.stepfive = function(){
		console.log('5')
		$scope.step = "five";
	};

	$scope.stepsix = function(){
		console.log('6')
		$scope.step = "six";
	};

	$scope.stepseven = function(){
		console.log('7')
		$scope.step = "seven";
	};

	$scope.skillset = $scope.addskillnamestoskillset()


}]);

