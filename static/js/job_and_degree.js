var app = angular.module('app',['ui.bootstrap','ngAnimate'])

app.controller('ctrl', ['$scope', function($scope) {
	console.log('test')
	$scope.step = "one";
	$scope.selected = false;

	$scope.skillnames=['Java','Ruby','C++/C','SQL','ASP.NET','Perl','HTML/CSS','Javascript',
	'AJAX','XML','Server','Objective-C','Swift','PHP','JSON','API','Data Structure','Algorithms',
	'UI/UX','Sketch','Graphic Design','Adobe Creative Suite'];
	$scope.degreenames=['Computer Science','Information science','Design','Other'];
	$scope.idealjobnames=['Frontend Developer','UI/UX Designer','Backend Developer','Project Manager','Web Developer'];
	$scope.samplequestion=[
		{testskill:"Data Structure",
		description:"Is it possible to find a loop in a Linked list?",
		rightanswer:"a",
		answera:"Possible at O(n)",
		answerb:"Not possible",
		answerc:"Possible at O(n^2) only",
		answerd:"Depends on the position of loop"},
	];

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


	$scope.adddegreetodegreelist = function(){
		var degreelist= [];
		for (i = 0; i < $scope.degreenames.length; i++){
			var s = $scope.degreenames[i];

			degreelist.push({
		    degree:s,
		    selected: false
			});
		};
		return degreelist;

	};

	$scope.addidealjobnamestojoblist = function(){
		var joblist= [];
		for (i = 0; i < $scope.idealjobnames.length; i++){
			var s = $scope.idealjobnames[i];
			joblist.push({
		    job:s,
		    selected: false
			});
		};
		return joblist;
	};

	$scope.setalltofalse=function(){
		for (i = 0; i < $scope.joblist.length; i++){
			var item = $scope.joblist[i];
			item.selected = false;
		};

		for (i = 0; i < $scope.degreelist.length; i++){
			var item = $scope.degreelist[i];
			item.selected = false;
		};

		for (i = 0; i < $scope.skillset.length; i++){
			var item = $scope.skillset[i];
			item.selected = false;
		};
	}

	$scope.ischosen = function(item){
		item.selected = !item.selected;
		console.log('settotrue');
	};

	$scope.clickedagain = function(item){
		item.selected = false;
		console.log('settofalse');
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

	$scope.stepeight = function(){
		console.log('8')
		$scope.step = "eight"
	};

	$scope.stepnine = function(){
		console.log('9')
		$scope.step = "nine";
	};

	$scope.skillset = $scope.addskillnamestoskillset();
	$scope.degreelist = $scope.adddegreetodegreelist();
	$scope.joblist = $scope.addidealjobnamestojoblist();


}]);

