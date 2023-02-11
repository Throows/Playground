import MyPyApp

def runScript(datas : MyPyApp):
    print("Running script")
    error = 0
    id = datas.getId()
    print("The object ID is: {}".format(id))
    datas.setName("MyPyApp")
    return error