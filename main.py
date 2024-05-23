import pygame
import tool
import os
import setup
import time
pygame.init()
screen = pygame.display.get_surface()
state='start'
slide_y=0
timer=0
pre_event=None
pre_event2=None
check=0
subject_slide=[]
subject_index=0
for i in range(20):
    y=100-(800/350*slide_y)+i*60
    temp=tool.blit_dialog(screen,setup.unifont_36,["項目"+str(i+1)],(0,0,0),(150,y),size=[230,40],center=True,return_img=True,background_color=(35,125,255),frame_color=(0,0,0))
    temp1=tool.blit_dialog(screen,setup.unifont_36,["項目"+str(i+1)],(0,0,0),(150,y),size=[230,40],center=True,return_img=True,background_color=(35,125,255),frame_color=(255,255,255))
    temp2=pygame.transform.scale(temp1,(220,30))
    button_temp=tool.Button(screen,temp,temp1,temp2,150,y)
    subject_slide.append(button_temp)
while True:
    screen.fill((181,230,29))
    if state=='start':
        tool.blit_text(screen,setup.unifont_36,'Phet推廣',(0,0,0),(150,50),center=True)
        setup.start_button_1.draw()
        setup.start_button_2.draw()
        setup.start_button_3.draw()
        setup.start_button_4.draw()
        setup.start_button_5.draw()
        setup.start_button_6.draw()
    elif state=='subject':
        for button in subject_slide:
            button.centery=100-(800/350*slide_y)+subject_slide.index(button)*60
            button.img_0_rect.center=(button.centerx,button.centery)
            button.img_1_rect.center=(button.centerx,button.centery)
            button.img_2_rect.center=(button.centerx,button.centery)
            if button.centery<100:
                button.use=False
            else:
                button.use=True
            button.draw()
        temp=pygame.Surface((300,75))
        temp.fill((181,230,29))
        tool.blit_image(screen,temp,(0,0))
        setup.search_button.draw()
        setup.return_button.draw()
        tool.blit_image(screen,setup.slider,(280,slide_y+100),center=True)
    elif state=='main':
        tool.blit_text(screen,setup.unifont_36,'項目'+str(subject_index+1),(0,0,0),(150,50),center=True)
        setup.return_button.draw()
        setup.main_button_1.draw() 
        setup.main_button_2.draw()
        setup.main_button_3.draw()
        setup.main_button_4.draw()
    elif state=='main_1':
        tool.blit_text(screen,setup.unifont_36,'學習此項目的教材',(0,0,0),(150,100),center=True)
        tool.blit_text(screen,setup.unifont_36,'由於Phet上沒有',(0,0,0),(150,160),center=True)
        tool.blit_text(screen,setup.unifont_36,'需去網路上找',(0,0,0),(150,200),center=True)
        tool.blit_text(screen,setup.unifont_36,'或自行編寫',(0,0,0),(150,240),center=True)
        setup.return_button.draw()
    elif state=='main_2':
        tool.blit_text(screen,setup.unifont_36,'動畫操作介面',(0,0,0),(150,100),center=True)
        tool.blit_text(screen,setup.unifont_36,'最好讓手機',(0,0,0),(150,140),center=True)
        tool.blit_text(screen,setup.unifont_36,'橫向操作',(0,0,0),(150,180),center=True)
        setup.return_button.draw()
        setup.main2_button_1.draw()
    elif state=='main_2_1':
        tool.blit_text(screen,setup.unifont_36,'Phet上的教師手冊',(0,0,0),(150,100),center=True)
        tool.blit_text(screen,setup.unifont_36,'最好要經過翻譯',(0,0,0),(150,140),center=True)
        setup.return_button.draw()
    elif state=='main_3':
        tool.blit_text(screen,setup.unifont_36,'題目或習題',(0,0,0),(150,100),center=True)
        tool.blit_text(screen,setup.unifont_36,'可以參考網站上的',(0,0,0),(150,140),center=True)
        tool.blit_text(screen,setup.unifont_36,'教師提交的活動',(0,0,0),(150,180),center=True)
        setup.return_button.draw()
    elif state=='main_4':
        tool.blit_text(screen,setup.unifont_36,'連結到網站上',(0,0,0),(150,100),center=True)
        tool.blit_text(screen,setup.unifont_36,'該項目的網址',(0,0,0),(150,140),center=True)
        setup.return_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEWHEEL:
            if state=='subject':
                if event.y>0:
                    slide_y-=50
                    if slide_y<0:
                        slide_y=0
                else:
                    slide_y+=50
                    if slide_y>350:
                        slide_y=350
                for button in subject_slide:
                    button.reset()
                
        if state=='start':
            if setup.start_button_1.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
            elif setup.start_button_2.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
            elif setup.start_button_3.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
            elif setup.start_button_4.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
            elif setup.start_button_5.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
            elif setup.start_button_6.handle_event(event):
                state='subject'
                slide_y=0
                setup.start_button_1.use=False
                setup.start_button_2.use=False
                setup.start_button_3.use=False
                setup.start_button_4.use=False
                setup.start_button_5.use=False
                setup.start_button_6.use=False
                setup.search_button.use=True
                setup.return_button.use=True
        elif state=='subject':
            if (event.type!=pygame.MOUSEWHEEL and pre_event.type!=pygame.MOUSEWHEEL) or check==1:
                if check==1 or pygame.mouse.get_pressed()[0]==1 or event.type==pygame.MOUSEMOTION:
                    if setup.search_button.handle_event(event):#他媽的滑鼠滾輪會回傳MOUSEBUTTONUP和MOUSEBUTTONDOWN
                        pass
                    elif setup.return_button.handle_event(event):
                        state='start'
                        setup.search_button.use=False
                        for button in subject_slide:
                            button.use=False
                        setup.return_button.use=False
                        setup.start_button_1.use=True
                        setup.start_button_2.use=True
                        setup.start_button_3.use=True
                        setup.start_button_4.use=True
                        setup.start_button_5.use=True
                        setup.start_button_6.use=True
                    for button in subject_slide:
                        if button.handle_event(event):
                            state='main'
                            subject_index=subject_slide.index(button)
                            setup.search_button.use=False
                            for button in subject_slide:
                                button.use=False
                            setup.return_button.use=True
                            setup.main_button_1.use=True
                            setup.main_button_2.use=True
                            setup.main_button_3.use=True
                            setup.main_button_4.use=True
                if check==1:
                    check=0
                if pygame.mouse.get_pressed()[0]==1:
                    check=1
        elif state=='main':
            if setup.return_button.handle_event(event):
                state='subject'
                setup.search_button.use=True
                setup.return_button.use=True
                for button in subject_slide:
                    button.use=True
                setup.main_button_1.use=False
                setup.main_button_2.use=False
                setup.main_button_3.use=False
                setup.main_button_4.use=False
            elif setup.main_button_1.handle_event(event):
                state='main_1'
                setup.main_button_1.use=False
                setup.main_button_2.use=False
                setup.main_button_3.use=False
                setup.main_button_4.use=False
            elif setup.main_button_2.handle_event(event):
                state='main_2'
                setup.main_button_1.use=False
                setup.main_button_2.use=False
                setup.main_button_3.use=False
                setup.main_button_4.use=False
                setup.main2_button_1.use=True
            elif setup.main_button_3.handle_event(event):
                state='main_3'
                setup.main_button_1.use=False
                setup.main_button_2.use=False
                setup.main_button_3.use=False
                setup.main_button_4.use=False
            elif setup.main_button_4.handle_event(event):
                state='main_4'
                setup.main_button_1.use=False
                setup.main_button_2.use=False
                setup.main_button_3.use=False
                setup.main_button_4.use=False
        elif state=='main_1':
            if setup.return_button.handle_event(event):
                state='main'
                setup.main_button_1.use=True
                setup.main_button_2.use=True
                setup.main_button_3.use=True
                setup.main_button_4.use=True
        elif state=='main_2':
            if setup.return_button.handle_event(event):
                state='main'
                setup.main_button_1.use=True
                setup.main_button_2.use=True
                setup.main_button_3.use=True
                setup.main_button_4.use=True
                setup.main2_button_1.use=False
            elif setup.main2_button_1.handle_event(event):
                state='main_2_1'
                setup.main2_button_1.use=False
        elif state=='main_2_1':
            if setup.return_button.handle_event(event):
                state='main_2'
                setup.main2_button_1.use=True
        elif state=='main_3':
            if setup.return_button.handle_event(event):
                state='main'
                setup.main_button_1.use=True
                setup.main_button_2.use=True
                setup.main_button_3.use=True
                setup.main_button_4.use=True
        elif state=='main_4':
            if setup.return_button.handle_event(event):
                state='main'
                setup.main_button_1.use=True
                setup.main_button_2.use=True
                setup.main_button_3.use=True
                setup.main_button_4.use=True
        pre_event2=pre_event
        pre_event=event
    pygame.display.update()