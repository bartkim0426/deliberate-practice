def calculator(numbers: int, price: int, original_delivery_fee: int=2500, discount: int=5000) -> int:
    '''get final price per one can after discount'''
    original_price = numbers * price
    return (original_price - discount + original_delivery_fee) // numbers


class Calculator:
    def __init__(self, number: int, price: int, original_delivery_fee: int, discount: int, addtional_discount: int):
        self.number = number
        self.price = price
        self.original_delivery_fee = original_delivery_fee
        self.discount = discount
        # 추가적인 할인이 있는 경우
        self.addtional_discount = addtional_discount

    @property
    def delivery_fee(self):
        return self.original_delivery_fee

    @property
    def original_price(self):
        return self.number * self.price

    @property
    def final_price(self):
        return self.original_price - self.discount + self.delivery_fee - self.addtional_discount

    @property
    def price_per_unit(self):
        return self.final_price // self.number


class PetFriend(Calculator):
    def __init__(self, number: int, price: int, is_parcel: bool=False):
        original_delivery_fee = 2500
        discount = 5000
        addtional_discount = 0
        if is_parcel:
            addtional_discount = 1000
        super().__init__(number=number, price=price, original_delivery_fee=original_delivery_fee, discount=discount, addtional_discount=addtional_discount)

    @property
    def delivery_fee(self):
        if self.original_price >= 20000:
            return 0
        else: return self.original_delivery_fee


if __name__ == '__main__':
    print('몇개 구매할건지?')
    number = int(input())
    print('얼마짜리 구매할건지?')
    price = int(input())
    print('택배로 구매할건지? (1000원 할인)')
    is_parcel = bool(input())
    pf = PetFriend(number, price, is_parcel)
    print(f'최종 개당 가격: {pf.price_per_unit} (총 {pf.final_price}, {pf.number}개)')
