## 호이스팅이란

- 자바스크립트 엔진이 "선언해둔 변수 누구있냐"
- 선언된 변수와 함수를 가져가서 메모리에 기억해둠
- a 호출하면 -> v8:"a나와 봐"
- 함수가 실행되기 전에 안에있는 변수들을 범위의 최상단으로 끌어올리는 것

  cf. const(상수) : 값 안바뀌게 하고 싶을때 // var : ES6이후 사라짐

  ```js
  console.log(a)  // undifined
  var a = 1
  console.log(a)  // 1
  ```
  - 호이스팅시 변수의 선언과 초기화 같이 시켜버림

  ```js
  console.log(a)  // undifined
  a = 1
  var a
  console.log(a)  // 1
  ```

* 전역변수 : 블록 밖에서 선언을 한 어디서든 쓰일 수 있는 변수

* 지역변수 : 블록 {} 안에서 선언된 변수, 블록 안에서만 쓸 수 있음
    ```js
    var a = 2

    function foo () {
      var b = 1
    }
    console.log(b)
    ```

* var는 함수만 지역변수로 호이스팅 되고 나머지는 다 전역 변수로 올림
  ```js
  for(var i=1; i<5; i++) {
    console.log(i)
  }
  console.log(i)
    '''
    1
    2
    3
    4
    5
    '''
    ```

* var는 변수 이름 중복 가능
  ```js
  var a = 1
  console.log(a)  // 1
  var a = 2
  console.log(a)  // 2
  ```

* 말이 안되잖아? 없애자 -> let
  ```js
  let a = 1
  console.log(a)
  let a = 2 // SyntaxError: Identifier 'a' has already declared
  console.log(a)
  ```
  

  ```js
  for(let i=1; i<5; i++) {
    console.log(i)
  }
  console.log(i)
  // ReferenceError: i is not defined
  ```

  * let도 호이스팅이 된다.
  ```js
  console.log(a)
  let a = 1
  console.log(a)
  // ReferenceError: Cannot access 'a' before initialization
  ```

  * TDZ(Temporal Death Zone)
    - a가 호이스팅으로 기억 된건 알겠어. 하지만 a 선언문이 나오기 전까지 너는 a에 접근할 수 없어. 일시적으로 너는 죽은 존이야
    - a 초기화문이 나올때 까지는 그 앞에서 얼마나 많이 a를 쓰려고 했던지 간에 a가 선언된 라인 전까지는 a를 쓸 수 없다. TDZ이기 때문.