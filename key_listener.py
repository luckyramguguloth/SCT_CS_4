"""
Task 04: Local Window Key Logger (Educational Scope)
SkillCraft Technology Cybersecurity Internship
This script demonstrates a local key logging interface.
It is strictly scoped to capture events occurring *only* within its own GUI window.
This highlights the programming concept of event handling/logging without creating 
dangerous, system-wide keylogging capabilities.
"""

import sys
import os
import time

try:
    import tkinter as tk
except ImportError:
    print("[!] Error: 'tkinter' library is required to run the local GUI listener.")
    print("    This is normally packaged with Python on Windows. Please check your install.")
    sys.exit(1)
LOG_FILE = "local_events.txt"
class LocalKeyListenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task 04: Local Event Listener")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        
        self.root.configure(bg="#1E1E1E")
        
        self.header = tk.Label(
            root,
            text="Local GUI Key Logger (Educational Demo)",
            fg="#4CAF50",
            bg="#1E1E1E",
            font=("Courier", 14, "bold")
        )
        self.header.pack(pady=10)
        
        self.info = tk.Label(
            root,
            text="Type anywhere in the text area below.\nYour keystrokes are recorded ONLY within this program window\nand logged to: local_events.txt",
            fg="#CCCCCC",
            bg="#1E1E1E",
            justify="center",
            font=("Arial", 9)
        )
        self.info.pack(pady=5)
        
        self.text_area = tk.Text(
            root,
            width=50,
            height=10,
            bg="#2D2D2D",
            fg="#FFFFFF",
            insertbackground="white",
            font=("Consolas", 11),
            relief="solid",
            bd=1
        )
        self.text_area.pack(pady=10)
        self.text_area.focus_set()
        
        # Setup file log
        self.log_file_path = os.path.join(os.getcwd(), LOG_FILE)
        print(f"[*] Logging events locally to: {self.log_file_path}")
        
        # Initialize log file with a session header
        with open(self.log_file_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- SESSION STARTED AT {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            
        self.text_area.bind("<KeyPress>", self.log_keypress)
        self.status = tk.Label(
            root,
            text="Status: Listening locally...",
            fg="#888888",
            bg="#1E1E1E",
            font=("Arial", 8, "italic")
        )
        self.status.pack(side="bottom", fill="x", pady=5)
        
    def log_keypress(self, event):
        """
        Callback triggered whenever a key is pressed while the text window is in focus.
        Logs the key identifier, character, and timestamp to a local file.
        """
        timestamp = time.strftime('%H:%M:%S')
        key_char = event.char
        key_name = event.keysym
        
        if not key_char or ord(key_char) < 32:
            display_str = f"[{key_name}]"
        else:
            display_str = key_char
            
        # Write to log file
        try:
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] Key: {key_name:<15} Char: {display_str}\n")
            print(f"[Event Log] Key: {key_name:<15} Char: {display_str}")
        except Exception as e:
            print(f"[!] Log write error: {e}")


def main():
    root = tk.Tk()
    app = LocalKeyListenerApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n[*] Application closed. Exiting.")
        
    print(f"[*] Session closed. Keystrokes saved to '{LOG_FILE}'.")

if __name__ == "__main__":
    main()
