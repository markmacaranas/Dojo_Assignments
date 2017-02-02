function finalCountdown(x, y, z, n){
  var i = y;
    while (i <= z){
      if(i % n == 0){
        i++;
      }
      else if (i % x == 0){
        console.log(i);
          i++;
      }
      else{
        i++;
      }
    }
  }
finalCountdown(3,5,17,9);
