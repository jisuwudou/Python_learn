from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
global a
a = 1
# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):

    print(a)
    if alpha == 0:
        return ' '
    if r >= 200 and g >= 200 and b >= 200:
        return '-'
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    # test()
    return ascii_char[int(gray/unit)]

def test():
    print(a)
if __name__ == '__main__':
    ee = int(eval('0xffffff') * 0.5)
    print(type(ee))
    print(str(hex(ee)))
    print(int('0xffffff', 16))


    # im = Image.open(IMG)
    # im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    #
    # txt = ""
    #
    # for i in range(HEIGHT):
    #     for j in range(WIDTH):
    #         txt += get_char(*im.getpixel((j,i)))
    #     txt += '\n'
    #
    # print(txt)
    #
    # #字符画输出到文件
    # if OUTPUT:
    #     with open(OUTPUT,'w') as f:
    #         f.write(txt)
    # else:
    #     with open("output.txt",'w') as f:
    #         f.write(txt)