import random

money = 10000
while money > 0:
    bet = int(input("少侠请下注: "))
    if bet > money:
        print("超出了你的身家，请重新投注。")
        continue
    dealer = random.randint(1, 6)
    player = random.randint(1, 6)
    # print("你摇出了" + str(player) + "点,庄家摇出了" + str(dealer) + "点")
    # print("你摇出了%d点,庄家摇出了%d点" % (player, dealer))
    print(f"你摇出了{player}点,庄家摇出了{dealer}点")
    if dealer > player:
        # money = money - bet
        money -= bet
        print("少侠,你输了，身家还剩" + str(money))
    elif dealer < player:
        # money = money + bet
        money += bet
        print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩" + str(money))
    else:
        print("打平了，少侠，在来一局？")
else:
    print("哈哈哈，少侠你已经破产，无资格进行游戏")
