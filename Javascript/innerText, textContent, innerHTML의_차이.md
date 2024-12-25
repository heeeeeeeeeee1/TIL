# JavaScript `innerText`, `textContent`, `innerHTML` 비교
* 🤔 여러 실습이나 프로젝트를 하면서, 위 3가지를 사용했을 때 비슷하게 출력되는 것 같아서 어떤 차이가 있는지 궁금했다. 

## HTML 예제
```html
<div id="example">
  <p style="display: none;">숨겨진 텍스트</p>
  <p>보이는 텍스트</p>
</div>
```

## 1. innerText
```javascript
const example = document.getElementById('example');
console.log(example.innerText);

// 결과 :
// 보이는 텍스트
```
  - innerText는 화면에 보이는 텍스트만 반환한다.
  - `<p style="display: none;">숨겨진 텍스트</p>`는 CSS로 숨겨졌으므로 포함되지 않는다.

## 2. textContent
```javascript
const example = document.getElementById('example');
console.log(example.textContent);
// 결과 :
// 숨겨진 텍스트
// 보이는 텍스트
```
  - textContent는 요소의 전체 텍스트를 반환하며, CSS 스타일의 영향을 받지 않는다.
  - 숨겨진 `<p>`의 텍스트도 포함된다.

## 3. innerHTML
```javascript
const example = document.getElementById('example');
console.log(example.innerHTML);
```
- 결과
  ```
  <p style="display: none;">숨겨진 텍스트</p>
  <p>보이는 텍스트</p>
  ```
  - innerHTML은 요소의 HTML 전체 구조를 반환한다.
  - 텍스트뿐만 아니라 HTML 태그(<p> 등)도 포함된다.


</br>

### 주요 차이점 요약

| 속성        | 반환 내용               | CSS 스타일 영향 | 태그 포함 |
|:-----------:|:----------------------:|:--------------:|:--------:|
| innerText   | 보이는 텍스트만         | 있음            | 없음     |
| textContent | 모든 텍스트             | 없음            | 없음     |
| innerHTML   | HTML 구조와 텍스트 포함 | 없음            | 있음     |
