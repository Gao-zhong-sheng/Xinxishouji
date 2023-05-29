import re

s = '2313-321312-3213213, 3213213-1231-3213-3'
print(re.findall(r'\d{4}-\d{6}-\d{7}', s))
