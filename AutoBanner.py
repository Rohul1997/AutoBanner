import os
import time
import ctypes
import sys

start = True
while start:
    retry = True
    while retry:
        #title = raw_input('type in your games folder name found from output/ then press enter:\n')
        title = sys.argv[1]
        if os.path.exists("output/"+title):
            os.system('cls')
            print "output/"+title+" folder found"
            retry = False
        else:
            os.system('cls')
            print "output/"+title+" folder does not exist"
            
    #copy cliboard work
    def Clb(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

    #declare ctrl+v and then enter as paste
    paste = 'ctypes.windll.user32.keybd_event(0x11, 0, 0, 0), ctypes.windll.user32.keybd_event(ord("V"), 0, 0, 0), ctypes.windll.user32.keybd_event(0x11, 0, 0x0002, 0), ctypes.windll.user32.keybd_event(ord("V"), 0, 0x0002, 0), ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0), ctypes.windll.user32.keybd_event(0x0D, 0, 0x0002, 0)'

    #set cwd as current working directory
    cwd = os.getcwd()

    #declare left click down, left click up as Lclick
    Lclick = 'ctypes.windll.user32.mouse_event(2, 0, 0, 0,0), ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)'

    #open ohana
    print 'Please wait whilst the banner work is being completed\nJust sit back, do not touch anything and let me do the hard work ;)'
    raw_input('Press Enter to continue...')
    os.startfile('tools\Ohana3DS.exe')
    os.system('cls')
    print 'Automation in progress please wait....'
    time.sleep(3)

    #mouse pos to texture tab and then click x2
    ctypes.windll.user32.SetCursorPos(295, 180)
    exec Lclick
    exec Lclick

    #declare mouse pos to open button as openB
    openB = 'ctypes.windll.user32.SetCursorPos(550, 610)'
    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner0.bcmdl")
    time.sleep(0.5)

    #paste from clipboard and enter
    exec paste
    time.sleep(0.5)

    #declare mouse pos to open button as importB
    importB = 'ctypes.windll.user32.SetCursorPos(640, 640)'
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\common1.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to common1_2 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\common1_2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to common1_3 and then import
    ctypes.windll.user32.SetCursorPos(350, 158)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\common1_3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1)

    #declare mouse pos to save button as saveB
    saveB = 'ctypes.windll.user32.SetCursorPos(550, 640)'
    exec saveB
    exec Lclick
    time.sleep(0.5)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner1.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner2.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner3.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner4.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner5.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner6.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner7.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to EUR_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\EUR_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner8.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to USA_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner10.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to USA_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner11.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to USA_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner12.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to USA_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    exec openB
    exec Lclick
    Clb(cwd + "\\banner\\banner13.bcmdl")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN2.png")
    time.sleep(0.5)

    exec paste
    time.sleep(0.5)

    #mouse pos to USA_EN3 and then import
    ctypes.windll.user32.SetCursorPos(350, 140)
    exec Lclick
    exec importB
    exec Lclick
    Clb(cwd + "\\output\\" + title + "\\USA_EN3.png")
    time.sleep(0.5)

    exec paste
    time.sleep(1.5)

    exec saveB
    exec Lclick
    time.sleep(1)

    os.system("TASKKILL /F /IM Ohana3DS.exe")
    os.system('cls')
    print 'Creating banner.bin'
    os.system('tools\\3dstool -c -f "output\\' + title + '\\banner.bin" -t banner --banner-dir banner')
    print 'banner.bin file created inside output/'+title+'/banner.bin'
    print 'AutoBanner complete'
    start = False
