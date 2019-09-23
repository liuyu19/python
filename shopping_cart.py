product_list = [
    ("Huawei Pro30",3800),
    ("Mac pro",16000),
    ("Nike",800) ,
    ("Milk Tea",15),
    ("Head First Python",128),
    ("Carbs",88)
]
shopping_cart = []
alipay_balance = int(input("alipay_balance:"))
while True:
    for item in product_list:
        print(product_list.index(item),item)
    user_choice = input("请选择商品编号：")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice >=0 and user_choice<6:
            product_item = product_list[user_choice]
            if alipay_balance >= product_item[1]:
                shopping_cart.append(product_item)
                alipay_balance = alipay_balance - product_item[1]
                print("added %s to your shoopping cart,your current alipay balance %s" %(item[0],alipay_balance))
            else:
                print("您的余额不足")
        else:
            print("product code [%s] is not exist." % user_choice)
    elif user_choice == "q":
        print("--------shopping cart---------")
        for item2 in shopping_cart:
            print(item2)
        print("your current balance:",alipay_balance)
        break
    else:
        print("您输入的商品不存在")
