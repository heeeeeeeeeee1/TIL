import './App.css'
import Viewer from './components/Viewer'
import Controller from './components/Controller'
import { useState, useEffect } from 'react'

function App() {
  const [count, setCount] = useState(0)
  const [input, setInput] = useState("")

  // 첫번째 인수: 콜백 함수, 두번째: 배열
  // 배열의 값이 바뀌게 되면 사이드이펙트로써 콜백함수 실행
  // count state값이 바뀔때 마다 첫번째 인수로 전달한 콜백함수를 실행
  useEffect(()=>{ // useEffect는 두번째 인수인 배열에 무엇을 넣느냐에 따라 다르게 동작
    console.log(`count: ${count} / input: ${input}`)
  }, [count, input]) // 의존성 배열(dependency array: deps)
  
  
  // 이벤트핸들러 만들어서 Controller (자식)컴포넌트에 전달하기
  const onClickButton = (value) => {
    setCount(count + value)
    // useEffect를 사용하지 않고 이벤트핸들러에 console찍으면 안되나?
    // console.log(count) // 안됨. 비동기(함수의 완료 뒤늦게 됨)로 동작하기 때문에 변경되기 이전 값을 콘솔에 출력함
  }
  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section>
        <input value={input} onChange={(e)=>{
          setInput(e.target.value)
        }}/>
      </section>
      <section>
        {/* Viewer 컴포넌트에게 count props로 count state값 전달*/}
        <Viewer count={count} />
      </section>
      <section>
        <Controller onClickButton={onClickButton}/>
      </section>
    </div>
  )
}

export default App
