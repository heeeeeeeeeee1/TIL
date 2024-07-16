
# Type Conversion 형변환
* 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정
* 암시적 형변환 / 명시적 형변환으로 나뉨

## 암시적 형변환(Implict Type conversion)
* 파이썬이 자동으로 수행하는 형변환
* 논리적 표현 필요한 곳
* 값만 있을때 bool 판단 필요할때 
* 예시
    - 정수와 실수의 연산에서 정수가 실수로 변환됨
    - Boolean과 Numeric Type에서만 가능

        ```python
        print(3 + 5.0)  # 8.0

        print(True + 3)  # 4

        print(True + False)  # 1
        ```

<br/>

## 명시적 형변환(Explicit Type conversion)
* 프로그래머가 직접 지정하는 형변환
* 암시적 형변환이 아닌 경우를 모두 포함
    - str -> integer : 형식에 맞는 숫자만 가능
    ```python
    print(int('1'))  # 1

    # ValueError: invalid literal for int() with base 10: '3.5' 에러남
    print(int('2.5')) 

    print(int(2.5))  # 2
    print(float('3.5'))  # 3.5
    ```

    - integer -> str : 모두 가능
    
    ```python
    print(str(1) + '층')  # 1층 
    ```



