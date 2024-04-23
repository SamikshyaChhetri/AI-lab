# Implementing goal based agent
# path = ['AB', 'BD', 'AC', 'CD', 'AD']

# AB, BD, AC, CD, AD = [60, 5, 13, 21, 85]
AB, BD, AC, CD, AD = [30, 5, 53, 41, 85]

print(AB, BD, AC, CD, AD,)
# print(f'''
#    {AB}         {BD}
# A-----------B------------D

#             {AD}
# A-------------------------D
#     {AC}        {CD}
# A-----------C-------------D
# ''')

# Visual representation of the path
print(f'''
       {AB}
A----------------B
|\               |
| \              |
|  \             |
|   \            |
|    \           |
|     \          |
|      \         |
|       \        |
|        \       |
|{AC}       \{AD}    |{BD}
|          \     |
|           \    |
|            \   |
|             \  | 
|    {CD}        \ |
C---------------D           
''')

# if path is fixed then calculation possible routes
path1 = AB+BD
path2 = AC+CD
path3 = AD
# minimum value is the shortest path that agent could visit and reach the goal
shortPath = min(path1, path2, path3)


print(f'''
AC-CD = {AC}+{CD} = {AC+CD}
AB-BD = {AB}+{BD} = {AB+BD}
AD = {AD}

''')
print(f'Shortest Path is AB-BD={path1}') if shortPath == path1 else print(
    f'Shortest Path is AC-CD = {AC}+{CD} = {AC+CD}') if shortPath == path2 else print(f'Shortest path is AD={AD}')
