import * as React from 'react' 
import { useState, useCallback, useRef } from 'react'

// 컴포넌트 선언
const WorldRelay = () => {
  // 단어 상태 관리 (초기값: '제로초')
  const [word, setWord] = useState('제로초')  

  // 입력 필드의 값 상태 관리 (초기값: '')
  const [value, setValue] = useState('')  

  // 결과 메시지 상태 관리 (초기값: '')
  const [result, setResult] = useState('')  

  // input 요소를 직접 접근하기 위한 ref 생성
  const inputEl = useRef<HTMLInputElement>(null)

  // Form 제출 이벤트 핸들러 - useCallback으로 메모이제이션
  const onSubmitForm = useCallback<(e: React.FormEvent) => void>((e) => {
    e.preventDefault()  // 폼 제출 시 페이지 리로드 방지
    const input = inputEl.current  // input 요소에 접근
    if (word[word.length -1] === value[0]) {  // 단어 끝 글자와 입력 값의 첫 글자가 같은지 비교
      setResult('정답')  // 결과 메시지를 '정답'으로 설정
      setWord(value)  // 현재 단어를 입력한 값으로 변경
      setValue('')  // 입력 필드를 비움
      if (input) {  // input 요소가 존재하면
        input.focus()  // 포커스를 input 필드로 이동
      }
    } else {  
      setResult('땡')  // 틀린 경우 결과 메시지를 '땡'으로 설정
      setValue('')  // 입력 필드를 비움
      if (input) {  // input 요소가 존재하면
        input.focus()  // 포커스를 input 필드로 이동
      }
    }
  }, [word, value])  // word와 value가 변경될 때만 새 함수 생성

  // 입력 필드 변경 시 발생하는 이벤트 핸들러
  const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.currentTarget.value)  // 입력 값을 상태에 반영
  }, [])

  return (
    <>
      <div>{word}</div>  {/* 현재 단어 화면에 표시 */}
      <form onSubmit={onSubmitForm}>  {/* form 요소에 onSubmit 이벤트 핸들러 추가 */}
        <input
          ref={inputEl}  // input 요소에 ref를 연결하여 DOM에 직접 접근 가능
          value={value}  // 입력 필드의 값을 상태 value로 바인딩
          onChange={onChange}  // 입력 값이 변경될 때 onChange 이벤트 발생
        />
        <button>입력</button>  
      </form>
      <div>{result}</div>  {/* 결과 메시지 화면에 표시 */}
    </>
  )
}

export default WorldRelay  // 컴포넌트를 모듈로 내보내기
