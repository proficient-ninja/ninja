// 세 수 중 최솟값
function solution(a, b, c) {
  let answer = 0;

  switch (a < b) {
    case true:
    answer = a;
    switch (answer < c) {
      case true:
      return answer;
    
      case false:
      answer = c;
      return answer;
    }

    case false:
    answer = b;
    switch (answer < c) {
      case true:
      return answer;
      
      case false:
      answer = c;
      return answer;
    }
  }
}
console.log(solution(6, 5, 11));