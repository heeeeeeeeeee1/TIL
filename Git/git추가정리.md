# git 추가 정리



## gitignore

* Git에서 특정 파일이나 디렉토리를 **추적하지 않도록** 설정하는데 사용되는 텍스트 파일
* a.k.a 블랙리스트. 보안이 필요한 파일
* 프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문

* .gitignore 생성 시점 : init 직후 생성 추천
    - commit 한번이라도 이루어지면 추적대상 등록
* .gitignore : 추적대상이 아닌 파일들을 대상으로 동작함

* [gitignore.io](https://www.toptal.com/developers/gitignore)
    - 사용 언어, 개발 환경에 따라 제외해야할 파일들을 자동 생성해주는 사이트
    - 전체 선택(ctrl + A) 후 복사 => .gitignore 파일에 붙여넣기 => 저장



----


* git remote -v : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
* git remote rm 원격_저장소_이름 : 현재 로컬 저장소에 등록된 원격  저장소 삭제


* git revert : 특정 commit을 없었던 일로 만드는 작업
    이전에 있던 commit을 취소시키고 해당 commit 취소함이라고 하면서 새로운 commit
    