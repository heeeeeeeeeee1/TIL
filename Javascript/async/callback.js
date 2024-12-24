// 1. 동기오 ㅏ비동기

// 자바스크립트는 동기적(synchronous)이다.
// 호이스팅된 이후부터 우리가 작성한 코드 순서에 맞춰서 하나씩 싱행됨
// 호이스팅 : var 또는 함수 선언들이 자동적으로 제일 위로 올라가는것?
console.log("1");
// setTimeout : 브라우저 제공 api. 지정한 시간 지나면 함수 호출
setTimeout(() => console.log("2"), 1000);
console.log("3");

// 동기적 콜백
function printImmediately(print) {
  print();
}
printImmediately(() => console.log("hello"));


// 비동기적 콜백
function printWithDelay(print, timeout) {
  setTimeout(print, timeout);
}
printWithDelay(() => console.log("aysnc callback"), 2000);


// 콜백 지옥 예시
// 백엔드에서 사용자 정보 가져왔다고 가정
class UserStorage {
  loginUser(id, password, onSuccess, onError) {
    // id, password 정보 일치하면 onSuccess호출, 불일치하면 onError호출
    setTimeout(() => {
      if (
        (id === "baki" && password === "dream") ||
        (id === "coder" && password === "academy")
      ) {
        onSuccess(id);
      } else {
        onError(new Error("not found"));
      }
    }, 2000);
  }

  getRoles(user, onSuccess, onError) {
    setTimeout(() => {
      // baki라면 name, role 객체 전달
      if (user === "baki") {
        onSuccess({ name: "baki", role: "admin" });
      } else {
        onError(new Error("no access"));
      }
    }, 1000);
  }
}

const userStorage = new UserStorage();
const id = prompt("enter your id");
const password = prompt("enter your password");

userStorage.loginUser(
  id,
  password,
  user => {
    userStorage.getRoles(
      user,
      userWithRole => {
        alert(`Hello ${userWithRole.name}, you have a ${userWithRole.role} role`)
      },      
      error => {console.log(error)}
    )
  },
  error => {console.log(error)}
)
