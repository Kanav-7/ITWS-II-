var composition = function(f,g) {
	return function(x){return f(g(x));};
};

var nthPowerFunc = function(func,n) {
	var apply = function(x){
		var t = x;
		for(var i=0;i<n;i++)
			t = func(t);
		return t;
	}
	return apply;
};

var composeFunctionsInArray = function(arr) {
	var arr = arr.filter(function(x){return isNaN(x)})
	return function(x){return arr.reduce(composition)(x);};
};	

var average = function(arr){
	return arr.reduce(function(sum,x){return sum+x;},0)/arr.length;
};

var averageMoreThanX = function(arr,x){
	return average(arr.filter(function(a){return a>=x}));
};

var moreThanK = function(arr,k){
	return arr.reduce(function(sum,x){return ((x>=k)?(sum+1):sum);},0);
};

var moreThanKArr = function(arr1,arr2){
	return arr2.map(function(x){return moreThanK(arr1,x);});
};

var createCounter = function(){
    var count = -1;
    return function() {count++; return count;}
}

// Export the definitions for automated evaluation
module.exports.composition = composition;
module.exports.nthPowerFunc = nthPowerFunc;
module.exports.composeFunctionsInArray = composeFunctionsInArray;
module.exports.average = average;
module.exports.averageMoreThanX = averageMoreThanX;
module.exports.moreThanK = moreThanK;
module.exports.moreThanKArr = moreThanKArr;
module.exports.createCounter = createCounter;