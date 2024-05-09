/* This code is used to pluralise a given word */

function pluralise(word){
	/*This function is used to return the plural of word*/

	var vowelSound = ["a", "e", "i", "o", "u"];
	let plural = "";

	if (vowelSound.includes(word[word.length - 2]) && word[-1] != "s"){
		plural = word + "s";
		return `The plural of the word ${word} is ${plural}`
	}
	else if (word[-1] == "s"){
		plural = word + "'";
		return `The plural of the word is ${word} but if it's a name the plural is ${plural}`
	}
	else if (word[-1] == "y"){
		plural = word.slice(0, (word.length - 1)) + "ies";
		return `The plural of the word ${word} is ${plural}`;
	}
	else if (word.slice((word.length - 2), word.length) == "fe"){
		plural = word.slice(0, (word.length - 2)) + "ves";
		return `The plural of the word ${word} is ${plural}`;
	}else{
		plural = word + "s";
		return `The plural of the word ${word} is ${plural}`;
	}
}

user_word = "knife";
console.log(pluralise(user_word));