class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        print("Owner =", self.owner)
        print("Balance =", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited: " + str(amount))
        else:
            print("돈을 입금해주세요")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: " + str(amount))
        else:
            print("출금할 수 없습니다.")

# 사용 예시
ABC = Bank("주인", 0)

while True:
    ABC.display_balance()  # 현재 잔액 확인
    action = input("입금하려면 'a'를, 출금하려면 'b'를 입력하세요 (종료하려면 'c'): ").lower()

    if action == 'a':  # 입금 선택
        try:
            deposit_amount = int(input("돈을 입금해주세요: "))
            ABC.deposit(deposit_amount)
        except ValueError:
            print("숫자를 입력해주세요.")

    elif action == 'b':  # 출금 선택
        try:
            withdraw_amount = int(input("돈을 출금해주세요: "))
            ABC.withdraw(withdraw_amount)
        except ValueError:
            print("숫자를 입력해주세요.")

    elif action == 'c':
        print("프로그램을 종료.")
        break

    else:
        print("잘못된 입력입니다. 'a', 'b', 또는 'c'를 입력해주세요.")

