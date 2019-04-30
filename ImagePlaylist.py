import random
import os


class ImagePlaylist:
    def __init__(self):
        self.__imageList = []
        self.__randomList = []
        self.__history = []
        self.__nextImage = 0
        self.__index = 0  # __index goes backward (i.e. negative) into history
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
        if file.endswith(tuple(self.supportedExtensions)) and entry not in self.__imageList:
            self.__imageList.append(entry)
            if self.__index == 0:
                self.__index = -1
                self.__history.append(0)
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

    def getRandomImage(self):
        self.__index = -1

        randListLen = len(self.__randomList)
        imgListLen = len(self.__imageList)
        histLen = len(self.__history)

        if randListLen <= 0:
            self.__randomList = random.sample(range(imgListLen), imgListLen)

        if histLen < imgListLen:
            self.__randomList -= self.__history
        else:
            self.__randomList = self.__history[-(imgListLen/2):]

        if len(self.__randomList) > 0:
            choice = self.__randomList.pop(0)
            self.__history.append(choice)

        return self.getImage()

    def getNextImage(self):
        if self.__index < -1:
            self.__index += 1
        else:
            next = self.__history[self.__index] + 1
            next %= len(self.__imageList)
            self.__history.append(next)
        return self.getImage()

    def getPrevImage(self):
        histLen = len(self.__history)
        if histLen + self.__index > 0:
            self.__index -= 1
        return self.getImage()

    def getImage(self):
        return self.__getImage(self.__history[self.__index])

    def __getImage(self, index):
        entry = self.__imageList[index]
        return os.path.join(entry[0], entry[1])

    def __getitem__(self, index):
        return self.__getImage(index)

    def __delitem__(self, index):
        del self.__imageList[index]

    def hasHistory(self):
        historyPosition = len(self.__history) + self.__index
        return True if historyPosition > 0 else False

    def __len__(self):
        return len(self.__imageList)

    def __str__(self):
        return str(self.__imageList)


if __name__ == '__main__':
    pl = ImagePlaylist()
    cwd = os.path.curdir()
    pl.supportedExtensions += ['.py', '.pyc']
