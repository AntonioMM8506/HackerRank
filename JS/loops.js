'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = ["a", "e", "i", "o", "u"];
    let a = [];
    let b = [];

    for(let i=0; i<s.length; i++){
        (vowels.includes(s[i])) ? a.push(s[i]) : b.push(s[i]) //assuming there are not numbers or symbols, just vowels and consonants 
    }
    
    a.forEach( element => console.log(element));
    b.forEach( element => console.log(element));
    
}//End of vowelsAndConsonants


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}