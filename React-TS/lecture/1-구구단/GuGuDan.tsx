import * as React from 'react'
import { useState, useRef } from 'react' // 위에서 * 사용으로 import했으므로 한줄에 작성 불가. tsconfig.json에서 "esModuleInterop" 설정하면 한줄 작성 가능하지만 비추천

// <> === React.Fragment
// Babel에서 변환할때 대비하기 위함. React.Fragment, React.createElement를 사용하지 않고 <> </>로 사용할 수 있음
// Babel 설정에서 새로운 JSX Transform이 활성화되어 있다면 React를 임포트하지 않아도 JSX가 변환
// 하지만 기존 설정에서는 JSX가 React.createElement 호출로 변환되므로 React 임포트가 필요할 수 있음
const GuGuDan = () => {
  // useState 사용방법 : import 하거나 React.useState(Math.ceil(Math.random() * 9))로 사용
  const [first, setFirst] = useState(Math.ceil(Math.random() * 9))
  const [second, setSecond] = useState(Math.ceil(Math.random() * 9))
  const [value, setValue] = useState('')
  const [result, setResult] = useState('')
  const inputEl = useRef<HTMLInputElement>(null)  // Generics 사용

  // onSubmit처럼 함수를 분리하는 경우는 타입을 직접 적어주어야 함
  const onSubmitForm = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const input = inputEl.current
    if (parseInt(value) === first * second) { // 정답 맞았다면
      setResult('정답')
      setFirst(Math.ceil(Math.random() * 9))
      setSecond(Math.ceil(Math.random() * 9))
      setValue('')
      if (input) {
        input.focus()
      }
    } else {
      setResult('땡')
      setValue('')
      if (input) {
        input.focus()
      }
    }
  }

  return (
    <>
      <div>{first} 곱하기 {second}는?</div>
      {/* 분리하는 경우 */}
      <form onSubmit={onSubmitForm}>  
        <input
          ref={inputEl}
          type="number"
          value={value}
          onChange={(e) => setValue(e.target.value)}  // 같이 쓰면 매개변수 타입추론 가능 (e: React.ChangeEvent<HTMLInputElement>)
        />
      </form>
      <div>{result}</div>
    </>
  )
}
export default GuGuDan