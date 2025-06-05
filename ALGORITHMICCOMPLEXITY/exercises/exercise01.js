const scores = [45, 12, 67, 23, 34, 9]

let sorted_scores = []

for (let i = 1; i < scores.length ; i++) {
    let key = scores[i]
    let j = i  - 1
    while (key >= 0 && scores[j] > key) {
        scores[j + 1] = scores[j];
        j--;
    }
    scores[j + 1] = key;
}

console.log(`With while [${scores}]`)


for(const score of scores) {
    if (sorted_scores.length === 0){
        sorted_scores.push(score);
    }
    else {
        let inserted = false
        for(let i = 0; i < sorted_scores.length; i++) {
            if (score  < sorted_scores[i]) {
                sorted_scores.splice(i, 0, score)
                inserted = true;
                break;
            }
        }
        if (! inserted){
            sorted_scores.push(score);}
    }
}
console.log(`With for [${scores}]`)

names = ["Zoe", "Alice", "John", "Bob", "Charlie"]
names_sorted = []

for (let i = 1; i < names.length ; i++) {
    let key = names[i]
    let j = i  - 1
    while (j >= 0 && names[j] > key) {
        names[j + 1] = names[j];
        j--;
    }
    names[j + 1] = key;
}

console.log(`With while [${names}]`)

dates = ["2023-06-05", "2021-12-25", "2022-01-01", "2024-02-14"]

sorted_dates = []

for(const date of dates) {
    if (sorted_dates.length === 0) {
        sorted_dates.push(date)
    }else {
        let inserted = false;
        for(let i = 0; i < sorted_scores.length; i++){
            if (date < sorted_dates[i]){
                sorted_dates.splice(i, 0, date)
                inserted = true;
                break;
            }
        }if(! inserted){
           sorted_dates.push(date)     
        }

    }
}

console.log(`With FOR [${sorted_dates}]`)


for(let i =  1; i < dates.length; i++){
    let key = dates[i];
    let j = i - 1
    while( j >= 0 && dates[j] > key){
        dates[j + 1] = dates[j]
        j--;
    }
    dates[j + 1 ] = key
}



for (let i = 1; i < scores.length ; i++) {
    let key = scores[i]
    let j = i  - 1
    while (key >= 0 && scores[j] > key) {
        scores[j + 1] = scores[j];
        j--;
    }
    scores[j + 1] = key;
}

console.log(`With while [${scores}]`)


for(const score of scores) {
    if (sorted_scores.length === 0){
        sorted_scores.push(score);
    }
    else {
        let inserted = false
        for(let i = 0; i < sorted_scores.length; i++) {
            if (score  < sorted_scores[i]) {
                sorted_scores.splice(i, 0, score)
                inserted = true;
                break;
            }
        }
        if (! inserted){
            sorted_scores.push(score);}
    }
}
console.log(`With for [${scores}]`)

names = ["Zoe", "Alice", "John", "Bob", "Charlie"]
names_sorted = []

for (let i = 1; i < names.length ; i++) {
    let key = names[i]
    let j = i  - 1
    while (j >= 0 && names[j] > key) {
        names[j + 1] = names[j];
        j--;
    }
    names[j + 1] = key;
}

console.log(`With while [${names}]`)

dates = ["2023-06-05", "2021-12-25", "2022-01-01", "2024-02-14"]

sorted_dates = []

for(const date of dates) {
    if (sorted_dates.length === 0) {
        sorted_dates.push(date)
    }else {
        let inserted = false;
        for(let i = 0; i < sorted_scores.length; i++){
            if (date < sorted_dates[i]){
                sorted_dates.splice(i, 0, date)
                inserted = true;
                break;
            }
        }if(! inserted){
           sorted_dates.push(date)     
        }

    }
}

console.log(`With FOR [${sorted_dates}]`)


for(let i =  1; i < dates.length; i++){
    let key = dates[i];
    let j = i - 1
    while( j >= 0 && dates[j] > key){
        dates[j + 1] = dates[j]
        j--;
    }
    dates[ j + 1 ] = key
}

console.log(`With WHILE [${dates}]`)
