import pygame
import time
import sys
import random
import threading
import os
pygame.init() #라이브러리 초기화
#color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)

#파일경로
now_path=os.path.dirname(__file__)
image_file_path=os.path.join(now_path,"image")
bgm_file_path=os.path.join(now_path,"브금")


def display(color_=False): 
    if color_: Game_screen.fill(color_) #color 인수로 들어오면 color색으로 화면 덮기
    pygame.display.update() #창 띄우기 

def Open_screen(color,caption,size=[800,600]):#창 만들기(배경색,캡션이름,해상도)
    global Game_screen
    Game_screen=pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    display(color)

def Open_text(Font_size,string,Font,color,xy):#텍스트 띄우기(글씨크기,문구,폰트,색,좌표)
    text_box=pygame.font.SysFont(Font,Font_size)
    text=text_box.render(string,True,color)
    Game_screen.blit(text,xy)
    display()

def KEY_CHECK():
    for event in pygame.event.get(): #나가기 누를때 종료
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    key_pressed=pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]: #ESC 누를 때 종료
        pygame.quit()
        sys.exit()
    return key_pressed #누른 키 리스트 반환

def Game_over():
    Open_text(72,"Game Over!","Bold",Red,(260,200))
    time.sleep(1)
    pygame.quit()
    sys.exit()

class character:
    def __init__(self,address):
        self.image=pygame.image.load(address)  
        self.pos_x=350 #초기 위치=중간
        self.speed=10 #속력
        self.score=0
    def pos(self): #좌표 반환
        return (self.pos_x,500) 
    def pos_loop(self):#캐릭터 화면 벗어나면 반대편에서 나오기
        if self.pos_x<-60 :
            self.pos_x=840+self.pos_x
        elif self.pos_x>780:
            self.pos_x=self.pos_x-840
    def move(self,key_pressed): #방향키 확인 후 캐릭터 위치 조정
        if key_pressed[pygame.K_LEFT]: 
            self.pos_x=self.pos_x-self.speed
        elif key_pressed[pygame.K_RIGHT]: 
            self.pos_x=self.pos_x+self.speed
        self.pos_loop() 

class leaf:
    def __init__(self,item_number):
        self.item_number=item_number
        if item_number == 0: #아이템 넘버0 = 나뭇잎
            self.image = pygame.image.load(os.path.join(image_file_path,"eh1.png"))
        elif item_number == 1:#아이템 넘버1= 속도 초기화 아이템
            self.image = pygame.image.load(os.path.join(image_file_path,"Re.png"))
        elif item_number == 2: #아이템 넘버2= 화면 클리어 아이템
            self.image = pygame.image.load(os.path.join(image_file_path,"delete.png"))
        self.pos_x = random.randrange(0,8)*100+25 # 나뭇잎 x좌표 랜덤설정(간격100)
        self.pos_y = 10
        self.initial_speed = random.randrange(2,6)
    def speed(self):
        self.total_speed = self.initial_speed+leaves_change_speed
        if self.total_speed>50:
            self.total_speed = 50
        return self.total_speed
    def pos(self):
        return [self.pos_x,self.pos_y]
    
def leaf_create():
    leaves.append(leaf(0)) # 나뭇잎 만들어서 리스트에 추가
    threading.Timer(1,leaf_create).start() #1초마다 반복

def Colide_Check(character_pos_x,index): #충돌하면 game_over
    global leaves
    global leaves_change_speed
    global falling_item
    if len(leaves)-1<index : return 0
    if 480<leaves[index].pos_y<560 : 
        if leaves[index].pos_x-91<character_pos_x<leaves[index].pos_x+50:#충돌인경우
            if leaves[index].item_number==0: # 나뭇잎이면
                bgm2=pygame.mixer.Sound(os.path.join(bgm_file_path,"삐.wav")) #효과음
                bgm2.play()
                if len(hearts)>1 : 
                    del hearts[len(hearts)-1]
                    time.sleep(0.5)
                    leaves.remove(leaves[index])
                else : Game_over() #하트 없으면 게임오버
            elif leaves[index].item_number==1:
                leaves_change_speed=0
                leaves.remove(leaves[index])
                falling_item=False
            else:
                Ironman.score=Ironman.score+len(leaves)-1
                leaves=[]
                falling_item=False
            
class heart:
    def __init__(self,index):
        self.pos_x=40*index+15
        self.pos_y=10
        self.image=pygame.image.load(os.path.join(image_file_path,"하트.png"))
    
    def pos(self):
        return [self.pos_x,self.pos_y]

def falling_leaf(index):
    if index>=len(leaves): return 0 #리스트 아웃 오브 레인지 방지 
    Game_screen.blit(leaves[index].image,leaves[index].pos()) # 화면에 나뭇잎 나타내기
    leaves[index].pos_y=leaves[index].pos_y+leaves[index].speed() #좌표 조정
    falling_leaf(index+1) 
    #재귀함수 호출(바로 다음 인덱스로 가기 때문에 리스트 끝에 도달 후 밑에 코드 실행)
    Colide_Check(Ironman.pos_x,index) 
    #마지막 인덱스부터 먼저 실행 하고 첫 번째 인덱스가 마지막으로 실행


def main() :
    #초기 화면
    Open_screen(White,"Dodge Leaves")   
    Open_text(30,"Push an spacebar to start!","Monospace",Red,(170,210))

    
    #스페이스바 대기
    Run=False
    while not Run:  
        pressed=KEY_CHECK() # 키 누르는지 확인
        if pressed[pygame.K_SPACE] : #스페이스바 눌렀을 때 
            Run=True
            display(White) #하얀 바탕으로 덮기
            Open_text(72,"Start!","Bold",Red,(340,200)) #1초 동안 start! 문구 나타내기
            time.sleep(1)
            display(White)
            pygame.mixer.music.load(os.path.join(bgm_file_path,'bgm1.mp3'))
            pygame.mixer.music.play(-1)
            
    #게임 중
    global Ironman 
    Ironman=character(os.path.join(image_file_path,"Ironman.png")) #캐릭터 생성
    global leaves_change_speed
    leaves_change_speed=0
    global leaves
    leaves=[] # 전체 나뭇잎 관리할 리스트
    global hearts
    hearts=[heart(0),heart(1),heart(2)]
    global falling_item
    falling_item=False
    clock= pygame.time.Clock()
    leaf_create()
    
 
    while Run:
        pressed=KEY_CHECK() #키 누르는지 확인
        Ironman.move(pressed) #캐릭터 이동
        Game_screen.blit(Ironman.image,Ironman.pos())
        for x in range(len(hearts)):
            Game_screen.blit(hearts[x].image,hearts[x].pos()) #하트 표시
        
        falling_leaf(0) #떨어지는 나뭇잎 좌표 조정 및 충돌 확인
        leaves.sort(key=lambda leaf: leaf.pos_y,reverse=True) 
	#바닥에 가까운 순으로 나뭇잎 정렬

        while len(leaves) and leaves[0].pos_y>560: #바닥 도달한 아이템 있으면
            if leaves[0].item_number==0:
                Ironman.score=Ironman.score+1 #나뭇잎이면 점수 추가
                if Ironman.score%10==0 and Ironman.score: #10점마다 속도업
                    leaves_change_speed=leaves_change_speed+1
                if Ironman.score%20==0 and falling_item==False:
                    leaves.append(leaf(random.randrange(1,3)))
                    falling_item=True
            else:
                falling_item=False #나뭇잎이 아님->아이템 바닥 도달->떨어지는 아이템없음
            leaves.remove(leaves[0]) #전체 아이템 리스트에서 뺌
              
        Open_text(48,"Points : {}".format(Ironman.score),"Bold",Black,(320,0))
        Game_screen.fill(White)
        clock.tick(30)
           
main()


