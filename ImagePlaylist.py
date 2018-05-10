import random, os

class ImagePlaylist:
    def __init__(self):
        self.__imageList = []
        self.__shuffledPlayList = []
        self.__shuffleIndex = 0
        self.supportedExtensions = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp']

    # def loadImagePlayList(self, imageListFile)

    # def saveImagePlayList(self, imageListFile)

    def appendImages(self, imageList):
        for image in imageList:
            additions = 0
            additions += self.appendImage(image)
        return additions

    def appendImage(self, image):
        if os.path.isfile(image):
            dir, file = os.path.split(image)
            additions = self.__appendImageFile(dir, file)
            return additions
        else:
            return 0

    def __appendImageFile(self, dir, file):
        entry = (dir, file)
        if (file.endswith(tuple(self.supportedExtensions)) and entry not in self.__imageList) :
            self.__imageList.append(entry)
            return 1
        else:
            return 0

    def appendDirectory(self, dir):
        if (dir != '' and os.path.isdir(dir)):
            additions = 0
            for file in os.listdir(dir):
                additions += self.__appendImageFile(dir, file)
            return additions
        else:
            return 0

    def removeImage(self, image):
        if image is int:
            return self.__imageList.pop(image)
        elif image is str:
            index = self.__imageList.index(os.path.split(image))
            if index >= 0:
                return self.__imageList.pop(index)


    def removeImages(self, indicies):
        for index in indicies:
            self.removeImage(index)

    def shuffleList(self):
        imgListLen = len(self.__imageList)
        self.__shuffledPlayList = random.sample(range(imgListLen), imgListLen)

    def getRandomImage(self, index):
        return self.__imageList[self.__shuffledPlayList[index % len(self.__imageList)]]

    def getImage(self, index):
        entry = self.__imageList[index]
        return os.path.join(entry[0], entry[1])

    def __getitem__(self, index):
        return self.getImage(index)

    def __delitem__(self, index):
        del self.__imageList[index]

    def __len__(self):
        return len(self.__imageList)

    def __str__(self):
        return str(self.__imageList)


if __name__ == '__main__':
    pl = ImagePlaylist()
    cwd = os.path.curdir()
    pl.supportedExtensions += ['.py', '.pyc']
