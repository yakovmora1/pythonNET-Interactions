import clr

# Import .NET libraries classes here:
"""
    Note: we first must import clr so it will load the CLR which makes
     the .NET environment available at runtime for us here in python.
     Then, it can Resolve direct imports of .NET classes (from GAC).
     Python.NET uses reflection to discover the .NET types
    and make them available in the Python runtime.
"""
from System.Collections.Generic import Dictionary
from System import Int32
from System.Reflection import BindingFlags



def call_net_func():
    #Add Aseembly TestLib.dll
    clr.AddReference("TestLib")

    #import from our library in the dll
    from TestLib import SecretOpCaller, SecretOp
    
    sec_op_obj = SecretOp(1337, 33)

    # Try computeInternal func
    result = sec_op_obj.computeInternal()

    print(f"The result is : {result}")

    #Try readFile func
    file_data = sec_op_obj.readFile("./test.exe")

    file_data_len = int(len(file_data) / 10)
    print(f"The first {file_data_len} bytes of data is {file_data[: file_data_len]}")

    #Try passing a pytohn dict to  C# function receives Dictionary<String, int>
    my_dict = {'a' : 111, 'b': 35, 'c': 3525}
    wrong_dict = {'a' : 111, 'b': 35, 'c': 3525, 'h' : "afaf"} 

    new_dict = Dictionary[str, int]()
    for key, val in my_dict.items():
        new_dict[key] = val
    
    result = sec_op_obj.complexDictionaryFunc(new_dict)
    print(f"The complex function result is: {result}")

    try:
        new_dict = Dictionary[str, int]()
        for key, val in wrong_dict.items():
            new_dict[key] = val

        result = sec_op_obj.complexDictionaryFunc(new_dict)
        print(f"The complex function result for wrong_dict is: {result}")
    except Exception as e:
        print(e)
    
    # Try passing an object as an argument
    sec_op_caller = SecretOpCaller()
    result = sec_op_caller.computeWrapper(sec_op_obj)

    print(f"The SecOpCaller result is : {result}")


def invoke_private_method(privat_method_name):
    #Add Aseembly TestLib.dll (we get a RuntimeAssembly Claass from Reflection)
    library = clr.AddReference("TestLib")

    from TestLib import SecretOp

    # Get the type object of the SecretOp class
    secretop_type = library.GetType("TestLib.SecretOp")
    #search for instace and private methods in the current Type
    methods = secretop_type.GetMethods(BindingFlags.NonPublic | BindingFlags.Instance)

    for method in methods:
        print(f"NonPublic Method: {method.Name}")

    #get the RuntimeMethodInfo object
    get_secret_val_method = secretop_type.GetMethod(privat_method_name, BindingFlags.NonPublic | BindingFlags.Instance)
    if get_secret_val_method == None:
        # We didn't find our private method
        raise TypeError(f"Method  {privat_method_name} not found!")

    print(f"Is {privat_method_name} is private: {get_secret_val_method.IsPrivate}") 

    # show its parameters
    parameters = get_secret_val_method.GetParameters()
    for param in parameters:
        print(f"Parameter {param.Position} name: {param.Name} , type: {param.ParameterType}")

    sec_op_instance = SecretOp(5, 5)

    #We can pass array argument as python array (it works)
    result = get_secret_val_method.Invoke(sec_op_instance, [Int32(555)])

    print(f"{privat_method_name} result is: {result}")



if __name__ == "__main__":
    #call_net_func()
    invoke_private_method("getSecretValue")