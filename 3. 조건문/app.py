재고량 = 10

if 재고량 > 0:
    print("지금 주문 가능합니다.")
else:
    print("주문할 수 없습니다.")

print()

중고차재고 = ["K5", "BMW", "Tico"]

if "K5" in 중고차재고 and "BMW" in 중고차재고 and "Tico" in 중고차재고:
    print("K5, BMW, Tico가 재고에 있습니다.")
elif not ("K5" in 중고차재고) and "BMW" in 중고차재고 and "Tico" in 중고차재고:
    print("BMW, Tico가 재고에 있습니다.")
elif "K5" in 중고차재고 and not ("BMW" in 중고차재고) and "Tico" in 중고차재고:
    print("K5, Tico가 재고에 있습니다.")
elif "K5" in 중고차재고 and "BMW" in 중고차재고 and not ("Tico" in 중고차재고):
    print("K5, BMW가 재고에 있습니다.")
elif "K5" in 중고차재고 and not ("BMW" in 중고차재고) and not ("Tico" in 중고차재고):
    print("K5가 재고에 있습니다.")
elif not ("K5" in 중고차재고) and "BMW" in 중고차재고 and not ("Tico" in 중고차재고):
    print("BMW가 재고에 있습니다.")
elif not ("K5" in 중고차재고) and not ("BMW" in 중고차재고) and "Tico" in 중고차재고:
    print("Tico가 재고에 있습니다.")
else:
    print("재고가 없습니다.")
