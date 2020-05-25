# Introduction
* Todo List 추가, 목록 조회, 삭제 등
* Django의 templates를 사용하여 화면도 함께 구현

<br>

# Technologies
* Python 3.8
* Django

<br>

# Demo
[![demo_video](https://user-images.githubusercontent.com/53142539/82811651-39e44680-9ecc-11ea-910f-8debb76291d6.png)](https://drive.google.com/file/d/1YfE2gK-MGhvNC6pKc7gBlZhmW-00YtQa/view)

<br>

# DB Modeling
![db_modeling](https://user-images.githubusercontent.com/53142539/82811137-0523bf80-9ecb-11ea-8a90-476f48267ea3.png)

<br>

# API Features

### TodoList

- 먼저 등록한 순서대로 보이도록 정렬
- active, done 을 query parameter로 받아서 filtering (특정하지 않으면 전체 list 보여주기)

### TodoCreate

- 할 일 추가
- 이미지 등록 가능
- 제목을 넣지 않고 저장하는 경우, default 값으로 저장

### TodoDelete

- 할 일 삭제

### TodoStatus

- 할 일의 is_active field가 true일 경우는 false로, false일 경우는 true로 변경

<br>

# Templates

### 기본 화면

- 제목 (My Reminder)
- All, Active, Done 3가지 navigation bar
- 할 일 목록 (완료 여부 버튼, 삭제 버튼)
- 이미지 사이즈 조절
- 할 일 추가 버튼 (details tag로 구현)

### 할 일 등록

- 제목 입력 (입력하지 않아도 default 값으로 저장됨)
- Attach image 버튼을 눌러 이미지 첨부 (첨부하지 않아도 저장됨)
- 저장 버튼을 클릭하여 저장
- 저장 완료되면 다시 기본 화면으로 redirect

### 할 일 삭제

- 삭제 버튼을 누르면 삭제 후 기본 화면으로 redirect

### 할 일 완료

- 완료 버튼을 눌렀을 때 ⇒ 체크 표시, 제목 strike
