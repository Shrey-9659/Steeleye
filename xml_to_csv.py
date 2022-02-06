import csv
import xml.etree.ElementTree as Xet
import pandas as pd
  
cols = ["Id", "FullNm", "ClssfctnTp", "CmmdtyDerivInd", "NtnlCcy", "Issr"]
rows = []
xmlparse = Xet.parse('./steeleye.xml')
root = xmlparse.getroot()
for i in root:
    # print(i.attrib)
    Id = i.find("name")
    FullNm = i.find("FullNm")
    ClssfctnTp= i.find("ClssfctnTp")
    CmmdtyDerivInd= i.find("CmmdtyDerivInd")
    NtnlCcy = i.find("NtnlCcy")
    Issr = i.find("Issr")
  
    rows.append({"Id":Id, "FullNm":FullNm, "ClssfctnTp":ClssfctnTp, "CmmdtyDerivInd":CmmdtyDerivInd, "NtnlCcy":NtnlCcy, "Issr":Issr})
  
df = pd.DataFrame(rows, columns=cols)
df.to_csv('steeleye1.csv')