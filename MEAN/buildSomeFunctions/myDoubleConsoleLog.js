// function myDoubleConsoleLog(parameter1, parameter2){
// 	if (typeof(myDoubleConsoleLog) == 'function' &&  typeof(myDoubleConsoleLog) == 'function'{
// 		console.log(myDoubleConsoleLog(), myDoubleConsoleLog());
// 	}
// }
// myDoubleConsoleLog(myDoubleConsoleLog, myDoubleConsoleLog);


// function myDoubleConsoleLog(paramA, paramB){
// 	if (typeof paramA === "function"){
// 		console.log(paramA())
// 	}
// 	if (typeof paramB === "function"){
// 		console.log(paramB())
// 	}
// }
//
// myDoubleConsoleLog(){
// 	console.log('what is up?')
// 	return 'nothing much'
// }, function(){
// 	return 5
// })


// function myDoubleConsoleLog(param1,param2){
//   if (typeof(param1) == 'function' && typeof(param2) == 'function'){
//     console.log(param1(), param2());
//   }
// }
// myDoubleConsoleLog(stringReturnOne, param2);


//5:
//Medium: Write a function named myDoubleConsoleLog that has two parameters, if the arguments passed to the function are functions, console.log the value that each, when invoked, returns.
function hello(){
 str = "hello";
 return str
}

function world(){
 str = "world"
 return str
}

function myDoubleConsoleLog(hello, world){
	if(typeof(hello) === "function" && typeof(world) === "function");
 console.log(hello(), world())
}
myDoubleConsoleLog(hello,world)
