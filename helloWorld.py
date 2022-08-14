import string
import random
import time

def main():
    character = string.ascii_letters + string.digits + string.punctuation + ' '
    word = ''
    start = time.time()
    print("Started")

    for char in "Hello World!":
        ran = random.choice(character)
        word = word + ran
        print(word)
        while (ran != char):
            print ("\033[A                             \033[A")
            word = word[:-1]
            print(word)
            ran = random.choice(character)
            print ("\033[A                             \033[A")
            word = word + ran
            print(word)
            time.sleep(0.05)
        time.sleep(1)
    
    end = time.time()
    print("Ended")
    print("Total time: ", end - start)



if __name__ == "__main__":
    main()