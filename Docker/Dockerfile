# FROM baseImage(어떤 베이스 이미지 사용할 것인지 명시)
# node는 미리 만들어 놓은 이미지가 있음
# 16: 버전, alpine: 정말 작은 단위의 리눅스 버전
FROM node:16-alpine

# 도커 이미지 안에서, 컨테이너 안에서 어떤 경로에 실행시킬 것인지 명시
WORKDIR /app
# unix 명령어에서 cd와 같은 개념

# 레이어 시스템(명령어 하나하나가 레이어) : 빈번히 변경되는 파일일수록 마지막에 작성하는 것이 좋음
# 소스파일(Layer0~4중에서 3, 4)이 변경되어 이미지를 새로 만들어야 될 떄 변경된 최상단의 레이어만 업데이트
# 변경되지 않은 나머지 레이어는 재사용 -> 이미지 만드는 시간 단축

# 소스코드 담고 있는 index.js보다 디펜던시 담고있는 package.json가 덜 변경됨 
# 현재 경로인 app으로 복사
COPY package.json package-lock.json ./ 

# RUN npm install 대신 ci 사용하는 것이 좋다.
# install은 package.json에 있는 라이브러리에 버전3이상은 괜찮다고 명시 되어있을 경우 설치 시점에서의 최신 버전(ex.버전5)이 설치 될 수 있다.
# 버전 불일치 문제 발생

# ci는 package-lock.json에 명시되어있는 정확한 버전을 사용하기 때문에 위와 같은 버전 문제 발생하지 않음
RUN npm ci

COPY index.js .

# 실행해
ENTRYPOINT [ "node", "index.js" ]