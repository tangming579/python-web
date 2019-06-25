import sys
import pygame

def run_game():
	#初始化游戏并创建屏幕对象
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (230, 230, 230)
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