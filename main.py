class VendingMachine():
    def __init__(self):
        self.money = []
        self.personal_array = []
        self.goods = ["化粧水","日焼け止め","口紅"]


    def enter(self, i):
        if i == 10 or i == 50 or i == 100 or i == 500 or i == 1000:
            self.personal_array.append(i)
            return "現在{}円が入っています".format(self.money_sum())
        else:
            return "他のお金を入れてください"


    def total(self):
        return sum(self.money)


    def money_sum(self):
        return sum(self.personal_array)


    def clear(self):
        self.personal_array = []


if __name__ == "__main__":
    vending_machine = VendingMachine()

    while(True):
        if vending_machine.money_sum() == 0:
            print("===================")
            for ind, goods in enumerate(vending_machine.goods, start=1):  # 商品を表示
                print("{}: {}".format(ind, goods))
            print("===================")

        i = input("お金を入れてください: ")

        if i == "売り上げ":
            print("=========")
            print(vending_machine.total())
            print("=========")
            continue

        print(vending_machine.enter(int(i)))
        if(vending_machine.money_sum() >= 100):
            select = input("購入しますか[y/n]")
            if select == "y":
                num = int(input("商品番号を入力してください: "))
                おつり = vending_machine.money_sum() - 100
                vending_machine.money.append(100)
                print("商品:{}".format(vending_machine.goods[num - 1]))
                # is_continue = input("続けて購入しますか[y/n]")
                # if is_continue == "y":
                #     continue
                print("お釣り: {}円".format(おつり))
                vending_machine.clear()
            elif select == "n":
                print("返金致します")
        else:
            print("お金が足りません")
