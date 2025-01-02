# 커피머신  


# 남은 재료 프린트
# 재료가 충분한 지 확인
# 코인 처리
# 코인 충분한지 확인 
# 커피 만들기(자원 차감감)

# TODO : 1. 남은 재료 보여주기
# TODO : 2. 재료 충분한 지 확인인
MENU = {
    "espresso" : {
        "ingredients" : {
            "milk" : 0,
            "water" : 50, 
            "coffee" : 18
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200, 
            "milk"  : 150,
            "coffee" : 24, 
        },
        "cost" : 2.5 
    },
    "cappuccino" : {
        "ingredients" : {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost" : 3.0
    },


}
resource = {
    "water" : 300,
    "milk": 200,
    "coffee": 100,
    "profit" : 0
}


def is_resourse_sufficient(order) :
    a = True
    
    if order["ingredients"]["water"] > resource["water"] :
        print("물 부족")
        a = False
    if order["ingredients"]["milk"] > resource["milk"] :
        print("우유 부족")
        a = False
    if order["ingredients"]["coffee"] > resource["coffee"] :
        print("커피 부족")
        a = False
    return a

    
    
    


is_on = True
while is_on : 
    answer = input(("What would you like? (espresso/latte/cappuccino) : "))
    if answer == "off" :
        is_on = False
    elif answer == "report" :
        print(f"water: {resource['water']}ml")
        print(f"milk: {resource['milk']}ml")
        print(f"coffee : {resource['coffee']}g"),
        print(f"moeny: ${resource['profit']}")
    else : 
        drink = MENU[answer]
        if is_resourse_sufficient(drink) : 
            n1 = int(input("페니 : ")) 
            n2 = int(input("니크 : ")) 
            n3 = int(input("딤 : ")) 
            n4 = int(input("쿼터 : "))
            total = n1 * 0.01 + n2 * 0.05 + n3 * 0.1 + n4 * 0.25
            if drink["cost"] > total : 
                print("넣은 동전이 충분하지않음. 돈 환불")
            else : 
                resource["profit"] += drink["cost"]
                resource["water"] -= drink["ingredients"]["water"]
                resource["milk"] -= drink["ingredients"]["milk"]
                resource["coffee"] -= drink["ingredients"]["coffee"]
                print(f"water: {resource['water']}ml")
                print(f"milk: {resource['milk']}ml")
                print(f"coffee : {resource['coffee']}g"),
                print(f"moeny: ${resource['profit']}")
                if total > drink["cost"]  :
                    print(f"잔돈 {round(total-drink['cost'],2)}이 반환됨 ")
                    print(f"{answer} 맛있게 드세요")
                else : 
                    print(f"{answer} 맛있게 드세요")
                
         
             


    