# Exercises 4 programmers

Training from the book: [Exercises 4 programmer](http://ebook.insightbook.co.kr/book/45)

# Python

## ch01.

### Tip calculator

- [x] input: 
    tip percentage: int
    price: int
- [x] output: rounding in cents

Challenge
+ [x] 가격과 팁 비율 값으로 숫자만 받게
+ [x] 잘못 입력된 값에 대해 메세지 출력하고 프로그램을 종료하는 대신 허용되는 값이 입력될 때까지 계속 입력요청
+ [x] 음수 값이 입력되지 않도록
+ [x] 연산 부분을 함수로 처리하도록 분할
+ [ ] GUI 버전으로 개선. 입력 값이 바뀌면 결과값이 자동으로 반영
+ [ ] 팁 비율을 퍼센트 단위로 입력받는 대신 슬라이더를 사용하여 조절할 수 있도록 수정. 슬라이더의 범위는 5~20%

## ch02. 입력, 프로세싱, 출력

### 2.1. 인사하기

Basic
- [x] 입력, string concatenation, 출력 부분 별도로 작성

challenge
- [x] 변수를 사용하지 않는 새로운 버전
- [ ] 사람들마다 서로 다른 인사말이 나타나도록 (4, 7장 이후 도전)

### 2.2. 글자 수 세기

```
What is the input string? Homer
Homer has 5 characters.
```

- [x] 출력 결과에는 입력 받은 문자열이 그대로 나타나도록 할 것 
- [x] 출력을 위해 하나의 출력문을 사용할 것 
- [x] 문자열의 길이를 구하기 위해 프로그래밍 언어에서 제공하는 내장 함수를 사용할 것

도전 과제

- [x] 사용자가 아무 것도 입력하지 않은 채로 엔터 키를 치면 무엇이라도 입력하라는 메시지를 나타내보자. 
- [ ] 이 프로그램을 GUI (그래픽 사용자 인터페이스) 버전으로 작성하여 글자를 입력할 때마다 글자 수가 바로 바로 업데이트되도록 하라. 만 일 여러분이 사용하는 언어에 GUI 라이브러리가 없다면 HTML 과 JavaScript 를 사용하라.

### 2.3. 따옴표 출력

```
What is the quote? These aren't the droids you're looking for
Who said it? Obi-Wan Kenobi
Obi-Wan Kenobi says, "These aren't the droids you're looking for."
```

- [x] 한개의 출력문만 사용
- [x] 문자열 보간(string interpolation)이나 대체(string substitution)를 사용하지 말고 문자열 연결(string concatenation)을 사용

도전 과제

- [x] 7 장에서 데이터 리스트에 대해서도 연습하게 될 것이다. 앞의 프로 그램을 수정하여 사용자로부터 입력을 받는 대신 인용구와 이와 관 련된 내용(사람 이름)을 담는 자료 구조를 만들어 모든 내용을 앞 의 출력 예와 같이 나타내보자. 맵 형태의 배열을 사용하면 좋을 것 이다.


### 2.4. Mad Libs

```
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly
Do you walk your blue dog quickly? That's hilarious!
```

- [x] 한개의 출력문만 사용
- [x] 문자열 보간이나 대체를 지원하면 이를 활용

도전과제
- [ ] 입력할 수 있는 단어를 늘려 확장
- [ ] 대답에 따라 이야기가 만들어지는 브랜칭 스토리( Branching story )를 구현해보자. 브랜칭 스토리 개념은 4 장 ‘의사 결정’에서 확인할 수 있다.


### 2.5. 간단한 수학

```
What is the first number? 10
What is the second number? 5
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

- [x] 문자열로 입력받기
- [x] 입력, 출력 모두 숫자 변환 및 기타 프로세스에 영향을 받지 않게 (?)
- [x] 한개의 출력문만 사용

도전과제

- [x] 숫자만 입력되도록 수정
- [x] 음수를 넣을 수 없게
- [x] 계산 부분을 함수로 구현
- [ ] GUI로 구현 (숫자를 넣는 즉시 결과 업데이트)


### 2.6. 퇴직 계산기

```
What is your current age? 25
At what age would you like to retire? 65
You have 40 years left until you can retire.
It's 2015, so you can retire in 2055.
```

- [x] 입력 값을 숫자로 변환
- [x] 올해 년도를 프로그램에 넣지 말고 프로그래밍 언어를 통해 구하기

도전과제

- [x] 이미 퇴직했을 나이를 입력하면 음수값이 출력되는 상황을 해결

## ch03. 입력, 프로세싱, 출력
