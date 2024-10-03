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



def call_net_func():
    clr.AddReference("TestLib")

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

if __name__ == "__main__":
    call_net_func()