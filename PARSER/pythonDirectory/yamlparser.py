import yaml

def get_yamldata(file_name):
    yamldata={}
    with open(file_name, 'r') as stream:
        try:
            yamldata=yaml.safe_load(stream)
            return yamldata
        except yaml.YAMLError as exc:
            print(exc)
            return None
