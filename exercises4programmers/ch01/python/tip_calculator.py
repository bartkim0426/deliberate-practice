'''
tip calculator

- [o] input: 
    tip percentage: int
    price: int
- [o] output: rounding in cents

+ [ ] 가격과 팁 비율 값으로 숫자만 받게
+ [ ] 잘못 입력된 값에 대해 메세지 출력하고 프로그램을 종료하는 대신 허용되는 값이 입력될 때까지 계속 입력요청
+ [ ] 음수 값이 입력되지 않도록
+ [ ] 연산 부분을 함수로 처리하도록 분할
+ [ ] GUI 버전으로 개선. 입력 값이 바뀌면 결과값이 자동으로 반영
+ [ ] 팁 비율을 퍼센트 단위로 입력받는 대신 슬라이더를 사용하여 조절할 수 있도록 수정. 슬라이더의 범위는 5~20%

pseudocode

TipCalculator
    Initialize bill to 0
    Initialize tip to 0
    Initialize tip_rate to 0
    Initialize total to 0

    Prompt for bill with "What is the bill amount?"
    Prompt for tip_rate with "What is the tip rate?"

    convert bill to a number
    convert tip to a number

    tip = bill * (tip_rate / 100)
    round tip up to cent

    total = bill + tip

    Display "Tip: $" + tip
    Display "Total: $" + total
End
'''


def calculate_tip() -> tuple:
    '''
    enter bill and tip_rate from prompt, print tip and total amount
    '''
    bill: str = input('What is the bill amount?')
    tip_rate: str = input('What is the tip rate?')

    bill, tip_rate = float(bill), float(tip_rate)

    tip = bill * (tip_rate / 100)

    tip = round(tip, ndigits=2)

    total = tip + bill

    print("Tip: $" + str(tip))
    print("Total: $" + str(total))
    
    return tip, total
