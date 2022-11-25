from omrc import omrc
import mido
import time
import threading
import colorama

def play(): 

    playobj = mido.MidiFile("omr.mid")

    with mido.open_output() as port: 

        for i in playobj.play(): 

            port.send(i)

def bf():   # sourcery skip: use-fstring-for-concatenation

    colorama.init()

    print(colorama.Fore.BLACK + colorama.Style.BRIGHT + "ONLY MY RAILGUN".center(53, " "))
    time.sleep(0.45)
    for n in omrc: 
        time.sleep(n[0])
        d = 35 if len(n[1]) <= 35 else 50
        print(colorama.Fore.YELLOW + n[1].ljust(d - len(n[1])), end="")
        print(colorama.Fore.BLUE + n[2])


if __name__ == "__main__": 
    t1 = threading.Thread(target=play)
    t2 = threading.Thread(target=bf)
    pool = [t1, t2]
    t1.start()
    t2.start()

    for p in pool: 
        p.join()

    print("\n" + colorama.Fore.RED + "演奏结束，给个赞再走吧~".center(45, " "))
    print(colorama.Fore.RESET)