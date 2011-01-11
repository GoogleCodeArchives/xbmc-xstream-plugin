from hosters.hoster import iHoster
from resources.lib.handler.hosterHandler import cHosterHandler

class cHoster(iHoster):

    def __init__(self):
        self.__sDisplayName = 'Archive.to'

    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName

    def getPluginIdentifier(self):
        return 'archive'

    def isDownloadable(self):
        return True
    
    def isJDownloaderable(self):
        return True

    def getPattern(self):
        return '<a href="([^"]+)">Download</a></b>'

    def setUrl(self, sUrl):
        self.__sUrl = sUrl

    def checkUrl(self, sUrl):
        return True

    def getUrl(self):
        return self.__sUrl

    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):
        oHosterHandler = cHosterHandler()
        aUrl = oHosterHandler.getUrl(self)

        if (aUrl[0] == True):
            return True, str(aUrl[1]).replace(':80', '')

        return aUrl