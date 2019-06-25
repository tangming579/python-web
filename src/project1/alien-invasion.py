import sys
import pygame

from settings import Settings

def run_game():
	#初始化游戏并创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	bg_color = ai_settings.bg_color
	#游戏主循环
	while True:		
		#监听键盘和鼠标事件
		for even in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		screen.fill(bg_color)
		pygame.display.flip()
			
run_game()