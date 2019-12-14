from testdata import abi, components
import json

arr_flag = "[]"

# combine origin abi and components
def deal_abi(abi, components):
    _newcomponent = deal_components(components)
    nabi = dict()
    nabi["version"] = "1.0"
    nabi["contract_account"] = ""
    newfs = []
    newevts = []
    nabi["functions"] = newfs
    nabi["events"] = newevts
    for f in abi["functions"]:
        nf = dict()
        nf["name"] = f["name"]
        nf["inputs"] = []
        nf["outputs"] = []

        for arg in f["inputs"]:
            newarg = deal_arg_with_components(components, arg)
            nf["inputs"].append(newarg)
        for arg in f["outputs"]:
            newarg = deal_arg_with_components(components, arg)
            nf["outputs"].append(newarg)

        newfs.append(nf)

    for evt in abi["events"]:
        nevt = dict()
        nevt["name"] = f["name"]
        nevt["inputs"] = []
        nevt["outputs"] = []

        for arg in evt["inputs"]:
            newarg = deal_arg_with_components(components, arg)
            nevt["inputs"].append(newarg)

        newevts.append(nevt)

    return nabi


# deconstruct componets array to the structure the  abi needed，spacial for array and struct
def deal_components(components):
    # recursive
    ## whthere component should be update
    for component in components:
        if not is_basic(component["type"]):
            deal_component(component, components)
    return component

def deal_component(component, components):
    if is_array(component["type"]):
        comname = component["type"][:len(component["type"]) - 2]
        component["type"] = "array"
        if is_basic(comname):
            nc = dict()
            nc["name"] = comname + "_item"
            nc["type"] = comname
            component["components"].append(nc)
        else:
            nc = dict()
            nc["name"] = comname + "_item"
            nc["type"] = comname
            nc["components"] = []
            deal_component(nc, components)
            component["components"].append(nc)
    elif is_basic(component["type"]):
        return
    elif component["type"] == "struct":
        for comp in component["components"]:
            deal_component(comp, components)
    else:
        # special struct,such as Transfer
        struct_name = component["type"]
        for item in components:
            if item["name"] == struct_name:
                component["type"] = "struct"
                component["components"] = item
                return

# deal arg with well form components to update the abi
# @return newarg
def deal_arg_with_components(components, arg):
    deal_component(arg, components)
    return arg

def is_basic(ty: str) -> bool:
    if ty == "uint64" or ty == "bool" or ty == "account":
        return True
    return False

def is_array(ty: str) -> bool:
    if len(ty) > 2 and ty[len(ty)-2:] == arr_flag:
        return True
    return False

if __name__ == "__main__":
    nabi = deal_abi(abi, components)
    print(json.dumps(nabi))
    print("=======================")
    print(json.dumps(components))
