
import sys
import json
import os

CCLI = "remarshal -i pyproject.toml -o pyproject.json"
path = os.environ["LAB"]
PCLI = f"remarshal -i {path}/pyproject.toml -o py-current-project.json"
TCLI = "remarshal -if json -of toml build/pyproject.json > build/pyproject.toml"

def merge_dependencies(_json_files:list,_json_dict:dict) -> dict:
    l_dependencies=[]
    for ijson in _json_files:
        with open(ijson, "r", encoding="utf-8") as f:
            data = json.load(f)
            for idep in data["project"]["dependencies"]:
                l_dependencies.append(idep)

    _json_dict["project"]["dependencies"] = l_dependencies
    return _json_dict

#no guard rails have been implemented.
#todo the checkings need to be added
if __name__ == "__main__":
    
    #generate the pyproject.json file from the pyproject.toml
    os.system(CCLI)
    #generate the py-current-project.json file from the pyproject.toml contained 
    #in the folder shared between the host and the container
    os.system(PCLI)

    #lists all the json files contained the current dir
    l_jfiles =[] 
    for ifile in os.listdir():
        if ".json" in ifile:
            l_jfiles.append(ifile)
    
    #loads the py-core pyproject.json file
    l_jpyproject = None 
    with open("pyproject.json", "r", encoding="utf-8") as f:
        l_jpyproject = json.load(f)
    
    #merge the list of packages of py-core with the current project
    l_jpyproject = merge_dependencies(l_jfiles,l_jpyproject)

    #create build dir if it doesn't exist
    os.makedirs("build", exist_ok=True)
    #create the pyproject.json file in the build dir
    with open("build/pyproject.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(l_jpyproject))

    #generate the pyproject.toml file from the pyproject.json contained
    #in the build directory
    os.system(TCLI)
