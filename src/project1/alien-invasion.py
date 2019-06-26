import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	#初始化游戏并创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen)
	#游戏主循环
	while True:		
		#监听键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		pygame.display.flip()
			
run_game()