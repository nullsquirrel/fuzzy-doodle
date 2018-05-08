import random, os

class ImagePlaylist:
    def __init__(self):
        self.__imageList = []
        self.__shuffledPlayList = []
        self.__shuffleIndex = 0
        self.supportedExtensions = ['.jpg', '.jpeg', '.png', '.tiff']

    # def loadImagePlayList(self, imageListFile)

    # def saveImagePlayList(self, imageListFile)

    def addImage(self, image):
        if (image not in self.__imageList
            and os.path.isfile(image)
            and image.endswith(tuple(self.supportedExtensions))
            ):
                self.__imageList.append(image)

    def addImages(self, imageList):
        for image in imageList:
            self.addImage(image)

    def appendDirectory(self, directory):
        if directory != '':
            fileList = [os.path.join(directory, file) for file in os.listdir(directory)]
            self.addImages(fileList)

    def removeImage(self, index):
        self.__imageList.pop(index)

    def removeImages(self, indicies):
        for index in indicies:
            self.removeImage(index)

    def shuffleImages(self):
        imgListLen = len(self.__imageList)
        self.__shuffledPlayList = random.sample(range(0, imgListLen), imgListLen)

    def getShuffledImage(self, index):
        return self.__shuffledImageList[self.__shuffledPlayList[index % len(self.__imageList)]]

    def getImage(self, index):
        return self.__imageList[index]

    def __getitem__(self, index):
        return self.getImage(index)

    def __delitem__(self, index):
        del self.__imageList[index]

    def __len__(self):
        return len(self.__imageList)

    def __str__(self):
        return str(self.__imageList)
