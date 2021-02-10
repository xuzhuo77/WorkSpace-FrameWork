a=["date",
"week",
"dayInfo",
"dayImg",
"dayWindDirect",
"dayWindPower",
"dayTemperature",
"neightTemperature",
"nightInfo",
"nightImg",
"neightWindDirect",
"neightWindPower",
]

def makeA(a):
    t=[
    "String",
    a,
        '= dayData.findPath(',
        '"'+"day"+'"' if a.startswith("day") else '"'+"night"+'"',
        ').findParent("',
        '").findValue("',
        '").asText();'
    ]
    return " ".join(t)
def makeB(a):

    t=[
        "info.set"+a[0].upper()+a[1:],

        "(formatValue(",
            a,
        "));",

    ]
    return " ".join(t)

def makeC(a):
    t=[
        "private String ",
        a,
        ";"


    ]
    return "".join(t)

for t in a :
    print(makeA(t))
for t in a:
    print(makeB(t))
for t in a:
    print(makeC(t))

print(any(['a', 'b', 'c', 'd']))
print(any(['a', '', 'c', 'd']))
print(any([ 0, '', False]))

print(all(['a', 'b', 'c', 'd']))
print(all(['a', '', 'c', 'd']))
print(all(['', 0, '', False]))
print()
s = ' hello world '
vvv='和'
k="张三{s}李四{vvv}王五"
print(k.format_map(locals()))