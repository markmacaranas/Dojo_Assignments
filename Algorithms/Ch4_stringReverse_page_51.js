function strarr(str){
var strarr = str.split("");
for(var i = 0; i < strarr.length/2; i++){
	var temp = strarr[i];
	strarr[i] = strarr[strarr.length - 1 - i];
	strarr[strarr.length - 1 - i] = temp;
	}
	return strarr.join("")
}

console.log(strarr("creatures"));
