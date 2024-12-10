// math 모듈 만들기
function add(a, b) {
    return a + b
}

function sub(a, b) {
    return a - b
}

// ESM
// 함수 앞에 바로 export 사용 가능
// export default: 모듈을 대표하는 기본값 -> 중괄호 없이 import 
export default function multifly(a, b) {
    return a * b
}


// CJS
// module.exports = {
//     add: add,
//     sub, // value와 key값의 이름이 같을 경우 생략 가능
// }
