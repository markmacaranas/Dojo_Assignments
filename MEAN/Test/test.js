var myarr = [1,5,25,125,42];

// for(var index in myarr){
//     console.log(myarr[index]*5);
// }

for(var i = 0; i < myarr.length; i++){
    console.log(myarr[i]*5)
    console.log("the right ways")
}

var myobject = {
    language: "JavaScript",
    dojo: "Washington DC",
    favorite_instructor: "Minh, no wait Dan AAaaaahh"
}

// Object.keys(myobject).forEach(function(key,value){
//     console.log(key,value,myobject[key]);
// })

for(var key in myobject){
    console.log(key, myobject[key] + " the value");
    console.log(myobject[key]);
}

