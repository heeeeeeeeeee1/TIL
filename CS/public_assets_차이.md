## 🤔 public 폴더와 assets 폴더의 차이는 무엇일까?
- react로 자기소개 페이지 구현하면서 스택 아이콘들은 어디에 넣어야할지 정확하게 판단이 되지 않았다.

  -> 어떻게 파일에 접근하고 사용하는지 및 파일이 빌드 과정에서 어떻게 처리되는지에 따라 다르다.

</br>

### 1. public 폴더

  - public 폴더는 React 프로젝트의 정적 파일을 저장하는 공간이다.
  - 이 폴더에 있는 파일들은 빌드 시 변환되지 않고 그대로 복사된다.
  - 파일에 접근할 때 절대 경로 사용
  - 파일을 public 폴더에 저장하면 URL을 통해 직접 접근 가능하다.(public/assets/logo.png에 저장된 이미지는 브라우저에서 /assets/logo.png로 접근 가능)

    ```javascript
    <img src="/assets/logo.png" alt="Logo" />
    ```

    * HTML에서 직접 참조해야 하는 파일
      - index.html에서 사용하는 favicon, 외부 JS 라이브러리, CSS 파일
        ```html
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <script src="%PUBLIC_URL%/external-library.js"></script>
        ```
    * 빌드 시 파일 변환이 필요 없는 경우
      - 고정된 이미지나 외부 파일

</br>

### 2. src/assets 폴더

- React 컴포넌트와 함께 사용되는 모듈화된 리소스를 저장하는 공간이다.
- 빌드 시 Webpack(또는 Vite 등 빌드 도구)이 파일을 처리하고 최적화한다.
- import하여 React 컴포넌트에서 사용할 수 있다.

    ```javascript
    import logo from "../assets/logo.png";
    
    const App = () => {
    return <img src={logo} alt="Logo" />;
    };
    ```

  * React 컴포넌트와 함께 동적으로 로드되는 파일
    - 프로젝트의 이미지, JSON 파일, 기타 리소스
  * 빌드 시 최적화가 필요한 경우
    - Webpack이 파일을 처리해 최적화하고, 필요에 따라 해시를 추가해 캐싱을 효율화

</br>

### 3. 사용해야 하는 경우의 기준
  * public 폴더
    - 정적 파일이고, React 컴포넌트에서 참조할 필요가 없거나 HTML에서 직접 참조해야 할 때
    - 예: favicon, 로고, 외부 JS/CSS 파일
  * src/assets 폴더
    - React 컴포넌트와 함께 로드되고, 빌드 시 최적화가 필요한 리소스
    - 예: 이미지, SVG 파일, JSON 데이터


</br>

### 차이점 정리

| **특성**              | **`public` 폴더**                            | **`src/assets` 폴더**                           |
| --------------------- | -------------------------------------------- | ----------------------------------------------- |
| **접근 방식**         | URL 또는 절대 경로 사용 (`/assets/logo.png`) | `import`를 통해 접근 (`import logo from ...`)   |
| **빌드 시 처리 여부** | 처리하지 않고 그대로 복사                    | Webpack/Vite에 의해 최적화 및 처리              |
| **주 용도**           | 고정된 정적 파일 (favicon, robots.txt 등)    | 컴포넌트와 함께 사용하는 리소스                 |
| **파일 경로 변경**    | 경로는 그대로 유지                           | 빌드 시 경로가 변경될 수 있음                   |
| **캐싱 관리**         | 브라우저 캐싱에 의존                         | Webpack이 파일 이름에 해시를 추가해 캐싱 최적화 |

---
