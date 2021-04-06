
def convertListtostring(comingList):
    listLength=len(comingList);
    result="";
    for i in range(listLength):
        if i==listLength-1:
            result+="and "+comingList[i];
        else:
            result+=comingList[i]+", ";
    return result;


print(convertListtostring(['apples', 'bananas', 'tofu', 'cats']));
            
        
        
    
