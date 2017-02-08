// //Make a function that copies an array, ONLY accepting the items that are numbers.
//
// IT SHOULD RETURN A NEW ARRAY
//
// HINT
//
// Use typeof to determine type (ex: typeof 24 === "number" would be true)


function numbersOnly(arr) {
var newArray = [];

  for(var i = 0; i < arr.length; i++){
    if(typeof(arr[i]) === "number"){
      newArray.push(arr[i])
    }
  }
      return newArray;
}

console.log(numbersOnly(["testing", 1, "testing", 2, "testing", 3]));


function numbersOnlyTwo(arr) {

  for(var i = 0; i < arr.length; i++){
    if(typeof(arr[i]) === "number"){
      arr.splice(i,4);
    }
  }
      return arr;
}

console.log(numbersOnlyTwo(["testing", 1, "testing", 2, "testing", 3]));
