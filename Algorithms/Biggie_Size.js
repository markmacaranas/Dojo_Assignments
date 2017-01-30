function makeItBig(arr){
  var arr = [1,3,5,7];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] > 0){
      arr[i] = "Big";
    }
  }
        return arr;

}
        var arr = [1,3,5,7];
            console.log(makeItBig(arr));
