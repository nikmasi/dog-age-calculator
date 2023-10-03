import os
import sys

import pygame
import pygame_gui
import pygame.freetype
import checkbox

pygame.init()

width = 828
height = 445
BG=pygame.image.load("picture/Background.png")
smanjena_slika = pygame.transform.scale(BG, (828, 445))

class Button:
    def __init__(self, txt, pos,dim=None):
        self.text = txt
        self.pos = pos
        self.dim=dim
        if(dim==None):self.dim=(150,40)
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), self.dim)

    def draw(self):
        pygame.draw.rect(window, 'light yellow', self.button, 0, 5)
        pygame.draw.rect(window, 'light yellow', [self.pos[0], self.pos[1], self.dim[0],self.dim[1]], 5, 5)
        font=myfont = pygame.font.SysFont("monospace", 14)
        text2=font.render(self.text,True,'green')

        window.blit(text2, (self.pos[0] + 12, self.pos[1] + 12))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


def draw_window():
    window.fill(white_color)
    pygame.display.update()

def draw_Label(text,color,w,h,lw,hl,font=22):
    myfont = pygame.font.SysFont("monospace",font)
    label = myfont.render(text, 1, color)
    window.blit(label, (w-label.get_width()/int(lw), h-label.get_height()/int(hl)))

def draw_Button(text,w,h,wh=None,hw=None):
    button=None
    if(wh==None and hw==None):button = Button(text,(w,h))
    else:button = Button(text, (w, h), (wh, hw))
    button.draw()
    return button

def get_age(text1,text2,checklab):
    age=0
    small=[15,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80]
    medium=[15,24,28,32,36,42,47,51,56,60,65,69,74,78,83,87]
    large=[15,24,28,32,36,45,50,55,61,66,72,77,82,88,93,99]
    giant=[12,22,31,38,45,49,56,64,71,79,86,93,100,107,114,121]
    if checklab[0]=="s":
        if(int(text1)!=0 and int(text1)!=16):
            age=small[int(text1)-1]+(small[int(text1)]-small[int(text1)-1])*int(text2)/12
        elif(int(text1)==0): age=small[0]*int(text2)/12
        else: age=small[int(text1)-1]
    elif checklab[0]=="m":
        if (int(text1) != 0 and int(text1) != 16):
            age = medium[int(text1) - 1] + (medium[int(text1)] - medium[int(text1) - 1])*int(text2) / 12
        elif (int(text1) == 0):
            age =  medium[0]*int(text2) / 12
        else:
            age = medium[int(text1) - 1]
    elif checklab[0]=="l":
        if (int(text1) != 0 and int(text1) != 16):
            age = large[int(text1) - 1] + (large[int(text1)] - large[int(text1) - 1])*int(text2) / 12
        elif (int(text1) == 0):
            age = 0 + large[0]*int(text2) / 12
        else:
            age = large[int(text1) - 1]
    else:
        if (int(text1) != 0 and int(text1) != 16):
            age = giant[int(text1) - 1] + (giant[int(text1)] - giant[int(text1) - 1])*int(text2) / 12
        elif (int(text1) == 0):
            age = giant[0]*int(text2) / 12
        else:
            age = giant[int(text1) - 1]
    return str(round(age,2))


def third_window(text1,text2,checklab):
    while True:
        window.blit(smanjena_slika, (0, 0))

        draw_Label("The results", 'green',width / 2 ,height / 6,2,2,18)
        draw_Label("In human years your dog is", 'black',width / 2 ,height / 3,2,2)
        age = get_age(text1, text2, checklab)
        myfont = pygame.font.SysFont("monospace", 22)
        label3 = myfont.render(" " + age + " years old ", 1, 'green', 'white')
        window.blit(label3, (width / 2 - label3.get_width() / 2, height / 2 - label3.get_height() / 2))

        button =draw_Button('Again', width / 2-30, height / 2+50,70,40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.check_clicked():
                    main()

        pygame.display.update()

def second_window(checklab):
    text1=""
    text2=""
    while True:
        window.blit(smanjena_slika, (0, 0))
        draw_Label("How old is your dog?",'black',width / 2, height / 3,2,2)
        button=draw_Button('Next', width / 2-30, height / 2+50,70,40)
        draw_Label("year   month", 'black',width / 2,height / 2,2,-2,12)
        #draw_year_month()
        UI_REFRESH_RATE = clock.tick(60) / 1000
        text_input.background_colour=(pygame.color.Color(255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#main_text_entry'):
                text1=event.text
            if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#main_text_entry2'):
                text2=event.text
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.check_clicked():
                    if(text1!="" and text2!="" and int(text1)>=0 and int(text1)<=16 and int(text2)>=0 and int(text2)<=12):
                        third_window(text1,text2,checklab)
            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(window)
        pygame.display.update()


def firstTwo_window():
    boxes = []
    button = checkbox.Checkbox(window, width/2-150, height/2-60, 0, caption='small (20ibs or less/9.06kg or less)')
    button2 = checkbox.Checkbox(window, width/2-150, height/2-35, 1, caption='medium (21-50Ibs/9.513-22.65kg)')
    button3 = checkbox.Checkbox(window, width/2-150, height/2-10, 2, caption='large (51-100Ibs/23.103-45.3kg)')
    button4 = checkbox.Checkbox(window, width/2-150, height/2+15, 2, caption='giant (100+ Ibs/45.3+ kg)')
    boxes.append(button)
    boxes.append(button2)
    boxes.append(button3)
    boxes.append(button4)
    while True:
        window.blit(smanjena_slika, (0, 0))

        draw_Label("Size of dog?",'green',width / 2,height / 6,2,2)
        button=draw_Button('Next', width / 2-30, height / 2+50,70,40)
        checklab=""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in boxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        checklab=box.get_caption()
                        for b in boxes:
                            if b != box:
                                b.checked = False
                if button.check_clicked():
                    if(checklab!=""):
                        second_window(checklab)

        for box in boxes:
            box.render_checkbox()


        pygame.display.update()
    pygame.time.wait(1000)


def first_window():
    while True:
        window.blit(smanjena_slika, (0, 0))
        draw_Label("How old is your dog in human years?",'black',width / 2,height / 3,2,2)
        button=draw_Button('Begin calculator', width / 2 - 70, height / 2 - 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.check_clicked():
                    firstTwo_window()
        pygame.display.update()

def main():
    global window
    global manager
    global text_input
    global text_input2
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dog age calculator")

    manager = pygame_gui.UIManager((825, 445))
    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((width / 2 - 42, height / 2 - 25), (30, 30)), manager=manager,
        object_id='#main_text_entry')

    text_input2 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((width / 2 + 8, height / 2 - 25), (30, 30)), manager=manager,
        object_id='#main_text_entry2')

    first_window()

window=None
manager = None
text_input = None
text_input2 =None
clock = pygame.time.Clock()

if __name__ == '__main__':
    white_color = (255, 255, 255)
    main()
