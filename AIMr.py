import os
import json
import time
import random
import string
import ctypes
import shutil
import zipfile
import threading
import subprocess
import urllib.request

try:

    def checkhwid():
        hwidlisturl = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/ids.txt"
        hwidlist = urllib.request.urlopen(hwidlisturl).read().decode()
        global hwid
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        if hwid in hwidlist:
            print("Your HWID is banned (somehow), buuut... you can still use AIMr! Enjoy :)")
        else:
            pass

    checkhwid()

    newest_version = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/current_version.txt"
    req = urllib.request.Request(newest_version, headers={'Cache-Control': 'no-cache'})
    response = urllib.request.urlopen(req)
    remote_version = response.read().decode().strip()

    # randomize terminal/window title
    def set_console_title():
        while True:
            randomchar = "AIMr " + remote_version + " " + '- FOSS version by enbyte'
            ctypes.windll.kernel32.SetConsoleTitleW(randomchar)
            time.sleep(0.1)

    # start above thread
    cstitle = threading.Thread(target=set_console_title)
    cstitle.daemon = True  # Set the thread as a daemon thread
    cstitle.start()

    file_paths = [
        "./AIMr.ico",
        "./AIMr.py",
        "./LICENSE",
        "./README.md",
        "./autopy.py",
        "./changelog.txt",
        "./config.py",
        "./current_version.txt",
        "./daily.txt",
        "./ids.txt",
        "./info.md",
        "./installation.md",
        "./library.py",
        "./logo.txt",
        "./req.txt",
        "./theme.json",
        "./yolo.cfg",
        "./yolo.weights",
        "./obfuscation.md"
    ]

    localv_path = "localv.json"
    config_path = "config.json"

    if not os.path.exists(localv_path) or not os.path.exists(config_path) or not os.path.exists(file_paths[1]):
        local_version = "0.0.0"
        data = {
            "version": remote_version,
            "pip": False,
            "python": True,
            "first_launch": True,
            "activated": False
        }
        with open(localv_path, "w") as file:
            json.dump(data, file)
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
    else:
        with open(localv_path, "r") as file:
            data = json.load(file)
            local_version = data["version"]
    
    with open(localv_path, "r") as file:
            data = json.load(file)
            activated = data["activated"]

    if activated is not True: # wtf??? whatever happened to "if activated:" ??
                              # "is not True" is crazy
            
        print("User ID: " + hwid)
        
        with open("localv.json", "w") as file:
            data["activated"] = True
            json.dump(data, file)

    with open("localv.json", "r") as file:
        data2 = json.load(file)
        first_launch = data["first_launch"]

    if first_launch is not True:
        with open("localv.json", "r") as file:
                data2 = json.load(file)
                pip = data["pip"]

        if pip is not True:
            file_url = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/req.txt"

            req = urllib.request.urlopen(file_url)
            lines = req.read().decode().split("\n")
            line_list = list(lines)
            line_list.pop()
            total_lines = len(line_list)

            for i in range(total_lines):
                subprocess.run(["pip", "install", line_list[i], "-q"])
                percent_installed = (i + 1) / total_lines * 100
                print(f"Installing pip module {i+1}/{total_lines}. {percent_installed:.2f}% complete.", end='\r', flush=True)


    if remote_version != local_version:

        with open("localv.json", "w") as file:
                data2["pip"] = False
                json.dump(data2, file)

        print("Deleting old files...")
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error occurred while removing {file_path}: {e}")

        print("Downloading AIMr...")
        # Download the zip file
        url = "https://codeload.github.com/ai-aimbot/AIMr/zip/refs/heads/main"
        response = urllib.request.urlopen(url)
        zip_content = response.read()

        # Save the zip file
        with open("ai-aimbot-main.zip", "wb") as file:
            file.write(zip_content)

        print("Unzipping...")
        # Unzip the file
        with zipfile.ZipFile("ai-aimbot-main.zip", "r") as zip_ref:
            zip_ref.extractall("ai-aimbot-main")
        os.remove("ai-aimbot-main.zip")

        print("Moving files...")
        # Move files from ai-aimbot/ to current directory
        for root, dirs, files in os.walk("ai-aimbot-main"):
            for file in files:
                shutil.move(os.path.join(root, file), os.path.join(".", file))

        # Remove ai-aimbot-testing/ directory
        shutil.rmtree("ai-aimbot-main")

        # Remove files from file_paths list
        for file_path in [file_paths[2], file_paths[3], file_paths[4], file_paths[5], file_paths[7], file_paths[8], file_paths[9], file_paths[10], file_paths[11], file_paths[14]]:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error occurred while removing {file_path}: {e}")

        with open("localv.json", "r") as file:
            data = json.load(file)

        with open("localv.json", "w") as file:
            data["version"] = remote_version
            data["first_launch"] = False
            data["pip"] = False
            json.dump(data, file)
        print("Please relaunch AIMr...")
        time.sleep(5)
        exit()

    def clear_terminal():
        if os.name == "nt":
            os.system("cls") # this is unreachable bruh like get better
        else:
            os.system("clear")

    clear_terminal()
    try:
        # 14 unique imports??? crazy copy paste skid coding here
        import os
        import json
        import time
        import ctypes
        import random
        import string
        import threading
        import subprocess
        from colorama import just_fix_windows_console
        just_fix_windows_console()

    except ImportError:
        file_url = "https://raw.githubusercontent.com/ai-aimbot/AIMr/main/req.txt"

        req = urllib.request.urlopen(file_url)
        lines = req.read().decode().split("\n")
        line_list = list(lines)
        line_list.pop()
        total_lines = len(line_list)

        for i in range(total_lines):
            subprocess.run(["pip", "install", line_list[i], "-q"])
            percent_installed = (i + 1) / total_lines * 100 # lol
            print(f"Installing pip module {i+1}/{total_lines}. {percent_installed:.2f}% complete.", end='\r', flush=True)
    subprocess.run(["python", "config.py"])

except KeyboardInterrupt:
    exit()

except Exception as e:
    print(f"An error occurred, exiting: {e}")
    # Wait for 15 seconds before closing
    # the above is one chatGPT ass comment