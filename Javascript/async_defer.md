## script 태그의 async와 defer
- 사용자가 HTML 파일을 다운로드 받으면 브라우저가 한줄씩 읽다가(파싱하다가) css와 병합해 DOM 요소로 변환하게 된다. 이 과정 중 script 태그를 만나면 HTML 파싱을 멈추고 js 파일을 서버에서 다운받아 실행하고, 그 이후 다시 파싱한다.

### 1. script 태그가 head에 있는 경우
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <script src="main.js"></script>
</head>
<body></body>
</html>
```
  - 위와 같이 js파일이 헤드 안에 포함될 경우, 브라우저는 HTML을 한 줄씩 분석 후 스크립트를 다운로드하여 실행하게 되므로 스크립트 파일의 용량이 크거나 인터넷이 느리면 페이지 로딩이 지연될 수 있다.

</br>

### 2. script 태그가 body 마지막에 있는 경우(일반적인 경우)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <div></div>
  <script src="main.js"></script>
</body>
</html>
```
  - 바디의 마지막 부분에 스크립트를 포함하면 js파일을 받기전에 페이지가 준비가 되어서 사용자들이 페이지 컨텐츠를 볼 수 있다. 하지만 자바스크립트에 의존성이 큰(사용자가 의미있는 컨텐츠를 보기 위해서 서버에 있는 데이터를 받아오거나 DOM요소를 꾸며주는 등)웹사이트에서는 추가적인 로딩 지연이 발생할 수 있다.

  </br>

### 3. head에서 async 사용
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <script async src="main.js"></script>
</head>
<body>
  <div></div>
</body>
</html>
```
  - `async`는 불리언 타입이기 때문에 선언하는 것만으로도 true로 설정된다.
  - HTML을 파싱하다가 script태그의 async 속성을 만나면 js파일 다운로드 명령 후, 다시 파싱하다가 js파일이 다운로드 완료되면 파싱을 멈추고 다운로드된 js파일을 실행한다. 그 후 나머지 HTML을 파싱한다.
  - 바디 끝에 사용하는 것보다는 파싱이 병렬적으로 일어나므로 js파일을 다운로드 받는 시간을 절약할 수 있다.
  - 하지만 js파일이 HTML파싱 전에 실행되기 때문에 js파일에서 DOM요소를 조작하는 경우 조작하려고 하는 시점에 필요한 DOM 요소가 아직 정의되지 않을 수 있다. 또한 HTML을 파싱하는 동안 언제든지 js파일을 실행하기위해 멈출 수 있기 때문에 사용자가 페이지를 보는데 시간이 여전히 더 걸릴 수 있다는 단점이 있다.
  
  </br>

### 4. haed에서 defer 사용
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <script defer src="main.js"></script>
</head>
<body>
  <div></div>
</body>
</html>
```
- 
  - `defer` 속성을 사용하면 js파일 다운로드 명령 후, HTML 파싱이 모두 끝난 후 자바스크립트를 실행한다. 전체 페이지가 먼저 로드된 후 스크립트가 실행되어 사용자 경험이 개선된다.(HTML을 파싱하는 동안 필요한 자바스크립트를 다운받고, HTML 파싱을 먼저 진행해 사용자에게 페이지를 보여준 다음 바로 이어서 자바스크립트를 실행한다.) 

</br>

### 5. async와 defer 비교
- async로 여러개의 js파일을 실행할 경우 script 순서 상관없이 다운로드 먼저된 순서로 실행된다. 다운로드는 b.js가 먼저 되었는데 b.js를 실행하기 위해 a.js가 선행되어야할 경우 문제가 될 수 있다.
- defer는 필요한 스크립트를 다 다운로드 반은 후 그 순서대로 실행하기 때문에 html파일에 작성한 순서대로 실행된다.

- `async`와 `defer`의 차이는 `async`는 실행 순서가 보장되지 않지만, `defer`는 스크립트의 실행 순서를 보장하므로 자바스크립트의 실행 순서가 중요한 경우 `defer` 사용이 권장된다.

</br>

#### cf. use strict
- 자바스크립트의 유연함은 개발자가 실수를 할 가능성을 높인다.
`use strict`를 사용하면 브라우저에서 오류가 발생하게 하여 불필요한 문제를 예방할 수 있다.