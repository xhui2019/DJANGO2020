import os
from pathlib import Path
path = os.path.join('aaa', 'bbbb')
print(path)
BASE_DIR1 = Path(__file__).resolve().parent.parent.parent.parent
BASE_DIR2 = Path(__file__).resolve().parent
BASE_DIR3 = Path(__file__).resolve()
BASE_DIR4 = Path(__file__)
print(BASE_DIR1, BASE_DIR2, BASE_DIR3, BASE_DIR4)
List = [1, 2, 3, 4, 5, 6, ]
print(List)
a = [
    1,
    2,
    3,
]
b = (1,
     2,
     3,
     4,
     )
c = {'a': 1,
     'c': [2,],
     'd'
     'ee': ['aa'],

}
print(a,b,c)