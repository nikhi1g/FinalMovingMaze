import TripleMain
# os.environ['DISPLAY'] = ":0.0"
# os.environ['KIVY_WINDOW'] = 'egl_rpi'
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from threading import Thread
from time import sleep
from pidev.kivy import DPEAButton

# from datetime import datetime

MAIN_SCREEN_NAME = 'main'
TIMER_SCREEN_NAME = 'TimerScreen'
WAIT_SCREEN_NAME = 'WaitScreen'
SCREEN_MANAGER = ScreenManager()


class KinectGUI(App):
    # class that runs the gui
    def build(self):
        # creates the window
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # sets the window color to white


class MainScreen(Screen):
    # class that handles the main events and stores objects from kivy file
    name_enter = ["a"]
    index = 0

    a1 = ObjectProperty(None)
    b1 = ObjectProperty(None)
    c1 = ObjectProperty(None)
    d1 = ObjectProperty(None)
    e1 = ObjectProperty(None)
    f1 = ObjectProperty(None)
    g1 = ObjectProperty(None)
    h1 = ObjectProperty(None)
    i1 = ObjectProperty(None)
    j1 = ObjectProperty(None)
    k1 = ObjectProperty(None)
    l1 = ObjectProperty(None)
    m1 = ObjectProperty(None)
    n1 = ObjectProperty(None)
    o1 = ObjectProperty(None)
    p1 = ObjectProperty(None)
    q1 = ObjectProperty(None)
    r1 = ObjectProperty(None)
    s1 = ObjectProperty(None)
    t1 = ObjectProperty(None)
    u1 = ObjectProperty(None)
    v1 = ObjectProperty(None)
    w1 = ObjectProperty(None)
    x1 = ObjectProperty(None)
    y1 = ObjectProperty(None)
    z1 = ObjectProperty(None)
    space = ObjectProperty(None)
    star = ObjectProperty(None)
    dash = ObjectProperty(None)
    delete = ObjectProperty(None)
    enter = ObjectProperty(None)
    timer = ObjectProperty(None)

    # making a file that appends each new name when it is entered:

    # this works, now how to add each line to an array so that it can be read and a leaderboard can be made. #burh the v key is missing
    fileonopen = open('namestorage.txt', 'w')
    fileonopen.write(' ')
    fileonopen.close()

    def A_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.a1.text))
        file.close()
        self.display_name()

    def B_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.b1.text))
        file.close()
        self.display_name()

    def C_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.c1.text))
        file.close()
        self.display_name()

    def D_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.d1.text))
        file.close()
        self.display_name()

    def E_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.e1.text))
        file.close()
        self.display_name()

    def F_Key_Update(self):
        file = open('namestorage.txt', 'a')  #
        file.write(str(self.f1.text))
        file.close()
        self.display_name()

    def G_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.g1.text))
        file.close()
        self.display_name()

    def H_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.h1.text))
        file.close()
        self.display_name()

    def I_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.i1.text))
        file.close()
        self.display_name()

    def J_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.j1.text))
        file.close()
        self.display_name()

    def K_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.k1.text))
        file.close()
        self.display_name()

    def L_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.l1.text))
        file.close()
        self.display_name()

    def M_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.m1.text))
        file.close()
        self.display_name()

    def N_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.n1.text))
        file.close()
        self.display_name()

    def O_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.o1.text))
        file.close()
        self.display_name()

    def P_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.p1.text))
        file.close()
        self.display_name()

    def Q_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.q1.text))
        file.close()
        self.display_name()

    def R_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.r1.text))
        file.close()
        self.display_name()

    def S_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.s1.text))
        file.close()
        self.display_name()

    def T_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.t1.text))
        file.close()
        self.display_name()

    def U_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.u1.text))
        file.close()
        self.display_name()

    def V_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.v1.text))
        file.close()
        self.display_name()

    def W_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.w1.text))
        file.close()
        self.display_name()

    def X_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.x1.text))
        file.close()
        self.display_name()

    def Y_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.y1.text))
        file.close()
        self.display_name()

    def Z_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.z1.text))
        file.close()
        self.display_name()

    def SPACE_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.space.text))
        file.close()
        self.display_name()

    def STAR_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.star.text))
        file.close()
        self.display_name()

    def DASH_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.dash.text))
        file.close()
        self.display_name()

    def ENTER_Key_Update(self):
        file = open('namestorage.txt', 'r')
        name = file.read()
        file.close()
        file = open('storage.txt', 'a')
        file.write(name)
        file.write('\n')
        file.close()
        sleep(0.4)
        SCREEN_MANAGER.current = WAIT_SCREEN_NAME


    def DELETE_Key_Update(self):  # this WORKS omg
        with open('namestorage.txt', 'rb+') as f:
            f.seek(0, 2)  # end of file
            size = f.tell()  # the size...
            f.truncate(size - 1)  # truncate at that size - how ever many characters
            self.display_name()


    def display_name(self):
        file = open('namestorage.txt', 'r')
        name = file.read()
        file.close()
        self.timer.text = name



class WaitScreen(Screen):
    def __init__(self, **kwargs):
        super(WaitScreen, self).__init__(**kwargs)

    loading = ObjectProperty(None)

class TimerScreen(Screen):

    def __init__(self, **kwargs):
        super(TimerScreen, self).__init__(**kwargs)

    timer = ObjectProperty(None)
    timer1 = ObjectProperty(None)

    # update the label of timer to be the seconds that have been passed

    def go_to_keyboard(self):
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME

    def timer_label_update(self):
        while True:
            self.timer.text = "Time passed: " + str(get_seconds()-13)
            sleep(0.5)
            if TripleMain.KinectIsOn == False:
                SCREEN_MANAGER.current = MAIN_SCREEN_NAME
                break

    def timer_label_update_thread(self):
        Thread(target=self.timer_label_update).start()



def everything_start():
    TripleMain.odrive_and_kinect_startup()


def get_seconds():
    while True:
        return TripleMain.seconds


Builder.load_file('TimerScreen.kv')
Builder.load_file('main.kv')
Builder.load_file('WaitScreen.kv')
SCREEN_MANAGER.add_widget(TimerScreen(name=TIMER_SCREEN_NAME))
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(WaitScreen(name=WAIT_SCREEN_NAME))
SCREEN_MANAGER.current = TIMER_SCREEN_NAME



if __name__ == '__main__':
    Thread(target=everything_start).start()
    KinectGUI().run()

# stackeeeeeexchange
# file = 'namestorage.txt'
# deleteeomthing___________(file, 1)#does this even work? #https://stackoverflow.com/questions/18857352/remove-very-last-character-in-file


# https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
