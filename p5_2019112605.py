def calculate_standard_weight(height):
    return(height - 100) * 0.9

def calculate_weight_diff(current_weight, standard_weight):
    return current_weight - standard_weight

def calculate_obesity_rate(current_weight, standard_weight):
    return (current_weight / standard_weight) * 100

def get_obesity_result(obesity_rate):
    if obesity_rate < 100:
        return "저체중"
    elif obesity_rate <= 110:
        return "정상체중"
    elif obesity_rate <= 120:
        return "과체중"
    else:
        return "비만"

print("===표준체중 계산기===")

name = input("이름: ")
height = float(input("키(cm): "))
current_weight = float(input("현재몸무게(kg): "))

standard_weight = calculate_standard_weight(height)
weight_diff = calculate_weight_diff(current_weight, standard_weight)
obesity_rate = calculate_obesity_rate(current_weight, standard_weight)

print("\n===체중 계산 결과===")
print(f"이름: {name}")
print(f"표준 체중: {standard_weight:.1f}kg")
print(f"체중차이: {'+'if weight_diff > 0 else ''}{weight_diff:.1f}kg")
print(f"비만도: {obesity_rate:.1f}%")
print(f"판정: {get_obesity_result(obesity_rate)}")
