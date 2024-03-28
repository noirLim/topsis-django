import math
from itertools import chain
# 1 mapping students
def map_by_id(students,alt):
    array_search = []
    for item in students:
        array_search = check_students_id(item,alt)
        item["alt"] = array_search

    return students

# check matching students id , return as array
def check_students_id(student,alt):
    new_arr = []
    for item in alt:
        if student["id"] == item["student__id"]:
            new_arr.append(item)
    return new_arr

# 2 normalize
def normalize(criteria_data,data_alternative,matriks):
    norm = []
    for item in criteria_data:
        angka = [ct["value"] ** 2 for ct in data_alternative if ct["criteria__id"] == item["id"]]
        norm.append({"criteria_id":item["id"],"res":math.sqrt(sum(angka))})

    new_res = []
    for item in matriks:
        value = normalize_mt(item,norm)
        new_res.append(value)

    return new_res
    

def normalize_mt(matriks,norm):
    for item in matriks["alt"]:
        for val in norm:
            if item["criteria__id"] == val["criteria_id"]:
                item["pow"] = item["value"] / val["res"]
    return matriks

# 3 weighted normalize
def calc_weighted(data,criteria_data):
    sum_of_weights = sum(item['weight'] for item in criteria_data)
    
    # simplify the weight
    for ct in criteria_data:
        ct["new_weight"] = ct["weight"] / sum_of_weights
    
    new_res = []
    for item in data:
        value = create_weight(item,criteria_data)
        new_res.append(value)
    
    return new_res 

def create_weight(res,criteria_data):
    for item in res["alt"]:
        for val in criteria_data:
            if item["criteria__id"] == val["id"]:
                item["new_weight"] = item["pow"] * val["new_weight"]
    return res

# 4 ideal solution
def find_ideal_solution(criteria_data,data):
    new_array = []
    for item in data:
        new_array.append(item["alt"])

    # flatten array
    flatten_arr = list(chain.from_iterable(new_array))
   
    for ct in criteria_data:
        angka = [dt for dt in flatten_arr if dt["criteria__id"] == ct["id"]]

        if ct["attribute"] == 'benefit':
           ct["positive"] = max(angka,key=lambda x:x["new_weight"])["new_weight"]
           ct["negative"] = min(angka,key=lambda x:x["new_weight"])["new_weight"]
        elif ct["attribute"] == 'cost':
           ct["positive"] = min(angka,key=lambda x:x["new_weight"])["new_weight"]
           ct["negative"] = max(angka,key=lambda x:x["new_weight"])["new_weight"]
    
    return criteria_data

# 5 distance ideal solution
def find_ideal_dis(data,new_criteria):
    new_res = []
    for item in data:
        value = calc_sol(item,new_criteria)
        new_res.append(value)

    return new_res

def calc_sol(item,criteria):
    pos = 0
    negative = 0
    for alt in item["alt"]:
        for ct in criteria:
            if alt["criteria__id"] == ct["id"]:
                pos += (alt["new_weight"] - ct["positive"])**2
                negative += (alt["new_weight"] - ct["negative"])**2
    
    item["positive"] = math.sqrt(pos)
    item["negative"] = math.sqrt(negative)
    item.pop("alt",None)
    return item

# 6 calculate preference and order by highest
def calc_preference(data):
    new_res = []
    for item in data:
       new_res.append({ 
           "student_id" : item["id"],
           "value":item["negative"] / (item["negative"] + item["positive"])
           }
       )
    
    return sorted(new_res,key=lambda x:x["value"],reverse=True)

# topsis formula
def calc_topsis(data_alternative,criteria_data,students_data):
    # 1 get_students by id
    matriks = map_by_id(students_data,data_alternative)
    
    # 2 normalize
    norm_normalize = normalize(criteria_data,data_alternative,matriks)
    
    # 3 weighted normalization
    weighted_norm = calc_weighted(norm_normalize,criteria_data)
    
    # 4 ideal solution
    new_criteria = find_ideal_solution(criteria_data,weighted_norm)
    
    # 5 ideal solutin distance
    find_ideal_sol = find_ideal_dis(weighted_norm,new_criteria)
    
    # 6 calc preference and give ranking by highest
    return calc_preference(find_ideal_sol)

def create_html_excel(data):
    html = """<table>\n<tr>\n"""

    for key, value in data["custom_labels"].items():
      html += f'<th>{value}</th>\n'

    html += '<tr/>\n'


    # isikan nilai ke dalam baris
    for index, dt in enumerate(data["data"]):
        html += f'<tr>\n<td>{index+1}</td>\n<td>{dt["student__name"]}</td>\n<td>{dt["value"]}</td>\n</tr>\n'

    html += '</table>'
    return html