#javaScriptObjectNotation - json
import json
print(dir(json))
x ={ "name":"salma","age":27,"adrs":"abc"}
y = json.load(x)
print(y)