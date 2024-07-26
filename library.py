#built in
import os
import time
import math
import random
import string
import threading
import subprocess


# file_url = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/req.txt"

# response = requests.get(file_url)
# lines = response.text.split("\n")
# line_list = list(lines)
# line_list.pop()
# total_lines = len(line_list)

# for i in range(total_lines):
#     subprocess.run(["pip", "install", line_list[i], "-q"])
#     percent_installed = (i + 1) / total_lines * 100
#     print(f"Installing pip module {i+1}/{total_lines}. {percent_installed:.2f}% complete.", end='\r', flush=True)
import cv2
import json
import ctypes
import requests
import keyboard
import pyautogui
import bettercam
import numpy as np
import deep_translator
import win32api, win32con
from pypresence import Presence
from colorama import Fore, Style
from pystyle import Colors, Colorate
import ctypes
import locale

config_path = "config.json"
try:
    with open("config.json", "r") as file:
        pass
except FileNotFoundError:
    config = {
        "aimbot": True,
        "detection": True,
        "pinned": True,
        "shoot": True,
        "aimkey": "rmb",
        "trigkey": "rmb",
        "trigdelay": "50",
        "side": 1.0,
        "smoothness": 3.0,
        "fov": 3,
        "rpc": True,
        "always": False,
    }
    with open(config_path, "w") as configfile:
        json.dump(config, configfile)


try:
    windll = ctypes.windll.kernel32
    # windll.GetUserDefaultUILanguage()
    tranlanguage = ((locale.windows_locale[windll.GetUserDefaultUILanguage()]).split("_"))[0]
except Exception as e:
    print("Error getting language: " + str(e))
    tranlanguage = 'en'

def translate(text):
    if tranlanguage == 'en':
        return text
    else:
        try:
            translated = deep_translator.GoogleTranslator(source='auto', target=tranlanguage).translate(text)
            return translated
        except Exception as e:
            print("Error translating: " + str(e))
            return text
        
if tranlanguage != "en":
    print(translate("Translating to") + " " + translate(tranlanguage) + translate(". Please wait.."))


# start bettercam
camera = bettercam.create()

def checkhwid():
    hwidlisturl = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/ids.txt"
    hwidlist = str(requests.get(hwidlisturl).text)
    global hwid
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    if hwid == "":
        print("Error getting UserID, please contact support.")
        time.sleep(10)
        exit()
    if hwid in hwidlist:
        print("Your HWID is banned, you can make a case in our discord to be unbanned.")
        time.sleep(10)
        exit()
    else:
        pass

checkhwid()

# Get local version for info banner
with open("localv.json", "r") as file:
    data = json.load(file)
    local_version = data["version"]

# discord channel launches
launchesurl = 'https://aimrstats.folate-lathe-0d.workers.dev/'
try:
    response = requests.get(launchesurl)
except Exception as e:
    pass

# Launch counter
url = "https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Flocalhost%2FAIMr&count_bg=%23FF0000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Launches&edge_flat=false"
response = requests.get(url)

dailyurl = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/daily.txt"
dailyresponse = str(requests.get(dailyurl).text)

# randomize terminal/window title
def set_console_title():
    while True:
        randomchar = "AIMr " + local_version + " " + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        ctypes.windll.kernel32.SetConsoleTitleW(randomchar)
        time.sleep(0.1)

# start above thread
cstitle = threading.Thread(target=set_console_title)
cstitle.daemon = True  # Set the thread as a daemon thread
cstitle.start()

# # make text type out effect
# def typewriter(text,option):
#         for character in text:
#             sys.stdout.write(character)
#             sys.stdout.flush()
#             if option == "logo":
#                 time.sleep(0.01)
#             else:
#                 time.sleep(0.02)
#         if option == "input":
#             value = input()
#             return value

# add [AIMr] or [Question] to the text
import shutil
columns = shutil.get_terminal_size().columns
def AIMr(text, indent):
    text = translate(text)
    printable = (Colorate.Horizontal(Colors.purple_to_blue, "[AIMr] ") + text)
    if indent:
        printable = printable + "\n"
    return printable

logo_url = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/logo.txt"
response = requests.get(logo_url)
logo_text = response.text

# clear the terminal and add banner

def clearfig():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.purple_to_blue, logo_text.rstrip(), 1))
    print(AIMr("Welcome to AIMr" + " [" +  local_version + "]", False))
    print(AIMr("Join the discord: discord.gg/AIMr", False))
    print(AIMr("User ID: " + hwid, False))
    print(AIMr("Daily: " + dailyresponse, False))

def is_button_pressed(button):
    special_buttons = ['lmb', 'mmb', 'rmb', 'smb', 'smb2']

    if button.lower() in special_buttons:
        # Check for special mouse buttons
        mouse_buttons = {'lmb': 0x01, 'mmb': 0x04, 'rmb': 0x02, 'smb': 0x05, 'smb2': 0x06}
        button_code = mouse_buttons.get(button.lower(), 0)
        if button_code:
            key_state = ctypes.windll.user32.GetKeyState(button_code)
            return ((key_state & 0x8000) != 0)
        else:
            print(f"Unknown mouse button: {button}")
            return False
    else:
        return keyboard.is_pressed(button)

# main loop
try:
    # # loading screen
    # os.system('cls' if os.name == 'nt' else 'clear')

    # typewriter(AIMr(questions(4), True), "print")

    # result = pyfiglet.figlet_format("A I M r", font="larry3d")
    # typewriter("\u001b[35m" + result.rstrip() + "\u001b[0m \n", "logo")
    # typewriter("\n" + AIMr(questions(5), True), "print")

    # time.sleep(1)

    # import model
    CONFIG_FILE = './yolo.cfg'
    WEIGHT_FILE = './yolo.weights'

    clearfig()

    config = False

    # get config
    with open("config.json", "r") as config_file:
        global config_data
        config_data = json.load(config_file)

    option = config_data["aimbot"]

    rpc = config_data["rpc"]

    if rpc:
        client_id = '1200859106345492492'
        rpcid = Presence(client_id)
        try:
            rpcid.connect()
            # Set the initial presence
            rpcid.update(
                details="An AI Aimbot",
                large_image="aimr_icon",
                large_text="discord.gg/AIMr",
                buttons=[
                    {"label": "Download", "url": "https://github.com/ai-aimbot/AIMr"},
                ],
                start=int(time.time())
            )
        except Exception:
            pass
        except KeyboardInterrupt:
            pass


    if option:
        

        show_frame = config_data["detection"]

        # if you have cuda it will use it
        net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHT_FILE)

        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            # CUDA is enabled
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
        else:
            # CUDA is not enabled
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        ln = net.getLayerNames()
        ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

        locked_box = None
        frames_without_detection = 0
        max_frames_without_detection = 10


        # setting config
        if show_frame:
            floating = config_data["pinned"]
        else:
            floating = False

        shoot = config_data["shoot"]


        key = config_data["aimkey"]


        placement_side = config_data["side"]
        if placement_side == 1:
            placement_side = "Left"
        elif placement_side == 2:
            placement_side = "None"
        elif placement_side == 3:
            placement_side = "Right"

        smoothness = config_data["smoothness"]

        smoothness = int(smoothness)

        # I have that I have to do this but the old implementation kept throwing errors
        fovnum = int(config_data["fov"])
        if fovnum == 1:
            square_size = 250
        elif fovnum == 2:
            square_size = 280
        elif fovnum == 3:
            square_size = 310
        elif fovnum == 4:
            square_size = 340
        elif fovnum == 5:
            square_size = 370
        elif fovnum == 6:
            square_size = 410
        elif fovnum == 7:
            square_size = 440
        elif fovnum == 8:
            square_size = 470
        elif fovnum == 9:
            square_size = 500
        elif fovnum == 10:
            square_size = 540

        # # mouse movement function
        # def movement_thread_func(x, y):
        #     headshot = 30
        #     steps = smoothness
        #     # formula = int(delta_x), int(delta_y)
        #     formula = int(x), int((y/1.2)+headshot)
        #     moveX, moveY = int(formula[0]/steps), int(formula[1]/steps)

        #     for i in range(steps):
        #         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, moveX, moveY, 0, 0)

        #     if shoot:
        #         # shoot if config says to
        #         shooting_thread = threading.Thread(target=shooting_thread_func)
        #         shooting_thread.start()


        # def movement(x, y):
        #     movement_thread = threading.Thread(target=movement_thread_func, args=(x, y))
        #     movement_thread.start()

        def shooting_thread_func():
            # Shoot
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # running text
        print(AIMr("RPC: " + str(rpc), False))
        print(AIMr("Detection Window: " + str(show_frame), False))
        if show_frame:
            print(AIMr("Pinned GUI: "  + str(floating), False))
        if shoot:
            print(AIMr("Shoot: " + str(shoot), False))
        if not config_data["always"]:
            print(AIMr("Aim/Shoot Key: " + str(key), False))
        else:
            print(AIMr("Aim/Shoot Key: " + "Always", False))
        print(AIMr("Block Side: "  + str(placement_side), False))
        print(AIMr("Smoothness: " + str(smoothness), False))
        print(AIMr("FOV: "  + str(fovnum), False))
        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            print(AIMr("CUDA: DISABLED - Slower | There is a guide in our discord on how to enable", False))
        else:
            print(AIMr("ENABLED - Faster", False))
        print(AIMr("Ready...", False))
        
        # Get image of screen
        screen_size = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        region = 0, 0, screen_size[0], screen_size[1]

        # square_size = round(250 + (30 * int(config_data["fov"])), -1)
        left, top = (region[2] - square_size) // 2, (region[3] - square_size) // 2
        right, bottom = left + square_size, top + square_size
        region = (left, top, right, bottom)
        frame_width, frame_height = square_size, square_size

        # block area settings
        if placement_side == "Left":
            # Rectangle on the left side
            rect_size_y = int(round(square_size * 4/5.4))
            rect_size_x = int(round(square_size * 2/5.4))
            rect_color = (0, 0, 0)
            rect_x = 0  # Left side
            rect_y = square_size - rect_size_y
        elif placement_side == "Right":
            # Rectangle on the right side
            rect_size_y = int(round(square_size * 2.5/5.4))
            rect_size_x = int(round(square_size * 1.5/5.4))
            rect_color = (0, 0, 0)
            rect_x = square_size - rect_size_x  # Right side
            rect_y = square_size - rect_size_y
        elif placement_side == "None":
            # Rectangle on the right side
            rect_size_y = 0
            rect_size_x = 0
            rect_color = (0, 0, 0)
            rect_x = square_size - rect_size_x  # Right side
            rect_y = square_size - rect_size_y
        else:
            exit(1)

        window_title = "AIMr Detections"

        while True:

            # detection loop/start timer for fps counter
            start_time = time.perf_counter()


            frame =  camera.grab(region=region)
            # 6ms

            # make sure its actually a frame (necessary)
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_size_x, rect_y + rect_size_y), rect_color, -1)

                # Detection loop
                blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (square_size, square_size), crop=True)
                net.setInput(blob)
                layerOutputs = net.forward(ln)
                #9ms

                boxes = []
                confidences = []

                # i barely understand, you can change confidences here
                
                for output in layerOutputs:
                    for detection in output:
                        scores = detection[5:]
                        classID = np.argmax(scores)
                        confidence = scores[classID]
                        if confidence > 0.1 and classID == 0:
                            box = detection[:4] * np.array([square_size, square_size, square_size, square_size])
                            (centerX, centerY, width, height) = box.astype("int")
                            x = int(centerX - (width / 2))
                            y = int(centerY - (height / 2))
                            box = [x, y, int(width), int(height)]
                            boxes.append(box)
                            confidences.append(float(confidence))

                # and here
                indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)
                #3ms

                # incase of pause in detection keep moving towards the last known enemy
                if locked_box is not None:
                    if locked_box not in boxes:
                        frames_without_detection += 1
                        if frames_without_detection >= max_frames_without_detection:
                            locked_box = None
                    else:
                        frames_without_detection = 0


                if locked_box is None:
                    if len(indices) > 0:
                        # print(f"Detected: {len(indices)}")
                        center_x = square_size // 2
                        center_y = square_size // 2

                        min_dist = float('inf')
                        for i in indices.flatten():
                            (x, y) = (boxes[i][0], boxes[i][1])
                            (w, h) = (boxes[i][2], boxes[i][3])

                            dist = math.sqrt(math.pow(center_x - (x + w / 2), 2) + math.pow(center_y - (y + h / 2), 2))
                            if dist < min_dist:
                                min_dist = dist
                                locked_box = boxes[i]

                
                if not config_data["always"]:
                    # find relative mouse movements
                    if locked_box is not None and is_button_pressed(key):
                        x = int(locked_box[0] + locked_box[2] / 2 - frame_width / 2)
                        y = int(locked_box[1] + locked_box[3] / 2 - frame_height / 2) - locked_box[3] * 0.5  # For head shot
                        headshot = 30
                        steps = smoothness
                        # formula = int(delta_x), int(delta_y)
                        formula = int(x), int((y/1.2)+headshot)
                        moveX, moveY = int(formula[0]/steps), int(formula[1]/steps)

                        for i in range(steps):
                            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, moveX, moveY, 0, 0)

                        if shoot:
                            # shoot if config says to
                            shooting_thread = threading.Thread(target=shooting_thread_func)
                            shooting_thread.start()

                else:
                    if locked_box is not None:
                        x = int(locked_box[0] + locked_box[2] / 2 - frame_width / 2)
                        y = int(locked_box[1] + locked_box[3] / 2 - frame_height / 2) - locked_box[3] * 0.5  # For head shot
                        headshot = 30
                        steps = smoothness
                        # formula = int(delta_x), int(delta_y)
                        formula = int(x), int((y/1.2)+headshot)
                        moveX, moveY = int(formula[0]/steps), int(formula[1]/steps)

                        for i in range(steps):
                            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, moveX, moveY, 0, 0)

                        if shoot:
                            # shoot if config says to
                            shooting_thread = threading.Thread(target=shooting_thread_func)
                            shooting_thread.start()


                # add drawings to detection window
                for i, box in enumerate(boxes):
                    (x, y, w, h) = box
                    if box == locked_box:
                        color = (0, 255, 0)  # Green color for locked box
                    else:
                        color = (255, 255, 255)
                    if show_frame:
                        cv2.circle(frame, (int(x + w / 2), int(y + h / 5)), 5, (0, 0, 255), -1) #draw target dot
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2) # bounding box

                        # Draw line from head to center of the frame
                        cv2.line(frame, (x + w // 2, y + h // 5), (square_size // 2, square_size // 2), (0, 0, 255), 2)

                        # Display confidence percentage above the box
                        confidence_text = f'{confidences[i] * 100:.2f}%'
                        text_width, text_height = cv2.getTextSize(confidence_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
                        cv2.putText(frame, confidence_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

                if show_frame:
                    if floating:
                        # pin window
                        cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
                        cv2.setWindowProperty(window_title, cv2.WND_PROP_TOPMOST, 1)
                    # show window
                    cv2.putText(frame, f"FPS: {int(1/(time.perf_counter() - start_time))}", (5, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (113, 116, 244), 2)
                    cv2.imshow("AIMr Detections", frame)
                    cv2.waitKey(1)
                #15ms

    else:
        # get config data
        key = config_data["trigkey"]
        delay = int(config_data["trigdelay"])
        # running text
        print(AIMr("RPC: " + str(rpc), False))
        print(AIMr("Triggerbot key: " + str(key), False))
        print(AIMr("Triggerbot delay: " + str(delay), False))
        print(AIMr("Hold " + key + " for it to shoot when it notices changes.", False))
        print(AIMr("Ready...", False))

        while True:
            # triggerbot loop
            time.sleep(0.010)
            if is_button_pressed(key):
                og_pixel_color = pyautogui.pixel(965, 538)
                pixel_color = pyautogui.pixel(965, 538)
                if abs(sum(pixel_color) - sum(og_pixel_color)) > 0.05 * sum(og_pixel_color):  # Change the condition based on the desired color
                    time.sleep((delay)/1000)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

except KeyboardInterrupt:
    if rpc:
        try:
            rpc.clear()
        except Exception:
            pass

    # to exit
    clearfig()
    print(AIMr("Exiting... Goodbye!", False))
    time.sleep(1)
    exit()

except Exception as e:
    print(f"An error occurred: {e}")
    # Wait for 15 seconds before closing
    time.sleep(15)