import requests,os,cv2,time,re
import tensorflow as tf

class GetImgUrl():
    def __init__(self,word,num=100):
        self.word = word
        self.num = num
        self.mainPath = './Face'
        self.secondPath = word
        self.Path = '{}/{}'.format(self.mainPath,self.secondPath)
        print(self.Path)
        if not os.path.exists(self.mainPath):
            os.mkdir(self.mainPath)
            if not os.path.exists('{}/{}'.format(self.mainPath,self.secondPath)):
                os.mkdir('{}/{}'.format(self.mainPath,self.secondPath))

    def urlDecrypt(self,encrypted_url):
        table = {'w': "a", 'k': "b", 'v': "c", '1': "d", 'j': "e", 'u': "f", '2': "g", 'i': "h",
                 't': "i", '3': "j", 'h': "k", 's': "l", '4': "m", 'g': "n", '5': "o", 'r': "p",
                 'q': "q", '6': "r", 'f': "s", 'p': "t", '7': "u", 'e': "v", 'o': "w", '8': "1",
                 'd': "2", 'n': "3", '9': "4", 'c': "5", 'm': "6", '0': "7",
                 'b': "8", 'l': "9", 'a': "0", '_z2C$q': ":", "_z&e3B": ".", 'AzdH3F': "/"}

        url = re.sub(r'(?P<value>_z2C\$q|_z\&e3B|AzdH3F+)', lambda matched: table.get(matched.group('value')), encrypted_url)
        decrypt_url = re.sub(r'(?P<value>[0-9a-w])', lambda matched: table.get(matched.group('value')), url)

        return decrypt_url


    def getUrlList(self):
        self.imglist = []
        for i,page in enumerate(range(0,self.num,30)):
            url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={}&pn={}'.format(self.word,str(page))
            response = requests.get(url=url).json()['data']
            try:
                for i in response:
                    newurl = self.urlDecrypt(i['objURL'])
                    self.imglist.append(newurl)
            except Exception as e:
                print(e)
        return self.imglist

    def Face_Detection(self):
        self.getUrlList()

        for url in self.imglist:
            print(url)
            try:
                img_bytes = requests.get(url=url).content
            except Exception as e:
                print(e)
                continue
            # cv2.imwrite('./.img',img_bytes)
            with open('./.img','wb') as f:
                f.write(img_bytes)
            try:
                img = cv2.imread('./.img')
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
                faces = face_cascade.detectMultiScale(gray,scaleFactor=1.15,
                                                      minNeighbors=10,
                                                      minSize=(50,50))
            except Exception as e:
                print(e)
                continue

            if len(faces) != 0:

                for x,y,w,h in faces:
                    print([x,y,w,h])
                    filepath = self.Path+'/'+''.join(str(time.time()).split('.'))+'.jpg'
                    filename = ''.join(str(time.time()).split('.'))+'.jpg'
                    face_img = gray[y-10:y+h+10,x-10:x+w+10]
                    face_img = cv2.resize(face_img,(100,100),interpolation=cv2.INTER_CUBIC)
                    print(filename)
                    cv2.imwrite('./TLY/face/{}'.format(filename),face_img)


            # cv2.imshow('test',img)
            # cv2.waitKey(0)


if __name__ == '__main__':
    name = input('input img name: ')
    a = GetImgUrl(name,num=100)
    a.Face_Detection()
