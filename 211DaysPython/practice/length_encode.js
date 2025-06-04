function countLetters(inputVal){
    let counter = 1
    const result = []

    for(let i = 0; i < inputVal.length; i++){
        const current = inputVal[i];
        const next = inputVal[i+1];

        if(current !== next){
            result.push([current, counter])
            counter = 1;
        }else{
            counter++;
        }

    }
    console.log(result);
}
var input_ex = "aaaabbcca"
countLetters(input_ex)