// var varFunction = 0;
// varFunction(varFunction);
// varFunction = function(varFunction) {
// 	console.log("How will this get hoisted?")
// }


awesome();
function awesome() {
	console.log("too good to be true");
}

function awesome() {
	console.log("too good to be true");
}
awesome();

// varFunction();
// var varFunction = function() {
// 	console.log("How will this get hoisted?")
// }

var varFunction;
varFunction();
varFunction = function () {
	console.log("How will this hoisted?")
}
