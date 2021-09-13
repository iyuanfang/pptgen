from copy_ppt import *
from pptx import Presentation


def get_name_from_line(line):
    return line.strip().split(':')[0].split('@')[0]


def get_indexs_from_line(line):
    print(line)
    return line.strip().split(':')[0].split('@')[1].split(',')


def get_placeholdertexts_from_line(line):
    if ":" in line:  # 设置了placeholader的值
        return line.strip().split(':')[1].split(',')
    else:
        return None


def gen(folder,filename):
    des = Presentation("gen/template.pptx")
    lines = open(folder+filename+".txt", "r", encoding="UTF-8").readlines()
    print(lines)
    for line in lines:
        if line.strip() == '':
            continue
        src = Presentation("./gen/"+get_name_from_line(line)+".pptx")
        placeholdertexts = get_placeholdertexts_from_line(line)
        print(placeholdertexts)
        if "@" in line:  # 指定页面
            indexs = get_indexs_from_line(line)
            for index in indexs:
                copy_ppt_index(des, src, int(index), placeholdertexts)
        else:  # 也支持placeholder，但会把所有slide的placeholder替换为指定值
            copy_ppt(des, src, placeholdertexts)
    des.save(folder+filename+".pptx")


if __name__ == '__main__':
    content = input("输入定义文件：")
    gen(content)
    # gen("content2")
