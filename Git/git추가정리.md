# git 추가 정리



## gitignore

* Git에서 특정 파일이나 디렉토리를 **추적하지 않도록** 설정하는데 사용되는 텍스트 파일
* a.k.a 블랙리스트. 보안이 필요한 파일
* 프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문

* .gitignore 생성 시점 : init 직후 생성 추천
    - commit 한번이라도 이루어지면 추적대상 등록
* .gitignore : 추적대상이 아닌 파일들을 대상으로 동작함
    - 추적하지 않을 파일 입력 후 저장 => 해당 파일이 Explorer에서 회색으로 변함

* [gitignore.io](https://www.toptal.com/developers/gitignore)
    - 사용 언어, 개발 환경에 따라 제외해야할 파일들을 자동 생성해주는 사이트
    - 전체 선택(ctrl + A) 후 복사 => .gitignore 파일에 붙여넣기 => 저장

<br/>

----

<br/>

* git remote -v : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
* git remote rm 원격_저장소_이름 : 현재 로컬 저장소에 등록된 원격  저장소 삭제
* git log : commit history 확인
    - 빠져나오기 `:q`
    - git log --oneline : 기록 한줄로(간단하게) 보기

<br/>

---

<br/>

### Git revert
* git revert : 특정 commit을 없었던 일로 만드는 작업.
    - 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업
    - 히스토리 기록 유지
    - commit 기록에서 commit을 삭제하거나 분리하는 대신 지정된 변경사항을 반전시키는 새 commit을 생성
    - git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임. 누가 뭘 취소했는지 기록됨


    - 이전에 있던 commit을 취소시키고 해당 commit 취소함이라고 하면서 새로운 commit 기록

    <br/>

    - git revert  < commit id > 
        - 단일 commit을 실행 취소. 프로젝트 기록에서 commit을 없었던 일을 처리 후 그 결과를 새로운 commit으로
    - git revert < commit id` `commit id` `commit id > 
        - 공백을 사용해 여러 커밋을 한번에 실행 취소 가능
        -  `..` 사용해 범위를 지정하여 여러 commit을 한꺼번에 실행 취소 가능
    - commit 메세지 작성을 위한 편집기를 열지 않음. 자동으로 commit 진행
        
        ```
        git revert --no--edit 7f6c24c
        ```
    - 자동으로 commit 하지 않고 Staging Area에만 올림. 이후에 직접 commit해야함. 이 옵션은 여러 commit을 revert할때 하나의 commit으로 묶는 것이 가능
        ```
        git revert --no--commit
        ```


<br/>

---

<br/>

### Git reset
- 특정 commit으로 되돌아가는 작업
-   `git reset [옵션] < commit >`

<br/>

* 작동원리
    - 되돌리기
    - 시계를 마치 과거로 돌리는 듯한 행위
    - 특정  commit으로 되돌아 갔을 때, 되돌어간 commit 이후의 commit은 모두 삭제
        - 옵션에 따라 기록 날아감

<br/>

* 옵션
    ```
    # 삭제된 commit의 기록을 staging area에 남김
    --soft

    # 삭제된 commit의 기록을 working directory에 남김(기본 옵션)
    --mixed

    # 삭제된 commit의 기록을 남기지 않음
    --hard
    ```

<br/>

---

<br/>

### 이미 삭제한 commit으로 돌아가는 방법
* git reflog
    - HEAD가 이전에 가리켰던 모든 commit을 보여줌
    - reset의 --hard 옵션을 통해 지워진 commit도 reflog로 조회하여 복구 가능

<br/>

---

<br/>

### git undoing
1. 파일 내용을 수정 전으로 되돌리기
    - git restore
        - Modified 상태의 파일 되돌리기
        - working directory에서 파일을 수정한 뒤, 파일의 수정사항을 취소하고 원래 모습대로 되돌리는 작업
        - 한번이라도 commit이 등록된 파일(관리/추적되고 있는 파일 대상)
    - git stash : 작업하던 것 잠시 어딘가에 저장
    - git stash apply : 되돌림

<br/>

2. staging area에 올라간 파일을 unstage
    - git rm --cached
        - staging area에서 working directory로 되돌리기(git 저장소에 commit이 없는 경우)
        - 추적 대상 삭제할 때도 사용
    - git restore --staged
        - SA에서 WD로 되돌리기
        - git 저장소에 commit이 존재하는 경우
