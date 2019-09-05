from collections import Counter

class VendingMachine():
    def __init__(self):
        self.money = []
        self.personal_array = []
        self.goods = ["化粧水","日焼け止め","口紅"]

    def write_購入履歴(self, goods):
        with open("購入履歴.txt", "a") as f:
            f.write("{}\n".format(goods))

    def read_購入履歴(self):
        with open("購入履歴.txt", "r") as f:
            return f.read().split("\n")[:-1]

    def return_best3(self):
        purchase_hist = self.read_購入履歴()
        counter = Counter(purchase_hist[-10:])
        return sorted(counter.items(), key=lambda x: x[1], reverse=True)

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

    if vending_machine.money_sum() == 0:
        print("===================")
        print("全商品100円でございます！！")
        for ind, goods in enumerate(vending_machine.goods, start=1):  # 商品を表示
            print("{}: {}".format(ind, goods))
        print("===================")

    i = input("お金を入れてください: ")
    vending_machine.enter(int(i))

    while(True):
        if i == "売り上げ":
            print("=========")
            print(vending_machine.total())
            print("=========")
            continue
        elif i == "rank":
            print("=========")
            print("直近10個の購入ランキング!!")
            for rank, goods in enumerate(vending_machine.return_best3(), start=1):
                print("{}位: {} {}個".format(rank, goods[0], goods[1]))
            print("=========")
            continue
        
        print(vending_machine.personal_array)

        if vending_machine.money_sum() >= 100:
            is_percase = input("購入しますか[y/n]: ")
            if is_percase == "y":
                num = int(input("商品番号を入力してください: "))
                vending_machine.write_購入履歴(vending_machine.goods[num - 1])
                vending_machine.money.append(100)
                print("商品:{}".format(vending_machine.goods[num - 1]))
                おつり = vending_machine.money_sum() - 100
                is_continue = input("続けて購入しますか[y/n]: ")
                if is_continue == "y":
                    if vending_machine.money_sum() <= 100:
                        print("お金が足りません")
                        i = input("お金を入れてください: ")
                        vending_machine.enter(i)
                    else:
                        vending_machine.personal_array = [おつり]
                else:
                    print("お釣り: {}円".format(おつり))
                    vending_machine.clear()
                    i = input("お金を入れてください: ")
                    vending_machine.enter(i)
            else:
                print("返金致します")
                vending_machine.clear()
                i = input("お金を入れてください: ")
                vending_machine.enter(i)
        else:
            is_back = input("返金しますか[y/n]")
            if is_back == "y":
                print("返金致します")
                vending_machine.clear()
            else:
                print("お金が足りません")
                i = input("お金を入れてください: ")
                vending_machine.enter(i)
