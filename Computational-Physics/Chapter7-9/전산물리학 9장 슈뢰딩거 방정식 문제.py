#바닥상태에 있는 수소원자의 고유에너지와 파동함수를 계산하는 프로그램

import math as m

#initial condition
dr=0.01 #r의 변위
r_range=[0,400*dr] #r의 범위(0-inf), 4는 무한대에 해당하는 값

ee=0.0144 #퍼텐셜 에너지 -ke^2/r 에서 ke^2 만 계산한 결과
hbarc=197.33*1000.*1.e-5 # 단위는 kev
prm=938.28*1000.
elm=0.511003*1000.
reduced_mass=prm*elm/(prm+elm) #전자와 양성자의 reduced mass

dE=0.05/1000 #에너지 변위
E_range=[-20/1000,0] #에너지 범위



#퍼텐셜 에너지 E(r)구하는 함수
def pE(rrange):#r의 범위를 받아옴
    
    global Ep #퍼텐셜 에너지 저장할 리스트
    Ep=[0]

    r=rrange[0]
    while r<rrange[1]:
        r=r+dr
        Ep.append(-ee/r)



#바닥상태에서의 에너지 고유치 구하는 함수
def detect_Ep(Erange,rm): #탐색할 에너지 범위, rm 받아옴

    E=Erange[0]
    while E<=Erange[1]: #에너지 변화시키면서 경계조건 만족여부 확인

        # ui(r) 구하기
        wavei=[0,1.e-18] #ui[r] 저장할 리스트, u(0)=0, u(h)=b (b는 임의의 상수)
        
        for x in range(1,int(rm/dr)+2):
            r=x*dr
            vi_r=(Ep[x]-E)*2*reduced_mass/(hbarc**2) #vi(r)구하기
            wavei.append(2*wavei[x]-wavei[x-1]+(dr**2)*vi_r*wavei[x]) #_Stormer method_

        # ue(r) 구하기
        wavee=[0,m.e**(-399*dr)] #ue(r)저장할 리스트, ue(inf)=0,ue(-h)=b'
        for x in range(399,int(rm/dr)-2,-1):
            r=x*dr
            index=len(wavee)-1
            ve_r=(Ep[x]-E)*2*reduced_mass/(hbarc**2) #ve(r)구하기
            wavee.append(2*wavee[index]-wavee[index-1]+(dr**2)*ve_r*wavee[index])

        #r=rm에서 ui'/ui=ue'/ue 맞는지 확인
        rm_i=int(rm/dr)
        ui_rm=wavei[rm_i]
        d_ui_rm=(8*(wavei[rm_i+1]-wavei[rm_i-1])-wavei[rm_i+2]+wavei[rm_i-2])/12/dr
        ratio_i=d_ui_rm/ui_rm 

        rm_e=len(wavee)-3
        ue_rm=wavee[rm_e]
        d_ue_rm=(8*(wavee[rm_e+1]-wavee[rm_e-1])-wavee[rm_e+2]+wavee[rm_e-2])/12/-dr
        ratio_e=d_ue_rm/ue_rm 

        if abs(ratio_i-ratio_e)/abs(ratio_i)<0.005: #상대오차가 0.5%보다 작으면
            energy=E #에너지 고유치는 현재 E값

            global wave
            wave=[0]
            cons=wavei[rm_i]/wavee[rm_e] #b/b'
            
            for x in range(1,rm_i+1):
                wave.append(wavei[x])
                
            cnt=0
            for x in range(rm_i+1,401):
                wave.append(wavee[rm_e-cnt]*cons)
                cnt=cnt+1

            return energy
        E=E+dE

        
#메인함수  
def main():
    
    pE(r_range) #r에 따른 퍼텐셜 에너지 구하기

    ans=detect_Ep(E_range,1) # 에너지 고유치 탐색
    
    print("E=%fev"%(ans*1000))

    print(wave)

main()
