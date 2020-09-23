import pygetwindow as gw
import pyautogui
import requests
import subprocess
from Processing import *

accounts=[]
nowVersion=16
request=requests.get('https://hagamiyuusan.github.io/checkdownload.json')
rq=request.json()
availVersion=int(rq['version'])
thongbao=rq['tinnhan']

def main():
    pyautogui.alert(thongbao, title='Cho e quang cao 1 xiu =))))))))')
    alert="Canh bao: Xin hay chac chan rang dang chay voi quyen admin\n\n"
    accountCount=int(pyautogui.prompt(text=alert+'Nhap so luong account: ', title='Onmyoji bot' , default='1'))
    while accountCount:
        accountCount-=1
        name_acc='Account '+str(accountCount)+'\n\n'
        gameMode="The loai:\n1. To doi 2 nguoi ran/thuc tinh\
             \n2. Tham hiem to doi \
                \n3. Tham hiem 1 nguoi \
                  \n4. Pha ket gioi \
                  \n5. Phong an yeu khi \
                  \n6. Su kien\n "
        gameMode=int(pyautogui.prompt(text=alert+name_acc+gameMode, title='Auto ADS' , default='3'))
        isCaptain=True
        isMainDMG=True
        windowName=int(pyautogui.prompt(text=alert+name_acc+'Enter name of window game: \n1. Onmyoji \n2. LDPlayer(64) ', title='Onmyoji bot' , default='1'))
        if windowName==1:
            windowName='Onmyoji'
        else:
            windowName='LDPlayer(64)'
        if windowName==1:
            cuaso1=gw.getWindowsWithTitle(windowName)[0]
            cuaso1.resizeTo(1138, 672)
        count=int(pyautogui.prompt(text=alert+name_acc+'Nhap so lan muon di: ', title='Auto ADS' , default='9999'))
        if gameMode==4:
            vitri=int(pyautogui.prompt(text=alert+name_acc+'Nhap vi tri ban muon target\nDe 0 neu ban khong muon: ', title='Auto ADS' , default='0'))
        if gameMode == 1 or gameMode == 2 or gameMode == 3 or gameMode ==5 or gameMode ==6 or gameMode==7:
            vitri=0
        if gameMode ==3 or gameMode == 2:
            phoban=str(pyautogui.prompt(text=alert+name_acc+'Nhap map ban muon auto: ', title='Auto ADS' , default='28'))
        """if gameMode ==3 or gameMode == 2:
            challengeBoss=pyautogui.prompt(text=alert+name_acc+'Ban co muon chi danh quai exp(Y/N): ', title='Auto ADS' , default='Y')
            if challengeBoss=='y' or challengeBoss=='Y':
                challengeExp=True
            else:
                challengeExp=False"""
        if gameMode == 1 or gameMode == 4 or gameMode == 5 or gameMode ==6 or gameMode==7:
            phoban='28'
        if gameMode == 2 or gameMode == 1:
            isCaptainChar=pyautogui.prompt(text=alert+name_acc+'Ban co phai la leader k(Y/N): ', title='Auto ADS' , default='Y')
            isMainDMGChar=pyautogui.prompt(text=alert+name_acc+'Ban co phai dame chinh k(Y/N): ', title='Auto ADS' , default='Y')
            if isCaptainChar=='y' or isCaptainChar=="Y":
                isCaptain=True
            else:
                isCaptain=False
            if isMainDMGChar=='y' or isMainDMGChar=="Y":
                isMainDMG=True
            else:
                isMainDMG=False
        
        accounts.append(Processing(windowName,gameMode,count,isCaptain,isMainDMG,str(phoban),int(vitri)))
    
    if len(accounts) == 2:
        accounts.append(Processing('[#] Onmyoji [#]',2,9999,False,True,str('28'),int('0')))
        account1=threading.Thread(accounts[0].run())
        account2=threading.Thread(accounts[1].run())
    else:
        account1=threading.Thread(accounts[0].run())
    

if nowVersion>=availVersion:
	main()
elif nowVersion<availVersion:
	pyautogui.alert('Da het han su dung, vui long download ban moi', title='Kich hoat')


