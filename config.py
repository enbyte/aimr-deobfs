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
from io import BytesIO
from customtkinter import *
from CTkColorPicker import *
from pynput import keyboard, mouse
import deep_translator
from PIL import Image
import customtkinter
import subprocess
import webbrowser
import CTkToolTip
import pyperclip
import requests
import ctypes
import time
import json
import os
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





# Grab the image from the URL
response = requests.get("https://img.icons8.com/wired/64/FFFFFF/paint.png")
paintimg = Image.open(BytesIO(response.content))

# Grab the image from the URL
response = requests.get("https://img.icons8.com/ios-filled/50/FFFFFF/gears.png")
setconfigimg = Image.open(BytesIO(response.content))

# Grab the image from the URL
response = requests.get("https://img.icons8.com/ios/50/FFFFFF/clipboard.png")
copyconfigimg = Image.open(BytesIO(response.content))

# Grab the image from the URL
response = requests.get("https://i.postimg.cc/Fzs4YjFL/Untitled.png")
skullimg = Image.open(BytesIO(response.content))

# Grab the image from the URL
response = requests.get("https://img.icons8.com/ios-filled/50/FFFFFF/discord-logo.png")
discordimg = Image.open(BytesIO(response.content))

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

os.system("cls")
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("theme.json")
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
with open("localv.json", "r") as file:
    data8 = json.load(file)
    version = data8["version"]
app.title("AIMr " + version)
app.iconbitmap("AIMr.ico")
# app.attributes("-topmost", True)
padding = 10
app.resizable(False, False)


with open("config.json", "r") as config_file:
    global config_data
    config_data = json.load(config_file)

try:

    currentverurl = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/current_version.txt"
    currentverresponse = str(requests.get(currentverurl).text)

    changelogurl = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/changelog.txt"
    changelogresponse = currentverresponse + "Changelog: \n" + str(requests.get(changelogurl).text)

    config_file = "config.json"

    # with open("localv.json", "r") as file:
    #     data8 = json.load(file)
    #     language = data8["language"]

    # # Read the lang.json file
    # with open("lang.json", "r", encoding='utf-8') as file:
    #     data5 = json.load(file)
    #     # Modify the English field in the answer field
    #     useranswer = data5["language"].get(language, {}).get("answers", {}).get("1", "")

    # def questions(list):
    #     with open("lang.json", "r", encoding='utf-8') as file:
    #         question = json.load(file)
    #     text = question["language"][language]["text"]
    #     text = text[list]
    #     return text

    # def toggle_window():
    #     if app.state() == "withdrawn":
    #         app.deiconify()
    #     else:
    #         app.state("withdrawn")

    # guikeyentry = customtkinter.CTkEntry(aimtab, placeholder_text=questions(0), width=240)
    # guikeyentry.pack(pady=padding, padx=padding, anchor="w")

    # def guikeyfunc():
    #     key = guikeyentry.get()
    #     data = {"gui_key": key}
    #     with open("config.json", "r+") as file:
    #         data = json.load(file)
    #         data["gui_key"] = key
    #         file.seek(0)
    #         json.dump(data, file)
    #         file.truncate()
    #     print("Set gui key")
    #     guikeyentry.delete(0, 'end')  # Clear the guikey entry

    # guikeybutton = customtkinter.CTkButton(aimtab, text=questions(1), command=guikeyfunc)
    # guikeybutton.pack(pady=padding, padx=padding, anchor="w")

    # def get_gui_key():
    #     try:
    #         with open("config.json", "r") as file:
    #             data = json.load(file)
    #             return data.get("gui_key", "")
    #         # If key is not found, do something
    #     except:
    #         with open("config.json", "w") as file:
    #             data = {"gui_key": "o"}
    #             json.dump(data, file)
    #         print("Set gui key")
    #         return "o"

    # keyboard.on_press_key(get_gui_key(), lambda _: toggle_window())

    def replace_string_in_json(string1, string2):
        file_path = "theme.json"
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Recursively replace string1 with string2 in the JSON data
        def recursive_replace(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = recursive_replace(value)
            elif isinstance(obj, list):
                for i in range(len(obj)):
                    obj[i] = recursive_replace(obj[i])
            elif isinstance(obj, str):
                obj = obj.replace(string1, string2)
            return obj

        # Update the data with the replaced strings
        data = recursive_replace(data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def runaimrmain():
        CTk.destroy(app)
        print("Loading AIMr...")
        subprocess.run(["python", "library.py"])

    with open("theme.json", "r") as file:
            theme_data = json.load(file)

    hover_color = theme_data["AIMrconfig"]["hover_color"]
    fg_color = theme_data["AIMrconfig"]["fg_color"]



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

    if config_data["aimbot"]:
        runaimrbutton = customtkinter.CTkButton(app, text=translate("Start AI Aimbot"), command=runaimrmain, fg_color=hover_color, hover_color=fg_color, image=CTkImage(dark_image=skullimg))
        runaimrbutton.pack(pady=padding, padx=padding, anchor="center")
        CTkToolTip.CTkToolTip(runaimrbutton, message="Press this button and it will start the AI aimbot.")
    else:
        runaimrbutton = customtkinter.CTkButton(app, text=translate("Start Triggerbot"), command=runaimrmain, fg_color=hover_color, hover_color=fg_color, image=CTkImage(dark_image=skullimg))
        runaimrbutton.pack(pady=padding, padx=padding, anchor="center")
        CTkToolTip.CTkToolTip(runaimrbutton, message="Press this button and it will start the triggerbot.")

    tabview = CTkTabview(master=app)
    tabview.pack(padx=20)

    faqtab = tabview.add(translate("FAQ"))
    sharingtab = tabview.add(translate("Configs"))
    generaltab = tabview.add(translate("General"))
    aimtab = tabview.add(translate("Aimbot"))
    trigtab = tabview.add(translate("Triggerbot"))


    # def faqimagefunc():
    #     # Grab the image from the URL
    #     response = requests.get("https://camo.githubusercontent.com/3e892790bb938387d19c34f37e7ea07ebc6cb92c37b7edf68a7d4e3ca3fc24d0/68747470733a2f2f692e696d6775722e636f6d2f67376d4e476b572e706e67")
    #     faqimg = Image.open(BytesIO(response.content))

    #     faqimage = customtkinter.CTkImage(dark_image=faqimg, size=(646, 557))

    #     toplevel = CTkToplevel(app)
    #     toplevel.title("Example")
    #     faq_button = customtkinter.CTkButton(toplevel, corner_radius=15, text="", fg_color="transparent", bg_color="transparent", hover=False, image=faqimage)
    #     faq_button.pack(pady=padding, padx=padding, anchor="center")

    # faqimagebutton = customtkinter.CTkButton(faqtab, text="See Example", command=faqimagefunc)
    # faqimagebutton.pack(pady=padding, padx=padding, anchor="center")

    changeloglabel = customtkinter.CTkLabel(faqtab, text=translate(changelogresponse), fg_color="transparent", anchor="w", justify="left")
    changeloglabel.pack(pady=padding, padx=padding, anchor="w")

    def ask_color():
        pick_color = AskColor() # open the color picker
        color = pick_color.get() # get the color string
        hex_color = color
        factor = 0.6
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        # Darken the color by applying the factor to each RGB component
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)

        # Ensure values are within the valid RGB range (0-255)
        r = min(max(r, 0), 255)
        g = min(max(g, 0), 255)
        b = min(max(b, 0), 255)

        # Convert back to hex
        darkened_hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        # Read the theme.json file
        with open("theme.json", "r") as file:
            theme_data = json.load(file)

        # Get the values of fg_color and hover_color under aimrconfig
        fg_color = theme_data["AIMrconfig"]["fg_color"]
        hover_color = theme_data["AIMrconfig"]["hover_color"]
        replace_string_in_json(fg_color, hex_color)
        replace_string_in_json(hover_color, darkened_hex_color)

    informationlabel = customtkinter.CTkLabel(faqtab, text=translate("If you have issues with the config being wrong \n try and turn the switch off and on, or re-enter an option."), fg_color="transparent")
    informationlabel.pack(pady=padding, padx=padding, anchor="center")

    def discordfunc():
        webbrowser.open("https://discord.gg/AIMr")

    discordbutton = customtkinter.CTkButton(faqtab, text=translate("Join the discord!"), command=discordfunc, image=CTkImage(dark_image=discordimg), fg_color="#454FBF", hover_color="#1e2357")
    discordbutton.pack(pady=padding, padx=padding, anchor="center")
    CTkToolTip.CTkToolTip(discordbutton, message=translate("Press this button and it will open our discord link."))

    optionlabel = customtkinter.CTkLabel(generaltab, text=translate("Pick an option:"), fg_color="transparent")
    optionlabel.pack(padx=padding, anchor="w")

    def optionmenu_callback(choice):
        if choice == "Aimbot":
            option = True
            runaimrbutton.configure(text=translate("Start AI Aimbot"))
        else:
            option = False
            runaimrbutton.configure(text=translate("Start Triggerbot"))
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["aimbot"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    optionmenu = customtkinter.CTkOptionMenu(generaltab, values=[translate("Aimbot"), translate("Triggerbot")], command=optionmenu_callback)
    optionmenu.set("Aimbot")
    optionmenu.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(optionmenu, message=translate("This dropdown decides if you use our ai aimbot or triggerbot."))
    if config_data["aimbot"]:
        optionmenu.set(translate("Aimbot"))
    else:
        optionmenu.set(translate("Triggerbot"))


    def rpcfunc():
        option = rpcswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["rpc"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want aimbot or a triggerbot? (1/2):"
    rpcvar = customtkinter.StringVar(value="")
    rpcswitch = customtkinter.CTkSwitch(generaltab, text=translate("Do you want Discord RPC?"), command=rpcfunc, variable=rpcvar, onvalue=True, offvalue=False)
    rpcswitch.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(rpcswitch, message=translate("This decides if you want if to show on discord that you are using AIMr."))
    if config_data["rpc"]:
        rpcswitch.select()
    else:
        rpcswitch.deselect()

    presetlabel = customtkinter.CTkLabel(sharingtab, text=translate("Config Presets (changes will not show in gui until restart):"), fg_color="transparent")
    presetlabel.pack(padx=padding, anchor="w")

    def universalconfig():
        config = '{"aimbot": true, "detection": true, "pinned": true, "shoot": true, "aimkey": "rmb", "trigkey": "rmb", "trigdelay": "50", "side": 2.0, "smoothness": 3.0, "fov": 3.0, "rpc": true, "always": false}'
        with open("config.json", "w") as file:
            data = json.loads(config)
            json.dump(data, file)
    
    def cs2config():
        config = '{"aimbot": true, "detection": false, "pinned": false, "shoot": true, "aimkey": "rmb", "trigkey": "rmb", "trigdelay": "50", "side": 3.0, "smoothness": 1.0, "fov": 1.0, "rpc": true, "always": false}'
        with open("config.json", "w") as file:
            data = json.loads(config)
            json.dump(data, file)

    def fortniteconfig():
        config = '{"aimbot": true, "detection": false, "pinned": false, "shoot": true, "aimkey": "rmb", "trigkey": "rmb", "trigdelay": "50", "side": 1.0, "smoothness": 1.0, "fov": 1.0, "rpc": true, "always": false}'
        with open("config.json", "w") as file:
            data = json.loads(config)
            json.dump(data, file)
    
    def bestconfig():
        config = '{"aimbot": true, "detection": false, "pinned": false, "shoot": true, "aimkey": "rmb", "trigkey": "rmb", "trigdelay": "50", "side": 2.0, "smoothness": 1.0, "fov": 1.0, "rpc": true, "always": false}'
        with open("config.json", "w") as file:
            data = json.loads(config)
            json.dump(data, file)

    configinputset = customtkinter.CTkButton(master=sharingtab, text=translate("BEST"), command=bestconfig)
    configinputset.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(configinputset, message=translate("Press this button and it will apply the BEST AND FASTEST config."))

    configinputset = customtkinter.CTkButton(master=sharingtab, text=translate("Universal"), command=universalconfig)
    configinputset.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(configinputset, message=translate("Press this button and it will apply the universal config."))

    configinputset = customtkinter.CTkButton(master=sharingtab, text=translate("Fortnite"), command=fortniteconfig)
    configinputset.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(configinputset, message=translate("Press this button and it will apply the fortnite config."))

    configinputset = customtkinter.CTkButton(master=sharingtab, text=translate("CS2"), command=cs2config)
    configinputset.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(configinputset, message=translate("Press this button and it will apply the CS2 config."))


    configsharelabel = customtkinter.CTkLabel(sharingtab, text=translate("Share or import configs:"), fg_color="transparent")
    configsharelabel.pack(pady=padding, padx=padding, anchor="w")

    configinput = customtkinter.CTkEntry(master=sharingtab, placeholder_text=translate("Enter the config here"), width=300)
    configinput.pack(pady=padding, padx=padding, anchor="w")

    def inputconfig():
        config = configinput.get()
        if config is not None and len(config) > 5:
            with open("config.json", "w") as file:
                data = json.loads(config)
                json.dump(data, file)
            configinput.delete(0, 'end')

    configinputset = customtkinter.CTkButton(master=sharingtab, text=translate("Set Config"), command=inputconfig, image=CTkImage(dark_image=setconfigimg))
    configinputset.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(configinputset, message=translate("Press this button and it will apply the config you pasted into the box above."))

    def copyconfig():
        with open("config.json", "r") as file:
            data = json.load(file)
            # Copy the data to the clipboard
            pyperclip.copy(str(data).lower().replace("'", "\""))

    copyconfigbutton = customtkinter.CTkButton(master=sharingtab, text=translate("Copy Config"), command=copyconfig, image=CTkImage(dark_image=copyconfigimg))
    copyconfigbutton.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(copyconfigbutton, message=translate("Press this button and it will copy your current config to your clipboard."))

    colorbutton = customtkinter.CTkButton(master=generaltab, text=translate("Change GUI Colors (Restart to set)"), command=ask_color, image=CTkImage(dark_image=paintimg))
    colorbutton.pack(padx=padding, pady=padding, anchor="w")
    CTkToolTip.CTkToolTip(colorbutton, message=translate("Press this button and it will let you pick the gui colors."))

    def detection():
        option = detectionswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["detection"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want it to shoot? (y/n):"
    detectionvar = customtkinter.StringVar(value="on")
    detectionswitch = customtkinter.CTkSwitch(aimtab, text=translate("Do you want a detection window? (SLOWER)"), variable=detectionvar,command=detection, onvalue=True, offvalue=False)
    detectionswitch.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(detectionswitch, message=translate("This switch decides if you want to see the AI detections in a separate window, at the cost of performance."))
    if config_data["detection"]:
        detectionswitch.select()
    else:
        detectionswitch.deselect()

    def pinned():
        option = pinnedswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["pinned"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want the detection window to be pinned on top? (y/n):"
    pinnedvar = customtkinter.StringVar(value="on")
    pinnedswitch = customtkinter.CTkSwitch(aimtab, text=translate("Do you want the detection window to be pinned on top?"), variable=pinnedvar, command=pinned, onvalue=True, offvalue=False)
    pinnedswitch.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(pinnedswitch, message=translate("This decides if you want the detection window to be pinned over the game (windowed fullscreen/borderless)."))
    if config_data["pinned"]:
        pinnedswitch.select()
    else:
        pinnedswitch.deselect()


    def shoot():
        option = shootswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["shoot"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want it to shoot? (y/n):"
    shootvar = customtkinter.StringVar(value="on")
    shootswitch = customtkinter.CTkSwitch(aimtab, text=translate("Do you want it to shoot?"), variable=shootvar,command=shoot, onvalue=True, offvalue=False)
    shootswitch.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(shootswitch, message=translate("This decides if you want the aimbot to shoot or just aim."))
    if config_data["shoot"]:
        shootswitch.select()
    else:
        shootswitch.deselect()

    def alwaysfunc():
        option = alwaysswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["always"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want aimbot or a triggerbot? (1/2):"
    alwaysvar = customtkinter.StringVar(value="")
    alwaysswitch = customtkinter.CTkSwitch(aimtab, text=translate("Do you want it to be always on? (DANGEROUS)"), command=alwaysfunc, variable=alwaysvar, onvalue=True, offvalue=False)
    alwaysswitch.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(alwaysswitch, message=translate("This decides if you want the aimbot to always be on so you don't have to hold any keys (DANGEROUS)."))
    if config_data["always"]:
        alwaysswitch.select()
    else:
        alwaysswitch.deselect()

    class KeyLoggerApp:
        def __init__(self, master):
            self.master = master
            with open("config.json", "r") as file:
                config_data = json.load(file)
                initial_aimkey = config_data.get("aimkey")

            self.start_button = customtkinter.CTkButton(master, text=f" {initial_aimkey.upper()} ", command=self.start_listening)
            self.start_button.pack(pady=padding, padx=padding, anchor="w")
            CTkToolTip.CTkToolTip(self.start_button, message=translate("Press this button then press the mousebutton/key you want to use to aim/shoot."))

            self.listener = None
            self.mouse_listener = None
            self.mouse_listener_active = False
            self.mouse_button_map = {
                mouse.Button.left: 'LMB',
                mouse.Button.middle: 'MMB',
                mouse.Button.right: 'RMB',
                mouse.Button.x1: 'SMB',
                mouse.Button.x2: 'SMB2'
            }

        def start_listening(self):
            with open("config.json", "r") as file:
                config_data = json.load(file)
                initial_aimkey = config_data.get("aimkey", "[...]")
            if self.listener is not None:
                self.listener.stop()

            if self.mouse_listener is not None:
                self.mouse_listener.stop()

            self.start_button.configure(state=customtkinter.DISABLED)
            self.start_button.configure(text=f"> {initial_aimkey.upper()} <")

            self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
            self.listener.start()

            self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
            self.mouse_listener.start()
            self.mouse_listener_active = True

        def on_key_press(self, key):
            try:
                key_value = key.char
            except AttributeError:
                key_value = key.name

            self.start_button.configure(text=f" {key_value.upper()} ")
            self.update_config_aimkey(key_value)
            self.stop_listening()

        def on_key_release(self, key):
            if key == keyboard.Key.esc:
                self.stop_listening()

        def on_mouse_click(self, x, y, button, pressed):
            if pressed and button in self.mouse_button_map:
                button_value = self.mouse_button_map[button]
                self.start_button.configure(text=f" {button_value.upper()} ")  # Обновляем текст кнопки
                self.update_config_aimkey(button_value)
                if self.mouse_listener_active:
                    self.stop_listening()

        def stop_listening(self):
            if self.listener is not None:
                self.listener.stop()
            if self.mouse_listener_active:
                self.mouse_listener.stop()
                self.mouse_listener_active = False
            self.start_button.configure(state=customtkinter.NORMAL)

        def update_config_aimkey(self, aimkey):
            with open("config.json", "r+") as file:
                data = json.load(file)
                data["aimkey"] = aimkey
                file.seek(0)
                json.dump(data, file)
                file.truncate()

    key_logger_app = KeyLoggerApp(tabview.tab(translate("Aimbot")))

    # # # Create a switch for "Press the key you want to use to aim:"
    # aimkeyentry = customtkinter.CTkEntry(aimtab, placeholder_text=questions(5), width=190)
    # aimkeyentry.pack(pady=padding, padx=padding, anchor="w")

    # def aimkeyfunc():
    #     key2 = aimkeyentry.get()
    #     data2 = {"gui_key": key2}
    #     with open("config.json", "r+") as file:
    #         data2 = json.load(file)
    #         data2["aimkey"] = key2
    #         file.seek(0)
    #         json.dump(data2, file)
    #         file.truncate()
    #     aimkeyentry.delete(0, 'end')  # Clear the guikey entry

    # aimkeybutton = customtkinter.CTkButton(aimtab, text=questions(10), command=aimkeyfunc)
    # aimkeybutton.pack(pady=padding, padx=padding, anchor="w")

    sidelabel = customtkinter.CTkLabel(aimtab, text=translate("Pick a block option:"), fg_color="transparent")
    sidelabel.pack(padx=padding, anchor="w")

    def sidemenu_callback(choice):
        if choice == translate("Left (fn)"):
            key2 = 1.0
        elif choice == translate("Right"):
            key2 = 3.0
        elif choice == translate("None"):
            key2 = 2.0
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["side"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    sidemenu = customtkinter.CTkOptionMenu(aimtab, values=[translate("Left (fn)"), translate("Right"), translate("None")], command=sidemenu_callback)
    sidemenu.set("None")
    sidemenu.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(sidemenu, message=translate("This decides what block you want to use, for example in fortnite \n its third person so it would detect yourself without using left block."))
    if config_data["side"] == 1.0:
        sidemenu.set(translate("Left (fn)"))
    elif config_data["side"] == 2.0:
        sidemenu.set(translate("None"))
    elif config_data["side"] == 3.0:
        sidemenu.set(translate("Right"))

    # Create a switch for "Smoothness? (1-10):"
    def slider_event(value):
        key2 = value
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["smoothness"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    sliderlabel = customtkinter.CTkLabel(aimtab, text=translate("Smoothness (1-10)"), fg_color="transparent")
    sliderlabel.pack(pady=padding, padx=padding, anchor="w")
    smoothslider = customtkinter.CTkSlider(aimtab, from_=1, to=10,number_of_steps=9, command=slider_event)
    smoothslider.pack(pady=padding, padx=padding, anchor="w")
    smoothslider.set(config_data["smoothness"])
    CTkToolTip.CTkToolTip(smoothslider, message=translate("This decides how smooth you want the aim to be."))

    # Create a switch for "Smoothness? (1-10):"
    def fov_event(value):
        key2 = value
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["fov"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    fovlabel = customtkinter.CTkLabel(aimtab, text=translate("What fov do you want (higher is slower)?"), fg_color="transparent")
    fovlabel.pack(pady=padding, padx=padding, anchor="w")
    fovslider = customtkinter.CTkSlider(aimtab, from_=1, to=10,number_of_steps=9, command=fov_event)
    fovslider.pack(pady=padding, padx=padding, anchor="w")
    fovslider.set(config_data["fov"])
    CTkToolTip.CTkToolTip(fovslider, message=translate("This decides how large you want the ai's fov to be, higher is much slower."))


    # # Create a switch for "Enter the key you want to use to activate the triggerbot:"
    # trigkeyentry = customtkinter.CTkEntry(trigtab, placeholder_text=questions(8), width=290)
    # trigkeyentry.pack(pady=padding, padx=padding, anchor="w")

    # def trigkeyfunc():
    #     key2 = trigkeyentry.get()
    #     with open("config.json", "r+") as file:
    #         data2 = json.load(file)
    #         data2["trigkey"] = key2
    #         file.seek(0)
    #         json.dump(data2, file)
    #         file.truncate()
    #     trigkeyentry.delete(0, 'end')  # Clear the guikey entry

    # trigkeybutton = customtkinter.CTkButton(trigtab, text=questions(10), command=trigkeyfunc, image=CTkImage(dark_image=setconfigimg))
    # trigkeybutton.pack(pady=padding, padx=padding, anchor="w")

    class KeyLoggerApp:
        def __init__(self, master):
            self.master = master
            with open("config.json", "r") as file:
                config_data = json.load(file)
                initial_aimkey = config_data.get("trigkey")

            self.start_button = customtkinter.CTkButton(master, text=f" {initial_aimkey.upper()} ", command=self.start_listening)
            self.start_button.pack(pady=padding, padx=padding, anchor="w")
            CTkToolTip.CTkToolTip(self.start_button, message=translate("Press this button then press the mousebutton/key you want to hold for the triggerbot to be active."))

            self.listener = None
            self.mouse_listener = None
            self.mouse_listener_active = False
            self.mouse_button_map = {
                mouse.Button.left: 'LMB',
                mouse.Button.middle: 'MMB',
                mouse.Button.right: 'RMB',
                mouse.Button.x1: 'SMB',
                mouse.Button.x2: 'SMB2'
            }

        def start_listening(self):
            with open("config.json", "r") as file:
                config_data = json.load(file)
                initial_aimkey = config_data.get("trigkey", "[...]")
            if self.listener is not None:
                self.listener.stop()

            if self.mouse_listener is not None:
                self.mouse_listener.stop()

            self.start_button.configure(state=customtkinter.DISABLED)
            self.start_button.configure(text=f"> {initial_aimkey.upper()} <")

            self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
            self.listener.start()

            self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
            self.mouse_listener.start()
            self.mouse_listener_active = True

        def on_key_press(self, key):
            try:
                key_value = key.char
            except AttributeError:
                key_value = key.name

            self.start_button.configure(text=f" {key_value.upper()} ")
            self.update_config_aimkey(key_value)
            self.stop_listening()

        def on_key_release(self, key):
            if key == keyboard.Key.esc:
                self.stop_listening()

        def on_mouse_click(self, x, y, button, pressed):
            if pressed and button in self.mouse_button_map:
                button_value = self.mouse_button_map[button]
                self.start_button.configure(text=f" {button_value.upper()} ")  # Обновляем текст кнопки
                self.update_config_aimkey(button_value)
                if self.mouse_listener_active:
                    self.stop_listening()

        def stop_listening(self):
            if self.listener is not None:
                self.listener.stop()
            if self.mouse_listener_active:
                self.mouse_listener.stop()
                self.mouse_listener_active = False
            self.start_button.configure(state=customtkinter.NORMAL)

        def update_config_aimkey(self, aimkey):
            with open("config.json", "r+") as file:
                data = json.load(file)
                data["trigkey"] = aimkey
                file.seek(0)
                json.dump(data, file)
                file.truncate()

    key_logger_app = KeyLoggerApp(tabview.tab(translate("Triggerbot")))

    # Create a switch for "Enter the key you want to use to activate the triggerbot:"
    trigdelayentry = customtkinter.CTkEntry(trigtab, placeholder_text=translate("Enter the key to activate the triggerbot (default e)"), width=300)
    trigdelayentry.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(trigdelayentry, message=translate("This decides what key you want to use to activate the triggerbot."))


    def trigdelayfunc():
        key2 = trigdelayentry.get()
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["trigdelay"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()
        trigdelayentry.delete(0, 'end')  # Clear the guikey entry

    trigdelaybutton = customtkinter.CTkButton(trigtab, text=translate("Enter the delay (ms) for the triggerbot (default 50)"), command=trigdelayfunc, image=CTkImage(dark_image=setconfigimg))
    trigdelaybutton.pack(pady=padding, padx=padding, anchor="w")
    CTkToolTip.CTkToolTip(trigdelaybutton, message=translate("This decides how long the triggerbot waits before shooting."))


    hwidtext = customtkinter.CTkLabel(app, text=f"User ID: {hwid}", fg_color="transparent")
    hwidtext.pack(padx=padding, anchor="center")

    cctext = customtkinter.CTkLabel(app, text=f"© AIMr 2024", fg_color="transparent")
    cctext.pack(padx=padding, anchor="center")

    # make it auto set the config in the gui


    os.system("cls")
    app.mainloop()


except KeyboardInterrupt:
    exit()