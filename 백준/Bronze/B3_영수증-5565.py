total_price = int(input())
except_price = 0

for _ in range(9):
    except_price += int(input())

print(total_price - except_price)
