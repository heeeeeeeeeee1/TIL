//ES Module system
import mul, {add, sub } from "./math.js" // ESM 사용시 확장자 이름 필수!
// export default로 내보낸 값은 중괄호 없이 import. mul처럼 이름 변경 가능

import randomColor from "randomcolor" // 라이브러리 값 불러올 때는 라이브러리 이름 명시
const color = randomColor()
console.log(color)


//CJS(Common JS)
// module.exports로 내보낸 값을 내장함수 require이용해서 사용 가능
// const moduleData = require("./math")
// console.log(moduleData) // moduleData는 객체
// console.log(moduleData.add(1,2))
// console.log(moduleData.sub(1,2))


// 구조 분해 할당 이용 시
// const { add, sub } = require("./math")
// console.log(add(1,2))
// console.log(sub(1,2))