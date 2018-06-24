import xml.sax
import data_structure
import excel_export

class SoccerParser (xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.page_waked = False
        self.title_waked = False
        self.pid_waked = False
        self.revision_waked = False
        self.text_waked = False
        self.isTarget = False
        self.instance = data_structure.DataSet()
        self.text = ''

    def startElement(self, name, attrs):
        if name == 'page':
            self.page_waked = True
        elif name == 'title' and self.page_waked is True and self.revision_waked is False:
            self.title_waked = True
        elif name == 'id' and self.page_waked is True and self.revision_waked is False:
            self.pid_waked = True
        elif name == 'revision' and self.page_waked is True:
            self.revision_waked = True
        elif name == 'text' and len(attrs) == 1 and self.revision_waked is True and self.page_waked is True:
            self.text_waked = True
        else:
            return

    def endElement(self, name):
        if name == 'page':
            self.page_waked = False
            if self.isTarget is True:
                data_structure.requestAppend(self.instance)
            self.instance = data_structure.DataSet()
        elif name == 'title' and self.page_waked is True and self.revision_waked is False:
            self.title_waked = False
        elif name == 'id' and self.page_waked is True and self.revision_waked is False:
            self.pid_waked = False
        elif name == 'revision' and self.page_waked is True:
            self.revision_waked = False
        elif name == 'text' and self.revision_waked is True and self.page_waked is True:
            self.text_waked = False
            if data_structure.isSoccerPage(self.text) is True:
                data_structure.DataSet.getInfoBox(self.text, self.instance)
                self.isTarget = True
            else:
                self.isTarget = False
            self.text = ''
        else:
            return

    def characters(self, data):
        if self.title_waked is True:
            self.instance.setField('Page Title', data)
        elif self.pid_waked is True:
            self.instance.setField('Page ID', data)
        elif self.text_waked is True:
            self.text += data
        else:
            return

pathToXML = '../dump/kowiki-20180401-pages-articles-multistream.xml'
# pathToXML = '../dump/test_soccer.xml'
pathToSave = 'c:/out.xlsx'
handler = SoccerParser()
print("Start to parse")
xml.sax.parse(pathToXML, handler)
print("Parsing is ended")
print("Resolved Data -------------------------------------------------------------------------------------------------")
print("Data is cropped :: %d" % len(data_structure.DataSetList))
print("End of Data ---------------------------------------------------------------------------------------------------")
print("Save Path :: " + pathToSave)
excel_export.printToExcel(pathToSave)
print("Export Done.")