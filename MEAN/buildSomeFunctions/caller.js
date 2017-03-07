// function phone(){
// 	console.log("Baller!")
// }
// function caller(parameter){
// 	typeof(parameter);
// 	return parameter;
// }
// 	console.log(caller(phone))



function caller(someParam){
	if (typeof someParam === "function"){
		console.log("It's a function!");
		someParam();
	}
}

caller(function(){
	console.log("hey there")
});

function someFunc(){
	console.log("hey there, i am a function!")

}
