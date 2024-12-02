from character import Hero, Monster
from battle import Battle
import pygame

def main():
    pygame.init()

    # 화면 크기 설정
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RPG Battle")

    font = pygame.font.SysFont("Arial", 24)

    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 선택하세요(전사/마법사/궁수): ")
    hero = Hero(name, hp=100, attack=20, defense=5, role=role)
    print(f"{hero.name}({hero.role})이(가) 생성되었습니다!")

    monster = Monster(name="Goblin", hp=50, attack=10, defense=2)
    print(f"\n몬스터 {monster.name}이(가) 등장했습니다!")

    battle = Battle(screen, font, hero, monster, WIDTH, HEIGHT)
    battle.fight()

    pygame.quit()

if __name__ == "__main__":
    main()
