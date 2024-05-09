/*This program is used to reverse a given integer and solve the leetcode
on reverse of a string*/

function reverseInteger(intValue){
	/*Convert integer to a list and reverse list directly*/
	var keepSign = "";
	convertToString = intValue.toString();
	if (convertToString[0] == "-"){
		keepSign = convertToString[0];
		convertToString = convertToString.slice(1);
	}
	//reversing the converted user string
	let miniReverseString = "";
	for (let i = convertToString.length - 1; i >= 0; i--){
		miniReverseString += convertToString[i];
	}
	var reversedString = keepSign + miniReverseString; //adding the sign to the converted string

	return reversedString;
}
var integerValue = -9048475;
console.log(reverseInteger(integerValue))
