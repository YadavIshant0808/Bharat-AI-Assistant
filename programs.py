programs = [
            ["notepad", r"C:\Windows\System32\notepad.exe"],
            ["calculator", r"C:\Windows\System32\calc.exe"],
            ["paint", r"C:\Windows\System32\mspaint.exe"],
            ["command prompt", r"C:\Windows\System32\cmd.exe"],
            ["file explorer", r"C:\Windows\explorer.exe"],
            ["edge", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"],
            ["chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"],
            ["vlc", r"C:\Program Files\VideoLAN\VLC\vlc.exe"],
            ["spotify app", r"C:\Users\scien\AppData\Roaming\Spotify\Spotify.exe"],
            ["vs code", r"C:\Users\scien\AppData\Local\Programs\Microsoft VS Code\Code.exe"],  # VS Code
            ["github", r"C:\Users\scien\AppData\Local\GitHubDesktop\GitHubDesktop.exe"],  # GitHub Desktop
            ["desktop", r"C:\Windows\explorer.exe"],  # Desktop view in File Explorer
            ["camera", r"C:\Windows\System32\Microsoft.WindowsCamera.exe"]  # Camera
        ]
#imports
import os
from speech import say

def open_program(query):
        for program in programs:
            try:
                if f"open {program[0]}".lower() in query.lower():
                    say(f"Opening {program[0]} sir...")
                    os.startfile(program[1])
                    say(f"{program[0]} Opened Sir...")
                    
            except Exception as e:
                print("Error : ",e)
                say("An error oucurred in opening {program[0]} sir...")
#kindly change the path to macth the path of programs in your system