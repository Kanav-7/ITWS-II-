var mySolution = require('./details.js'); 
var data = require('itws2-sample-marks-data');


var n = mySolution.getHighestMarks(data);
console.log(n);

var m = mySolution.getSubject2Toppers(data);
console.log(m);

var a =mySolution.getSubjectAverage(data);
console.log(a);

var ga =mySolution.getAbove(data,85);
console.log(ga);
