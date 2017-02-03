function shiftArrayValues(arr){

  for(var i = 0; i < arr.length; i++){
  arr[i] = arr[i +1];
  }
  arr[arr.length - 1] = 0;


    return arr;
}


console.log(shiftArrayValues([1,3,5]));
