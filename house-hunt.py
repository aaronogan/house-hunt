import yaml

def get_config():
    file_name = "config.yml"
    with open(file_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                print(ex)
                return None

if __name__ == "__main__":
    print(get_config())

