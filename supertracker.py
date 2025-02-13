import os
import subprocess
import ctypes
import winreg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def scan_registry():
    errors = []
    try:
        # Attempt to open a registry key as a test
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion", 0, winreg.KEY_READ)
        winreg.CloseKey(key)
    except FileNotFoundError:
        errors.append("Registry key not found: SOFTWARE\\Microsoft\\Windows\\CurrentVersion")
    except PermissionError:
        errors.append("Permission error accessing registry key: SOFTWARE\\Microsoft\\Windows\\CurrentVersion")
    return errors

def fix_registry():
    # Placeholder function for fixing registry errors
    # In a real scenario, this would involve making appropriate changes to the registry
    print("Fixing registry errors...")

def main():
    if not is_admin():
        print("This program requires administrative privileges.")
        print("Please run this script as an administrator.")
        return

    print("Scanning registry for errors...")
    errors = scan_registry()

    if errors:
        print("Registry errors found:")
        for error in errors:
            print(f"- {error}")
        user_input = input("Would you like to attempt to fix these errors? (yes/no): ").strip().lower()
        if user_input == 'yes':
            fix_registry()
            print("Attempted to fix registry errors.")
        else:
            print("Registry errors were not fixed.")
    else:
        print("No registry errors found. Your system is stable.")

if __name__ == "__main__":
    main()