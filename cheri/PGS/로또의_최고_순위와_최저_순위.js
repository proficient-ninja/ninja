function solution(lottos, win_nums) {
    let announceCnt = 0;
    let winCnt = 0;

    // 맞춘 번호 카운팅과 미지정 번호 카운팅
    for (let x of lottos) {
        if (x === 0) {
            announceCnt++;
        }
        if (win_nums.includes(x)) {
            winCnt++;
        }
    }

    //최소등수구하기 : 번호가 1개 이하로 맞으면 6등이므로 조건을 달아주었다.
    const min = winCnt <= 1 ? 6 : 6 - winCnt + 1;

    //최대등수구하기 : 미지정숫자가 6개인 경우를 제외하고, 최소등수에서 미지정숫자를 빼면 최대등수가 된다.
    const max = announceCnt === 6 ? 1 : min - announceCnt;
    return [max, min];
}
