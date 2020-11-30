# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values


#some changes from another branch called signin 

#some changes from another branch called signin and merge to the master branch 


def main():
    # define some starting values
    print('*'*100)
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them. 
    #print(s+b)
    #x = s + b
    #print(x)

    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    b2 = b.decode('utf-8')
    x = s + b2
    print(x)
    print(type(x))
    s2 = s.encode('utf-8')
    x2 = b + s2
    print(x2)
    print(type(x2))

    # TODO: encode the string as UTF-32
    s3 = s.encode('utf-32')
    print(s3)
    print(type(s3))
    b3 = b2.encode('utf-32')
    print(b3)
    print(type(b3))
    print(s3, ':', b3)


if __name__ == "__main__":
    main()

def EandD():
    print('*'*100)
    x = 'string'
    y = bytes([0x45, 0x46, 0x47, 0x48])
    print(type(x), x)
    print(type(y), y)

    x2 = x.encode('utf-8')
    print(type(x2), x2 + y)
    y2 = y.decode('utf-8')
    print(type(y2), y2 + x)


    y3 = y2.encode('utf-32')
    x3 = x.encode('utf-32')
    print(type(x3), x3, ' : ', type(y3), y3)
    print(f'This is an enryppted text {x3}')
    print('This is the first encrypted text {0}, and this is the second one {1}'.format(x3, y3))



EandD()