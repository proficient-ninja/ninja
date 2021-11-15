function solution(board, moves) {
    const boardWidth = board[0].length;
    let _board = board;
    let cnt = 0; //터진 인형의 갯수

    let dollNumArr = []; //기계가 뽑은 인형(숫자)를 dollNumArr에 저장한다.
    for (let move of moves) {
        for (let i = 0; i < boardWidth; i++) {
            if (_board[i][move - 1] !== 0) {
                //인형이 있으면 dollNumArr에 인형number을 넣고,
                dollNumArr.push(_board[i][move - 1]);
                _board[i][move - 1] = 0; //인형이 원래 있던 자리는 없다는 표시로 0으로 바꿔준다.
                break;
            }
        }
        const length = dollNumArr.length;
        if (length >= 2) {
            //인형이 2개 이상이면 아래의 코드를 실행
            for (let i = 0; i < length; i++) {
                //dollNumArr의 마지막 인덱스가 undefined가 아니고, 마지막-1 인덱스와 같다면 터진 인형의 갯수를 추가해준다.
                if (
                    dollNumArr[length - 1] &&
                    dollNumArr[length - 1] === dollNumArr[length - 2]
                ) {
                    dollNumArr.splice(-2);
                    cnt += 2;
                }
            }
        }
    }

    return cnt;
}
