function solution(s) {
    let answer = s;
    const enNumArray = [
        /zero/i,
        /one/i,
        /two/i,
        /three/i,
        /four/i,
        /five/i,
        /six/i,
        /seven/i,
        /eight/i,
        /nine/i,
    ];
    for (let i = 0; i < enNumArray.length; i++) {
        while (answer.match(enNumArray[i])) {
            answer = answer.replace(enNumArray[i], i);
        }
    }
    return Number(answer);
}
