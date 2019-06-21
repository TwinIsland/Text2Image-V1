#encoding:utf-8
import cv2
import os

photo_data = cv2.imread('input.jpg')

def content_from_file():
    return open('input.txt','r',encoding='utf-8').read()

def to_bin(inf):
    new = ''
    for i in inf:
        new += str(bin(ord(i))).replace('0b','') + ' '
    return new[:-1]

def to_string(inf):
    return chr(int(inf,2))

def int_to_bin(inf):
    con  = str(bin(int(str(inf),10))).replace('0b','')
    if con == '0':
        return '00000'
    elif len(con) <= 4:
        #print('stimulate small number generator')
        return str(pow(10,(5 - len(con))))[1:] + con
    else:
        return con

def bin_to_int(inf):
    place = inf.find('1')
    if place == -1:
        return 0
    else:
        return int(inf[place:],2)


if __name__ == '__main__':


    #print(bin_to_int(int_to_bin(10033)))
    data = to_bin(content_from_file()).split(' ')
    index = list(map(lambda x:int_to_bin(len(x)),data))
    #print(data)
    #print(index)
    total_index = len(data)
    len_for_total_index = len(str(int_to_bin(total_index)))
    len_for_len_for_total_index = len(str(int_to_bin(len_for_total_index)))
    h,w = photo_data.shape[:2]
    max_size = h * w

    # compose information
    inf = []
    inf.append(int_to_bin(len_for_len_for_total_index))
    inf.append(int_to_bin(len_for_total_index))
    inf.append(int_to_bin(total_index))
    inf += index
    inf += data
    #print(inf)
    inf = ''.join(inf)
    # print(inf)

    total_size = len(inf)

    print('Config: \n'
          '------------\n'
          'Total index: ' + str(total_index) + '\n'
          'Len for total index: ' + str(len_for_total_index) + '\n'
          'Total Size(guess): ' + str(total_size)+ '\n'
          'Max Size: ' + str(int(max_size)) + '\n'
          '------------\n')

    input('press enter to continue...')

    # check if out of bound
    if total_size >= max_size or len(int_to_bin(len_for_len_for_total_index)) >5:
        print('Max Size Out Of Flow !')
        input('press to exit...')
        os._exit(0)

    print('encoding...')

    # initialize the photo, and make it writable
    for x in range(h):
        for y in range(w):
            if photo_data[x,y,0] % 2 != 0: # is odd
                photo_data[x,y,0] = photo_data[x,y,0] + 1 # to even

    #print(str(inf[:20]) + '...')

    # [ len for len for len for index, len for len for  index, index lens, ...index data..., ...data...]
    # ['0001', '0011', '1101011000', '0111', '0111', '0111', '0110', '0111', '0111', '0111', '0110', '0111', '0111'

    for x in range(h):
        for y in range(w):
            count = x*w + y
            if count < len(inf):
                #print('Processing: ' + str(count+1) +'/' + str(total_size))
                photo_data[x,y,0] -= int(inf[count]) # not use +
            else:
                break

    #print(photo_data[:1,:10,0])
    print('OK !')

    # cannot write as jpg, because of one cv2's bug
    # thanks: https://blog.csdn.net/oukohou/article/details/82378552
    cv2.imwrite('output.png',photo_data)

    input()