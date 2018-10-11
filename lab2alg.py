def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        current = list_to_sort[i]
        position = i
        while position > 0 and current > list_to_sort[position - 1]:
            list_to_sort[position] = list_to_sort[position - 1]
            position -= 1
        list_to_sort[position] = current


if __name__ == "__main__":
    file = open('discnt_in.txt')
    lines = [line.rstrip('\n') for line in file]
    list_sale = []
    for sale in lines[0].split(" "):
        list_sale.append(int(sale))
    discount_percent = int(lines[1])

    insertion_sort(list_sale)

    third = int(len(list_sale) / 3)
    final_sale = 0
    for pos in range(0, len(list_sale)):
        if pos < third:
            discount = (100 - discount_percent) / 100
            final_sale += (list_sale[pos] * discount)
        else:
            final_sale += list_sale[pos]

    print("FINAL SALE: %.2f" % final_sale)

    f = open("discnt_out.txt", "w")
    f.write("Final sale: %.2f" % final_sale)