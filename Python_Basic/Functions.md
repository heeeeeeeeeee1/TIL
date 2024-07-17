# 함수
* 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
* 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
* 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상

* 함수 정의
   - 함수 정의는 `def` 키워드로 시작
   - def 키워드 이후 함수 이름 작성
   - 괄호안에 매개변수를 정의할 수 있음
   - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

* 함수 body
    - 콜론(`:`) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행 될 때 수행되는 코드를 정의
    - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

* 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - `return` 키워드 이후에 반환할 값을 명시
    - `return` 문은 함수의 **실행을 종료**하고, 결과를 호출 부분으로 반환

* 함수 호출
    - 함수를 사용하기 위해서는 호출이 필요
    - 함수의 이름과 소괄호를 활용해 호출
    - 필요한 경우 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨

### 함수 호출(function call)
> function_name(arguments)
   - 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것


```python
# 함수 정의
def greet(name): 
    """입력된 이름(name) 값에
    인사를 하는 메세지('Hello, ')를 만드는 함수
    """ # docstring 
      
    message = 'Hello, ' + name
    return message # 함수 반환 값

# 함수 호출
result = greet('Alice')
print(result)
```

* 추가 예시
    - print는 return이 없다. return과 출력은 다름.
        ```python
        def make_sum(pram1, pram2):
            """이것은 두 수를 받아
            두 수의 합을 반환하는 함수입니다.
            >>> make_sum(1, 2)
            3
            """
            return pram1 + pram2

        result = make_sum(100, 30)
        return_value = print(result) # 130
        print(return_value) # None

        ```
        ```python
        def my_func():
            print('hi') # hi

        result = my_func()
        print(result) # None
        ```

<br/>

---

<br/>

# 매개변수와 인자
## 매개변수(parameter)
* 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

## 인자(argument)
* 함수를 호출할 때, 실제로 전달되는 값

```python
def add_numbers(x, y): # x, y : 매개변수
	result = x + y
	return result


a = 2
b = 3
sum_result = add_numbers(a, b) # a, b : 인자
print(sum_result)
```

### 다양한 인자 종류
1. 위치 인자
2. 기본 인자 값
3. 키워드 인자
4. 임의의 인자 목록
5. 임의의 키워드 인자 목록


## 위치인자 Positional Arguments
* 함수 호출 시 인자의 위치에 따라 전달되는 인자
* 함수 호출 시 매개변수와 인자의 위치에 따라 인자 값이 매개변수에 할당됨
* `위치인자는 함수 호출 시 반드시 값을 전달해야 함`

```python
def greet(name, age): # 매개변수
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Zoe', 22) # 안녕하세요, Zoe님! 22살이시군요.
greet('Zoe') # TypeError: greet() missing 1 required positional argument: 'age'
greet(20, 'Zoe') # 안녕하세요, 20님! Zoe살이시군요.
```

<br/>

## 기본 인자 값 Default Argument Values
* 함수 정의에서 매개변수에 기본 값을 할당하는 것
* 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
* 만약 해당위치에 인자가 전달되지 않으면 기본값을 사용하겠다.

```python
def greet(name, age=60): # 매개변수
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Harry') # 안녕하세요, Harry님! 60살이시군요.
greet('Judy', 40) # 안녕하세요, Judy님! 40살이시군요.
```

<br/>

## 키워드 인자 Keyword Arguments
- 함수 호출 시 ~~인자의 이름~~ 함께 값(매개변수명과 인자값)을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
- `단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함`
- 매개변수의 순서가 기억나지 않을 때

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='Dave') # 순서 바뀌어도 출력됨
greet(age=35, 'Dave') # SyntaxError: positional argument follows keyword argument
```
<br/>

## 임의의 인자 목록 Arbitrary Argument Lists
* 정해지지 않은 개수의 인자를 처리하는 인자
* 함수 정의 시 매개변수 앞에 `‘*’`를 붙여 사용하며, 여러 개의 인자를 tuple로 처리

    ```python
    def calculate_sum(*args):
        print(args) # (1, 2, 3)
        total = sum(args)
        print(f'합계: {total}') # 합계: 6

    calculate_sum(1, 2, 3)
    ```
<br/>

## 임의의 키워드 인자 목록 Arbitrary Keyword Argument Lists
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 `‘**’`를 붙여 사용하며, <br>여러 개의 인자를 dictionary로 묶어 처리

    ```python
    def print_info(**kwargs):
        print(kwargs)


    print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
    ```

<br/>

## 함수 인자 권장 작성순서
- `위치 -> 기본 -> 가변 -> 가변 키워드`
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- `단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음`
    - 인자의 모든 종류를 적용한 예시
    ```python
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
        print('pos1:', pos1)
        print('pos2:', pos2)
        print('default_arg:', default_arg)
        print('args:', args)
        print('kwargs:', kwargs)

    func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
    """
    pos1: 1
    pos2: 2
    default_arg: 3 
    args: (4, 5, 6)
    kwargs: {'key1': 'value1', 'key2': 'value2'}
    """
    ```
    ```python
    # 기본값으로 정한 'default'를 보고 싶으면 위에서 정의한 함수에서
    func(1, 2, key1='value1', key2='value2') # 이렇게 호출해야함
    """
    pos1: 1
    pos2: 2
    default_arg: 3
    args: ()
    kwargs: {'key1': 'value1', 'key2': 'value2'}
    """

<br/>

---

<br/>

# 재귀함수
* 함수 내부에서 자기 자신을 호출하는 함수

<br/>

---

<br/>

# 내장 함수 Built-in function
* 파이썬이 기본적으로 제공하는 함수(별도 inport없이 사용가능)

"""

"""



## map(function, iterable)
* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

```python
map(function, iterable)
```