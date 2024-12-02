import pygame
class Battle:
    def __init__(self, screen, font, hero, monster, WIDTH, HEIGHT):
        self.screen = screen
        self.font = font
        self.hero = hero
        self.monster = monster
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.clock = pygame.time.Clock()
        self.attack_button = pygame.Rect(300, 500, 200, 50)
        self.battle_started = False
        self.turn = 'hero'

    def fight(self):
        battle_running = True
        while battle_running:
            self.screen.fill((255, 255, 255))


            self.display_hero_status()

            self.display_monster_status()


            pygame.draw.rect(self.screen, (0, 0, 0), self.attack_button)
            attack_text = self.font.render("Attack", True, (255, 255, 255))
            self.screen.blit(attack_text,
                             (self.attack_button.x + (self.attack_button.width - attack_text.get_width()) // 2,
                              self.attack_button.y + (self.attack_button.height - attack_text.get_height()) // 2))

            if self.battle_started and self.turn == 'hero':
                turn_text = self.font.render("Hero's Turn", True, (0, 0, 0))
                self.screen.blit(turn_text, (self.WIDTH // 2 - turn_text.get_width() // 2, 200))

            elif self.battle_started and self.turn == 'monster':
                turn_text = self.font.render("Monster's Turn", True, (0, 0, 0))
                self.screen.blit(turn_text, (self.WIDTH // 2 - turn_text.get_width() // 2, 200))

            # 이벤트 처리
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    battle_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack_button.collidepoint(event.pos):
                        if not self.battle_started:
                            self.battle_started = True
                        elif self.turn == 'hero':
                            self.hero_attack()
                            self.turn = 'monster'
                        elif self.turn == 'monster':
                            self.monster_attack()
                            self.turn = 'hero'

            # 전투 종료 조건
            if not self.hero.is_alive() or not self.monster.is_alive():
                battle_running = False

            pygame.display.update()
            self.clock.tick(30)


        self.display_result()

    def hero_attack(self):
        damage = self.hero.special_attack()
        self.monster.take_damage(damage)

    def monster_attack(self):
        if self.monster.is_alive():
            monster_damage = self.monster.attack
            self.hero.take_damage(monster_damage)

    def display_hero_status(self):
        # 영웅 상태 표시
        hero_name_text = self.font.render(f"{self.hero.name}", True, (0, 0, 0))
        hero_hp_text = self.font.render(f"HP: {self.hero.hp}", True, (0, 0, 0))
        hero_attack_text = self.font.render(f"Attack: {self.hero.attack}", True, (0, 0, 0))

        self.screen.blit(hero_name_text, (50, 80))
        self.screen.blit(hero_hp_text, (50, 110))
        self.screen.blit(hero_attack_text, (50, 140))

        # 영웅 체력바 그리기
        pygame.draw.rect(self.screen, (255, 0, 0), (50, 180, 200, 20))  # 배경
        pygame.draw.rect(self.screen, (0, 255, 0), (50, 180, 200 * (self.hero.hp / 100), 20))  # 체력

    def display_monster_status(self):
        # 몬스터 상태 표시
        monster_name_text = self.font.render(f"{self.monster.name}", True, (0, 0, 0))
        monster_hp_text = self.font.render(f"HP: {self.monster.hp}", True, (0, 0, 0))
        monster_attack_text = self.font.render(f"Attack: {self.monster.attack}", True, (0, 0, 0))

        self.screen.blit(monster_name_text, (self.WIDTH - 200, 50))
        self.screen.blit(monster_hp_text, (self.WIDTH - 200, 100))
        self.screen.blit(monster_attack_text, (self.WIDTH - 200, 150))

        # 몬스터 체력바 그리기
        pygame.draw.rect(self.screen, (255, 0, 0), (self.WIDTH - 200, 180, 200, 20))  # 배경
        pygame.draw.rect(self.screen, (0, 255, 0), (self.WIDTH - 200, 180, 200 * (self.monster.hp / 50), 20))  # 체력

    def display_result(self):
        if self.hero.is_alive():
            result_text = self.font.render(f"{self.hero.name} Win!", True, (0, 0, 0))
        else:
            result_text = self.font.render(f"{self.hero.name} Lose!", True, (0, 0, 0))

        self.screen.fill((255, 255, 255))
        self.screen.blit(result_text, (self.WIDTH // 2 - result_text.get_width() // 2, self.HEIGHT // 2))
        pygame.display.update()

        pygame.time.wait(2000)
