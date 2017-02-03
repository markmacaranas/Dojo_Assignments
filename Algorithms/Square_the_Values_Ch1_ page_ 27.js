function squareValues (arr){

  for(var i = 0; i < arr.length; i++){
      arr[i] = arr[i] * arr[i];
  }
        return arr;
}

console.log(squareValues([1,3,5]));

function squareValues (arr){

  for(var i = 0; i < arr.length; i++){
      arr[i] = arr[i] * arr[i];

      console.log(arr[i]);
        return arr;
      }
}

squareValues([1,3,5]);
