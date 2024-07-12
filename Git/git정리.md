# 정리

## Git
> Git이란
> 분산 버전 관리 시스템

* Git은 3개의 영역이 존재
1. Working Directory
    * 현재 수정, 생성, 삭제된 파일들이 위치한 영역
    * `git status` 붉은 색으로 파일 명 표시
        * Untracked : 새로 생성된 파일을 의미
        * Modified :수정된 파일을 의미
        * Deleted : 삭제된 파일을 의미
    * 해당 영역에 있는 파일은 commit에 기록되지 않음(Staging 
    Area로 이동시켜야함)

2. Staging Area
    * 분류소(버전 관리할 파일)
    * 버전 관리할 파일들을 모아두는 임시 영역
    * `git status`로 확인을 종종 할 필요가 있음
    * New file : 생성된 파일
    * Modified : 수정된 파일

3. Repository
    * 실제 버전 관리 내용이 저장되는 영역
    * `git log` 이용 하여 commit 이력을 확인할 수 있음

*`git add 파일명`
    * Workind Directory => Staging Area로 파일을 이동시키는 명령어
    * `git add .` : 현재 폴더의 모든 하일과 폴더를 Staging Area로 이동시킬 수 있음
        * 주의 : 버전 관리가 필요없는 파일이나 폴더가 같이 올라갈 가능성이 있어 반드시 Staging Area를 확인해야함

* `git commit`
    * 커밋 이력을 남기는 명령어
    * `-m '메세지'` : 해당 옵션으로 간단한 커밋 메세지를 남길 수 있음


> (참고) Vim 에디터 간단 사용법

* Vim은 두가지 모드가 있음
    * Command 모드 : 저장, 나가기
    * Editor 모드 : 텍스트 수정

* Editor 모드로 전환하는 방법은 키보드로 i 누르면 됨

* Command모드로 전환하는 방법은 ESC
* 저장하고 나가기 `:wq`
* 저장하지 않고 강제로 나가기 `:q!`