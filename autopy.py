import os
import json
import time
import shutil
import ctypes
import random
import string
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
            print("Your HWID is banned, you can make a case in our discord to be unbanned.")
            time.sleep(10)
            exit()
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
            randomchar = "AIMr " + remote_version + " " + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
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
            "python": False,
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


    with open(localv_path, "r") as file:
            data = json.load(file)
            activated = data["activated"]
    
    if activated is not True:
        def check_string(string):
            numbers_count = sum(c.isdigit() for c in string)
            symbols_count = sum(not c.isalnum() for c in string)
            charcount = len(string)

            if numbers_count == 5 and symbols_count == 2 and charcount == 16:
                return True
            else:
                return False
        print("User ID: " + hwid)
        key = input("OPEN https://is.gd/YuWC3r IN YOUR BROWSER TO GET A KEY | Enter your key: ")
        
        if check_string(key):
            print("Thank you for activating, AIMr will now install!")
        else:
            print("Please enter a valid key.")
            exit()
        with open("localv.json", "w") as file:
            data["activated"] = True
            json.dump(data, file)


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

        with open("localv.json", "w") as file:
            data["version"] = remote_version
            json.dump(data, file)

        with open(localv_path, "r") as file:
            data = json.load(file)
            python = data["python"]

        print("User ID: " + hwid)
        install_python = False if input("Do you have python installed? (y/n): ").lower() == "y" else True

        if install_python:
            if python is not True:
                print("Downloading python...")
                # Download the python
                url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
                filename = "pythoninstaller.exe"
                urllib.request.urlretrieve(url, filename)

                print("Installing python (may take a little while)...")
                subprocess.run([filename, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"])

                with open("localv.json", "r") as file:
                    data = json.load(file)

                with open("localv.json", "w") as file:
                    data["python"] = True
                    json.dump(data, file)


                os.remove(filename)

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
            os.system("cls")
        else:
            os.system("clear")

    clear_terminal()
    subprocess.run(["python", "config.py"])

except KeyboardInterrupt:
    exit()

except Exception as e:
        print(f"An error occurred: {e}")
        # Wait for 15 seconds before closing
        time.sleep(15)
        exit()