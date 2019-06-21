#encoding:utf-8

import wtp
import cv2
import os

if __name__ == '__main__':

    print('solving...')
    photo_data = cv2.imread('output.png')

    # get information
    h, w = photo_data.shape[:2]

    #print(photo_data[:1, :10, 0])

    # data structure:
    # ['00101', '00101', '00001', '00111', '1110011'] w
    # ['00101', '00101', '00010', '00111', '00111', '1110111', '1111001'] wy

    code = ''
    for x in range(h):
        for y in range(w):
            if photo_data[x,y,0]%2 == 0:
                code += '0'
            else:
                code += '1'

    # ['00101', '00110', '111000', '00111', '00111', '00111', '00111', '00111', '00110', '00110', '00110', '00111', '00111', '00111', '00111', '00110', '00111', '00111', '00111', '00111', '00110', '00111', '00111', '00111', '00110', '00111', '00111', '00111', '00111', '00111', '00111', '00110', '00110', '00110', '00110', '00111', '00111', '00111', '00111', '00111', '00111', '00111', '00110', '00111', '00111', '00111', '00111', '00111', '00111', '00111', '00110', '00110', '00110', '00110', '00110', '00110', '00110', '00110', '00110', '1101000', '1110100', '1110100', '1110000', '1110011', '111010', '101111', '101111', '1100010', '1101100', '1101111', '1100111', '101110', '1100011', '1110011', '1100100', '1101110', '101110', '1101110', '1100101', '1110100', '101111', '1001101', '1110010', '1011111', '1000011', '1100001', '1110100', '110001', '110010', '110011', '101111', '1100001', '1110010', '1110100', '1101001', '1100011', '1101100', '1100101', '101111', '1100100', '1100101', '1110100', '1100001', '1101001', '1101100', '1110011', '101111', '111000', '110000', '110101', '111000', '110100', '111001', '111000', '111000']

    navigator_pointer = code[:5]
    i = wtp.bin_to_int(navigator_pointer)
    navigator_pointer_2 = wtp.bin_to_int(code[5:5+i])
    index_total = wtp.bin_to_int(code[5+i:5+i+navigator_pointer_2])
    #print(index_total)

    index = code[5+i+navigator_pointer_2:][:5*index_total]
    index = [wtp.bin_to_int(index[i:i+5]) for i in range(0,len(index),5)]
    data = code[5+i+navigator_pointer_2:][5*index_total:]
    #data = [data[sum(data[:ind]):sum(data[:ind])+lens] for ind,lens in enumerate(index)]

    message = ''

    for ind,lens in enumerate(index):
        old_sum = sum(index[:ind])
        message += wtp.to_string(data[old_sum:old_sum + lens])

    with open('output.txt','w') as f:
        f.write(message)

    print('ok !')
    input()