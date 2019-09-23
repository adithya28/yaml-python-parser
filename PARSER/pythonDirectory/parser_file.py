from pythonDirectory.yamlparser import  *
import os
import re
dirname = os.path.dirname(__file__)
class_folder_Name = "pythonclassfiles"
yaml_folder_name = 'yaml_files'
for filename in os.listdir('yaml_files'):
    data  = get_yamldata(yaml_folder_name+"\\"+filename)
    print(data)
    inner_dict=data[sorted(data.keys())[0]]
    with open (class_folder_Name+"\\"+re.sub('([A-Z]{1})', r'_\1',filename).lower().replace('.yaml','.py')[1:],"w+") as file:
        file.write("from Constants import *\n")
        file.write("from CommonRoutines import *\n")
        file.write("from commonUtils import *\n\n")
        file.write("class "+filename.replace(".yaml","")+":\n")
        file.write("\tdef __init__(self):\n")
        for key in inner_dict.keys():
            file.write("\t\tself."+key+" = find_component(self.__class__.__name__, \""+key+"\")\n")