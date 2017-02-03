//Java Script for populating deatails.html file

var table = document.getElementById("students");
for(var name in data)
{
	var tr = document.createElement("tr");
	var td1 = document.createElement("td");
	td1.innerHTML = name;
	marks = data[name];
	var td2 = document.createElement("td");
	td2.innerHTML = marks[0];
	var td3 = document.createElement("td");
	td3.innerHTML = marks[1];
	var td4 = document.createElement("td");
	td4.innerHTML = marks[2];
	var td5 = document.createElement("td");
	td5.innerHTML = marks[3];
	var td6 = document.createElement("td");
	td6.innerHTML = marks[4];

	tr.appendChild(td1);
	tr.appendChild(td2);
	tr.appendChild(td3);
	tr.appendChild(td4);
	tr.appendChild(td5);
	tr.appendChild(td6);
	table.appendChild(tr);
}

//Java Script Codes
var getHighestMarks = function(data){
	var max=-1;
	var nameMax;
	for(name in data)
	{	
		var sum=0;
		var marks=data[name];
		for(j=0;j<5;j++)
			sum+=marks[j];
		if(max<sum)
		{
			max=sum;
			nameMax=name;
		}
	}
	return nameMax;
}

var getSubject2Toppers = function(data){
	var mark2=-1;
	for(name in data)
	{
		if(data[name][1]> mark2)
			mark2=data[name][1];
	}
	var name_highest=[];
	for(name in data)
	{
		if(mark2 === data[name][1])
			name_highest.push(name);
	}
	name_highest.sort();
	return name_highest;
}
var getSubjectAverage = function(data){
  	var avg_marks=[];
    var sum_marks=[0,0,0,0,0];
  	var len=0;

  	for(name in data)
  		len++;
    for(name in data)
   	{
		for(i=0;i<5;i++)
		{
		    	sum_marks[i]+=data[name][i];
		}
    }

  	for(i=0;i<5;i++)
  	{
  		sum_marks[i] = sum_marks[i]/len;
		avg_marks.push(sum_marks[i]);	
  	}
  	return avg_marks;
}

var getAbove = function(data,percent){	
	var name_list=[];
	for(name in data)
	{
		var sum=0;
		for(i=0;i<5;i++)
			sum+=data[name][i];
		sum= sum/500;
		if(sum>percent/100)
			name_list.push(name);
	}
	name_list.sort();
	return name_list;
}

//Exporting 

module.exports.getAbove = getAbove;
module.exports.getSubjectAverage = getSubjectAverage;
module.exports.getSubject2Toppers = getSubject2Toppers;
module.exports.getHighestMarks = getHighestMarks;



