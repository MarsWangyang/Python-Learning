import os
import time

def main():
    content = 'Taiwan No.1!!!!! China No.-1......'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()