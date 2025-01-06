import * as React from 'react'  // 이제 react import는 안해도 되지 않나
// import * as ReactDOM from 'react-dom' // export default 없으면 애스터리스크 사용해서 import
import WorldRelay from './WordRelay';
import { createRoot } from 'react-dom/client'  // React 18부터 createRoot 사용

// ReactDOM.render(<GuGuDan />, document.querySelector('#root'))

const container = document.getElementById('root') // id가 root인 element를 찾아서 container에 할당
if (container) {  // container가 null이 아닌 경우(즉, 'root' 요소가 존재하는 경우)에만 다음 코드 실행
  const root = createRoot(container);
  root.render(<WorldRelay />);
}

// non-null 단언 연산자 !를 적용
// import * as React from 'react';
// import GuGuDan from './GuGuDan';
// import { createRoot } from 'react-dom/client';

// const container = document.getElementById('root')!; // 'root' 요소가 null이 아님을 단언
// const root = createRoot(container);
// root.render(<GuGuDan />);
// 주의사항 : non-null 단언 연산자 !는 컴파일러에게만 해당 값이 null이 아님을 알리며, 실제 런타임에서는 여전히 null일 가능성이 있다.
// 해당 요소의 존재를 100% 확신할 수 있을 때만 사용하는 것이 좋다. 만약 해당 요소의 존재를 확신할 수 없다면 if 문을 사용하여 null 체크를 수행하는 것이 안전하다.

