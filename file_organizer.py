import os
import shutil
from datetime import datetime
import sys

folders_ext = {
    "Python": (".py",),
    "Images": (".png", ".jpg"),
    "Documents": (".txt",".pdf"),
    "Ai" : (".ai",)
}

def move_files(src, dest_folder, log, moved, skipped, errors):
    
    try:
        if "--dry-run" in sys.argv:
            message = f"[DRY-RUN] {os.path.basename(src)} -> {dest_folder}\n"
            log.write(message)
            print(message)
        else :
            shutil.move(src,dest_folder)
            log.write(f"[MOVED] {os.path.basename(src)}\n")
            moved +=1
    except Exception as e :
        log.write(f"[ERRORS] {os.path.basename(src)} : {e}\n")
        errors +=1
    return moved, skipped,errors


def main():
    home = os.getenv("HOME") or os.getenv("USERPROFILE")
    desktop = os.path.join(home, "Desktop")

    today_date = datetime.now().strftime("%m-%y-%d")
    moved_file_name = f"moved_file_{today_date}"
    organized_file = os.path.join(desktop,moved_file_name)

    if not "--dry-run" in sys.argv:
        os.makedirs(organized_file,exist_ok=True)

    log_file = os.path.join(organized_file,"Log_file.txt")

    moved = 0
    skipped = 0
    errors = 0

    with open(log_file, 'a' , encoding="utf_8") as log :
        log.write("----------------------------------\n")
        log.write(f"The process started at {today_date}\n")


        for file in os.listdir(desktop) :
            file_path = os.path.join(desktop,file)
            
            if not os.path.isfile(file_path):
                skipped +=1
                continue

            folder_found = False
            for folder,ext in folders_ext.items():
                if file.endswith(ext):
                    folder_path = os.path.join(organized_file,folder)
                    destination = os.path.join(folder_path,file)

                    if not "--dry-run" in sys.argv:
                        os.makedirs(folder_path,exist_ok=True)
                    moved, skipped, errors = move_files(file_path,destination,log,moved,skipped,errors)

                    folder_found = True
                    break

            if not folder_found :
                other_folder = os.path.join(organized_file,"Others")
                des_other = os.path.join(other_folder,file)
                if not "--dry-run" in sys.argv:
                    os.makedirs(other_folder,exist_ok=True)
                moved, skipped, errors = move_files(file_path,des_other,log,moved,skipped,errors)

        log.write(f"-->\nMOVED : {moved}\nSKIPPED : {skipped}\nERRORS : {errors}\n")

    print(f"MOVED : {moved}")
    print(f"SKIPPED : {skipped}")
    print(f"ERRORS : {errors}")


main()