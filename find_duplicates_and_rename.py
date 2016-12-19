import re

dict = {}
for i in range(1, 10135):
    # os.remove('./data/'+str(i))
    # os.remove('./full_data/'+str(i))
    with open('./full_data/'+str(i), 'r') as f:
        old = f.read()
        review_name = re.search(r'<review_link>\n(.*?)\n', old).group(1)
        if review_name in dict.keys():
            dict[review_name].append(i)
        else:
            dict[review_name] = []
            dict[review_name].append(i)
for key in dict.keys():
    if len(dict[key]) > 1:
        print(dict[key])
