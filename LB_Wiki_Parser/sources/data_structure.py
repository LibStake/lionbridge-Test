import re
import data_dresser
pattern = re.compile('\[\[분류:(.{2,12})[의|에] 축구 선수\]\]')
pattern_deny_category = re.compile('분류:(.{2,12})[의|에] 축구 선수')
DataSetList = []

listInfoboxTemplate = ['축구 선수 정보']
listInfoboxBirth = ['출생일']
listInfoboxHeight = ['키']
listInfoboxTeam = ['현 소속팀']

def requestAppend(instance):
    if (pattern_deny_category.search(instance.field['Page Title'])) is not None:
        return

    instance.field['Date of Birth'] = data_dresser.dressBirthDate(instance.field['Date of Birth'])
    instance.field['Height'] = data_dresser.dressHeight(instance.field['Height'])
    instance.field['Team'] = data_dresser.dressTeam(instance.field['Team'])

    print(instance.field['Page ID'] + '\t' + instance.field['Page Title'] + '\t' + instance.field['Template Name'] + '\t' + instance.field['Date of Birth'] + '\t' + instance.field['Height'] + '\t' + instance.field['Team'])
    DataSetList.append(instance)
class DataSet:
    def __init__(self):
        self.field = {'Page ID': 'None', 'Page Title': 'None', 'Template Name': 'None', 'Date of Birth': 'None', 'Height': 'None', 'Team': 'None'}

    def setField(self, fieldName, value):
        self.field[fieldName] = value

    @staticmethod
    def getInfoBox(text, instance):
        lengthoftext = len(text)
        begin = -1
        end = -1
        for templateName in listInfoboxTemplate:
            begin = text.find('{{' + templateName)
            if begin == -1:
                continue
            idx = begin + 2
            brk = 2
            while brk > 0:
                if text[idx] == '}':
                    brk -= 1
                elif text[idx] == '{':
                    brk += 1
                idx += 1
                if idx == (lengthoftext - 1):
                    idx = 0
                    break
            end = idx

        if end is -1:
            print("Error :::::: Cannot find main infobox Page ID :: " + instance.field['Page ID'])
            return ''

        DataSet.parseInfoboxIntoDataStructure(text[begin:end], instance)

    @staticmethod
    def parseInfoboxIntoDataStructure(info, instance):
        for key in listInfoboxTemplate:
            out = DataSet.parseInfobox(info, key)
            if out is not 'None':
                instance.setField('Template Name', out)

        for key in listInfoboxBirth:
            out = DataSet.parseInfobox(info, key)
            if out != 'None':
                instance.setField('Date of Birth', out)

        for key in listInfoboxHeight:
            out = DataSet.parseInfobox(info, key)
            if out != 'None':
                instance.setField('Height', out)

        for key in listInfoboxTeam:
            out = DataSet.parseInfobox(info, key)
            if out != 'None':
                instance.setField('Team', out)

    @staticmethod
    def parseInfobox(str, key):
        stk = []
        cntBBrk = 0
        cntBrk = 0
        keyname = ''
        keyvalue = ''

        for ch in str:
            if ch is '{':
                cntBrk += 1
            elif ch is '}':
                cntBrk -= 1
            elif ch is '|':
                if cntBrk is 2 and keyname is '' and cntBBrk is 0:
                    keyname = ''.join(stk).strip()
                    stk = []
                    if keyname == key:
                        return keyname
                    else:
                        keyname = ''
                elif cntBrk is 2 and keyname is not '' and cntBBrk is 0:
                    keyvalue = ''.join(stk).strip()
                    stk = []
                    if keyname == key:
                        return keyvalue
                    else:
                        keyname = ''
                        keyvalue = ''
                else:
                    stk.append(ch)
            elif ch is '=':
                if cntBrk is not 2:
                    stk.append(ch)
                else:
                    keyname = ''.join(stk).strip()
                    stk = []
            elif ch is '[':
                cntBBrk += 1
                stk.append(ch)
            elif ch is ']':
                cntBBrk -= 1
                stk.append(ch)
            else:
                stk.append(ch)

        return 'None'

def isSoccerPage(text):
    if pattern.search(text) is not None:
        return True
    else:
        return False


