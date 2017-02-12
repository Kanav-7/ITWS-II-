var fifthDay = function(){
	var d = new Date();
	var today = d.getDay();
	today = (today + 5)%7;
	var temp = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
	return temp[today];
};

var altSpaceToUnderscore = function(inpString){
	var string = inpString.trim();
	var count = 0;
	var arr = string.split(" ");
	string = "";

	for(i=0;i<arr.length;i++)
	{	
		string = string.concat(arr[i]);
	if(i!= arr.length-1)
	{
		if(i%2===1)
			string = string.concat("_");
		else
			string = string.concat(" ");
	}
	}
	return string;
};

var interestingSort = function(inpString){
	var arr = inpString.split("");
	var array_1 = arr.filter(function(x){return x <= 'm';});
	var array_2 = arr.filter(function(x){return x > 'm';});
	array_1 = array_1.sort();
	array_1 = array_1.concat(array_2);
	return array_1.join("");
};

var getMeNextFirst = function(inpString){
	var st = inpString.trim();
	var arr = st.split("");
	for(var i=0; i < arr.length - 1 ;i++)
	{
		if(arr[i] == ' ')
		{
			var temp = arr[i];
			arr[i] = arr[i+1];
			arr[i+1] = temp;
			i++;
		}
	}
	return arr.join("").trim();
};

// Export the definitions for automated evaluation
module.exports.fifthDay = fifthDay;
module.exports.altSpaceToUnderscore = altSpaceToUnderscore;
module.exports.interestingSort = interestingSort;
module.exports.getMeNextFirst = getMeNextFirst;
