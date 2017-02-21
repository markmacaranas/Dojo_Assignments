function bracesValid(str){
	var dict = {'(':')', '[':']', '{':'}'};
	var brace = [];
	for (var idx = 0; idx < str.length; idx++){
		switch(str[idx]){
			case '(':
				// brace.push(str[idx]);
			case '[':
				// brace.push(str[idx]);
			case '{':
				brace.push(str[idx]);
				break;
			case ')':
				// brace.push(str[idx]);
			case ']':
				// brace.push(str[idx]);
			case '}':
				// brace.push(str[idx]);
		if (brace[brace.length-1] != dict[str[idx]]) {
			brace.pop();
			break;
		} else {
			return false;
		}
		default:
			continue;

	}
}
		return(brace.length === 0 );
}

console.log(bracesValid("({}]"))

// does not work; this is a draft
