import pygame
import sys

# 初始化 pygame
pygame.init()

# 设置游戏窗口大小
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("山海经冒险游戏")

# 定义帧率
clock = pygame.time.Clock()

# 加载背景图片 (png格式)
background = pygame.image.load('assets/images/background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))  # 调整背景图大小

# 加载中文字体
font_path_chinese = 'assets/fonts/FZZiZLDJW.TTF'  # 中文字体
font_chinese = pygame.font.Font(font_path_chinese, 72)

# 加载英文字体
font_path_english = 'assets/fonts/joystix.ttf'  # 英文字体
font_english = pygame.font.Font(font_path_english, 28)  # 英文字体大小为28

# 加载音效文件
click_sound = pygame.mixer.Sound('assets/sounds/click_sound.wav')
intro_sound = pygame.mixer.Sound('assets/sounds/intro_sound.wav')  # 开场背景音效

# 加载按钮图片 (png格式)
button_image = pygame.image.load('assets/images/start_button.png').convert_alpha()
button_rect = button_image.get_rect(center=(screen_width // 2, screen_height // 1.3))  # 按钮位置在屏幕下方

# 开场页面显示
def show_intro():
    # 播放开场背景音效
    intro_sound.play(-1)  # -1 表示循环播放背景音效

    running = True
    fade_in_time = 3  # 字体逐渐浮现的时间（秒）
    fade_in_speed = 255 / (fade_in_time * 60)  # 每帧字体透明度增加量（每秒60帧）

    # 中文文字
    text_chinese = font_chinese.render("山海经冒险游戏", True, (255, 255, 255))  # 白色文字
    text_rect_chinese = text_chinese.get_rect(center=(screen_width // 2, screen_height // 3))  # 中文文字位置调整

    # 英文文字
    text_english = font_english.render("Shan Hai Jing Adventure Game", True, (255, 255, 255))  # 白色文字
    text_rect_english = text_english.get_rect(center=(screen_width // 2, screen_height // 2.3))  # 英文文字在中文下方

    # 设置透明度初始值
    alpha_value = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos) and alpha_value >= 255:  # 确保完全显示后才可点击
                    click_sound.play()  # 播放点击音效
                    pygame.time.delay(500)  # 等待音效播放完成
                    intro_sound.stop()  # 停止背景音效
                    return  # 结束函数以便进入下一个界面

        # 填充背景
        screen.blit(background, (0, 0))

        # 逐渐增加透明度
        if alpha_value < 255:
            alpha_value += fade_in_speed
        else:
            alpha_value = 255

        # 应用透明度到文字
        text_chinese.set_alpha(alpha_value)
        text_english.set_alpha(alpha_value)

        # 应用透明度到按钮
        button_image.set_alpha(alpha_value)

        # 绘制文字
        screen.blit(text_chinese, text_rect_chinese)
        screen.blit(text_english, text_rect_english)

        # 绘制按钮
        screen.blit(button_image, button_rect)

        # 刷新显示
        pygame.display.flip()
        clock.tick(60)  # 设置帧率

# 主循环
def main():
    show_intro()  # 显示开场页面

    # 进入下一个界面（比如游戏菜单或第一个关卡）
    print("进入下一个界面！")  # 测试用

    pygame.quit()
    sys.exit()

# 启动主循环
if __name__ == "__main__":
    main()

