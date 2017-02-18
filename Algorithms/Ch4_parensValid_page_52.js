function parensValid(string){
var strarr = string.split("");
var count = 0;

	for(var x = 0; x < strarr.length; x++){
		if(string[x] == ")" && count != 0) {
			count += 1;
			break;
		}
		var index = x;
			if(strarr[x] == "("){
				count += 1;
				index += 1;
					while(index < strarr.length){
						if(strarr[index] == ")"){
							count-=1;
						}
						if(strarr[index] == "("){
							count += 1;
						}
						if(count == 0){
							break;
						}
						index++;

					}
			}
		}
	if(count == 0){
		return true;
	} else {
		return false;
	}
}

console.log(parensValid("(B)(A)"));
