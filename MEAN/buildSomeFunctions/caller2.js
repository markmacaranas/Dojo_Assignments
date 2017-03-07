function world(){
 console.log("ending?")
}

function str(){
 var str = "interesting"
 return str
}

function caller2(){
 console.log("starting")
 setTimeout(function(){ world(); }, 2000);
}

function myDoubleConsoleLog(caller2, str){
 console.log(caller2, str)
}
myDoubleConsoleLog(caller2(), str())
