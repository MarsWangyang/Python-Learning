import random
import string

def generateCap(len=4):
    asciiCode = string.ascii_letters + string.digits
    captcha = random.sample(asciiCode, len)
    return "".join(captcha)
if __name__ == '__main__':
    len = int(input('請輸入你要多長的CAPTCHA: '))
    print(generateCap(len))