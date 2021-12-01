import random
import time

import keyboard

import TripleMain
# os.environ['DISPLAY'] = ":0.0"
# os.environ['KIVY_WINDOW'] = 'egl_rpi'
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.core.window import Window, Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from threading import Thread
from time import sleep
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
# from datetime import datetime
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel
from pidev.MixPanel import MixPanel

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

    #cursormovement
    square = ObjectProperty(None)
    enterpressed = False
    x_check = 0
    y_check = 0
    def CursorCheck(self):
        print("CursorCheck")
        MainObjectList = [self.a1,self.b1,self.c1,self.d1,self.e1,self.f1,self.g1,self.h1,self.i1,self.j1,self.k1,self.l1,self.m1,self.n1,self.o1,self.p1,self.q1,self.r1,self.s1,self.t1,self.u1,self.v1,self.w1,self.x1,self.y1,self.z1,self.space,self.star,self.dash,self.delete,self.enter]

        while self.enterpressed == False:
            if TripleMain.leftmove:
                print('leftmove')
                for i in range(14):
                    self.square.x -= 5.7
                TripleMain.leftmove = False

            if TripleMain.rightmove:
                print('right move')
                for x in range(14):
                    self.square.x += 5.7
                TripleMain.rightmove = False
            if TripleMain.click:
                print('clcked')
                # print('x:',self.square.x)
                # print('y:',self.square.y)
                for thing in MainObjectList:
                    #print(thing.text)
                    if self.square.collide_widget(thing):
                        print(thing.text)
                        #thing.on_press()
                        thing.trigger_action(duration=0.1)
                        thing.color = (1,1,1,1)
                        sleep(0.2)
                        thing.color = (0,1,0,1)
                        #thing.state = 'down'
                        #sleep(0.2)
                        #thing.state = 'normal'


                TripleMain.click = False

            if TripleMain.upmove:
                print('up move')
                for y in range(14):
                    self.square.y += 6.5
                TripleMain.upmove = False

            if TripleMain.downmove:
                print('down move')
                for y in range(14):
                    self.square.y -= 6.5
                TripleMain.downmove = False

            sleep(1.2)


        # while self.enterpressed == False:
        #     if TripleMain.leftmove:
        #         print('leftmove')
        #         for i in range(14):
        #             self.x_check -= 1
        #             if self.x_check < 0:
        #                 self.x_check=0
        #             elif self.x_check >= 0:
        #                 self.square.x -= 5.7
        #
        #         TripleMain.leftmove = False
        #
        #     if TripleMain.rightmove:
        #         print('right move')
        #         for x in range(14):
        #             self.x_check += 1
        #             if self.x_check > 9:
        #                 self.x_check = 9
        #             elif self.x_check <= 9:
        #                 self.square.x += 5.7
        #         TripleMain.rightmove = False
        #
        #     if TripleMain.click:
        #         print('clcked')
        #         TripleMain.click = False
        #
        #     if TripleMain.upmove:
        #         print('up move')
        #         for y in range(14):
        #             self.y_check -= 1
        #             if self.y_check < 0:
        #                 self.y_check = 0
        #             elif self.y_check >= 0:
        #                 self.square.y += 6.5
        #         TripleMain.upmove = False
        #
        #     if TripleMain.downmove:
        #         print('down move')
        #         for y in range(14):
        #             self.y_check += 1
        #             if self.y_check > 2:
        #                 self.y_check=2
        #             elif self.y_check <= 2:
        #                 self.square.y -= 6.5
        #         TripleMain.downmove = False
        #     print(self.x_check)
        #     print(self.y_check)
        #     sleep(.8)
    # making a file that appends each new name when it is entered:

    # this works, now how to add each line to an array so that it can be read and a leaderboard can be made. #burh the v key is missing
    fileonopen = open('namestorage.txt', 'w')
    fileonopen.write(' ')
    fileonopen.close()

    TripleMain.KeyboardIsOn = True

    def old_clear(self):
        deletion = 0
        while deletion < 30:
            self.DELETE_Key_Update()
            self.deletion += 1

    counter = 0

    def resetimername(self):
        Thread(target=self.CursorCheck).start()
        for i in range(30):
            self.DELETE_Key_Update()
        self.timer.text = "ENTER YOUR NAME: "
        self.keyboard_movement_update()

    def keyboard_movement_update(self):  # call to TripleMain?
        print('')
        # TripleMain.KeyboardIsOn = True

    def A_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.a1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def B_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.b1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def C_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.c1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def D_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.d1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def E_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.e1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def F_Key_Update(self):
        file = open('namestorage.txt', 'a')  #
        file.write(str(self.f1.text))
        file.close()
        self.display_name()

        self.counter += 1

    def G_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.g1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def H_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.h1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def I_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.i1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def J_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.j1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def K_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.k1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def L_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.l1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def M_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.m1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def N_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.n1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def O_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.o1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def P_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.p1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def Q_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.q1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def R_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.r1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def S_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.s1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def T_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.t1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def U_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.u1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def V_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.v1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def W_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.w1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def X_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.x1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def Y_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.y1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def Z_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.z1.text))
        file.close()
        self.display_name()
        self.counter += 1

    def SPACE_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.space.text))
        file.close()
        self.display_name()
        self.counter += 1

    def STAR_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.star.text))
        file.close()
        self.display_name()
        self.counter += 1

    def DASH_Key_Update(self):
        file = open('namestorage.txt', 'a')
        file.write(str(self.dash.text))
        file.close()
        self.display_name()
        self.counter += 1

    def ENTER_Key_Update(self):
        self.enterpressed = True
        if self.counter > 0:
            file = open('namestorage.txt', 'r')
            name = file.read()
            file.close()
            file = open('storage.txt', 'a')
            file.write(name)
            file.close()
            # Thread(target=self.reset_name).start()
            sleep(0.4)

            SCREEN_MANAGER.current = WAIT_SCREEN_NAME
        elif self.counter == 0:
            file = open('storage.txt', 'a')
            file.write(' Bob')
            file.close()
            sleep(0.4)
            SCREEN_MANAGER.current = WAIT_SCREEN_NAME

    def DELETE_Key_Update(self):  # this WORKS omg

        if self.counter > 0:
            with open('namestorage.txt', 'rb+') as f:
                f.seek(0, 2)  # end of file
                size = f.tell()  # the size...
                f.truncate(size - 1)  # truncate at that size - how ever many characters
                self.display_name()
                self.counter -= 1
            if self.counter < 0:
                self.counter = 0

    def display_name(self):
        file = open('namestorage.txt', 'r')
        name = file.read()
        file.close()
        self.timer.text = name

    def reset_name(self):
        self.timer.text = "ENTER YOUR NAME: "


class WaitScreen(Screen):
    def __init__(self, **kwargs):
        super(WaitScreen, self).__init__(**kwargs)

    first_place = ObjectProperty(None)
    loading = ObjectProperty(None)
    print("Before file")
    # lines = []
    # scores = []
    # names = []

    def score_update(self):
        scores = []
        names = []
        with open("storage.txt", "r") as file:
            for line in file:
                split_line = line.strip().split()
                scores.append(split_line[0])
                names.append(split_line[1])
        print("Scores:", scores)
        print("Names:", names)

        pairs = list(zip(scores, names))
        print("Pairs Before:", pairs)
        pairs.sort(key=lambda pair: int(pair[0]))
        print("Pairs After:", pairs)

        # string = ""
        # for element in pairs:
        #     string += element

        count =0
        score_board = ""
        while count < 10:
            score_board += pairs[count][0]+" " + pairs[count][1] + "\n"
            count+=1
        self.first_place.text= score_board



        # with open("storage.txt") as file_in:
        #     for line in file_in:
        #         self.lines.append(line)
        #
        # for line in self.lines:
        #     self.scores.append(line.split()[0])
        #     self.names.append(line.split()[1])
        #
        # print(self.scores)
        # print(self.names)
        # # converting to int
        # scoresint = []
        # for i in range(len(self.scores)):
        #     q = int(self.scores[i])
        #     scoresint.append(q)
        #
        # dict_scores_names = {}
        # for i in range(1,len(scoresint)):
        #     dict_scores_names[self.names[i]]=(scoresint[i])
        # print(dict_scores_names)



        # # firstplacefinder
        # # so we have scoresint, and scores. Find the min, remove it from both, and then find the next min inside a variable.
        #


        # leaderboardnames = []
        # leaderboardscores = []
        # for i in range(10):
        #     index = scoresint.index(min(scoresint))
        #     leadnames = self.names[index]
        #     leaderboardnames.append(leadnames)
        #     leadscores = self.scores[index]
        #     leaderboardscores.append(leadscores)
        #     del self.names[index]
        #     del scoresint[index]
        #     del self.scores[index]
        #
        #
        # print(leaderboardscores)
        # print(leaderboardnames)


        # for i in range(10):
        #     print(str(leaderboardnames[i]), 'with a score of ' + str(leaderboardscores[i]))
        #
        # leaderboardscores.clear()
        # leaderboardnames.clear()
        # # newstuff

        # temp_list_scores = []
        # for i in leaderboardscores:
        #     if i not in temp_list_scores:
        #         temp_list_scores.append(i)
        #
        # self.leaderboardscores = temp_list_scores
        #
        # temp_list_names = []
        # for i in leaderboardnames:
        #     if i not in temp_list_names:
        #         temp_list_names.append(i)
        #
        # self.leaderboardnames = temp_list_names
        Thread(target=self.switch_screen).start()

        # https://www.guru99.com/python-howto-remove-duplicates.html

    # delete dooplicate fiunction?
    def switch_screen(self):
        # self.names.clear()
        # self.scores.clear()
        # self.scoresint.clear()
        # self.leaderboardnames.clear()
        # self.leaderboardscores.clear()
        sleep(10)
        print("Switch screen")
        TripleMain.KinectIsOn = True
        SCREEN_MANAGER.current = TIMER_SCREEN_NAME


class TimerScreen(Screen):
    def __init__(self, **kwargs):
        super(TimerScreen, self).__init__(**kwargs)
        self.seconds = 0

    timer = ObjectProperty(None)

    # update the label of timer to be the seconds that have been passed

    def timer_label_update_thread(self):
        Thread(target=self.timer_label_update).start()

    def timer_label_update(self):

        self.timer.font_size = 150

        self.timer.text = "GET READY!"
        sleep(2)
        self.timer.text = "THREE"
        sleep(0.8)
        self.timer.text = "TWO"
        sleep(0.8)
        self.timer.text = "ONE"
        sleep(0.8)
        self.timer.text = "GO!!!"
        sleep(0.7)
        time_start = time.time()
        while True:
            seconds = int(time.time() - time_start)
            print(seconds, 'seconds passed')
            print('')
            self.timer.font_size = 400
            self.timer.text = str(seconds)
            sleep(1)
            if TripleMain.KinectIsOn == False:
                print("Seconds Passed:", seconds)
                file = open('storage.txt', 'a')
                file.write('\n' + str(seconds) + '')
                file.close()
                SCREEN_MANAGER.current = MAIN_SCREEN_NAME
                break


def everything_start():
    TripleMain.odrive_and_kinect_startup()


Builder.load_file('TimerScreen.kv')
Builder.load_file('main.kv')
Builder.load_file('WaitScreen.kv')
# Builder.load_file('Leaderboard.kv')
SCREEN_MANAGER.add_widget(TimerScreen(name=TIMER_SCREEN_NAME))
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(WaitScreen(name=WAIT_SCREEN_NAME))
# SCREEN_MANAGER.current = TIMER_SCREEN_NAME


if __name__ == '__main__':
    Thread(target=everything_start).start()
    KinectGUI().run()

# stackeeeeeexchange
# file = 'namestorage.txt'
# deleteeomthing___________(file, 1)#does this even work? #https://stackoverflow.com/questions/18857352/remove-very-last-character-in-file


# https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
