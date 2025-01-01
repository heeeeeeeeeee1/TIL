// express 모듈 불러오기(Express는 Node.js를 위한 웹 애플리케이션 프레임워크)
const express = require('express')

// Express 애플리케이션 생성
// app 객체를 통해 라우팅 및 서버 설정을 구성
const app = express()

// HTTP GET 요청이 '/' 경로로 들어왔을 때 실행될 핸들러 정의
// req: 요청(request) 객체, res: 응답(response) 객체
app.get('/', (req, res) => {
  // 클라이언트에게 'Docker example'이라는 문자열을 응답으로 보내기
  res.send('Docker example')
})

// 서버를 8080번 포트에서 실행
// 서버가 시작되면 '서버 정상 작동' 메시지가 콘솔에 출력
app.listen(8080, () => console.log('서버 정상 작동'))

