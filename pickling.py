import pickle

dict1 = {"a": 100,
         "b": 200,
         "c": 300
         }

list1 = [400, 500, 600]

print("Objects about to be serialized:")
print(dict1)
print(list1)

fw = open("serialized_objects_file.pkl", 'wb')
pickle.dump(dict1, fw, pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, fw, pickle.HIGHEST_PROTOCOL)

fw.close()

fr = open("serialized_objects_file.pkl", 'rb')
dict2 = pickle.load(fr)
list2 = pickle.load(fr)

print("Diserialized objects: ")
print(dict2)
print(list2)







