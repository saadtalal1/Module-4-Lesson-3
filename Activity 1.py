
student_data=  {

"student_ID1":{"Name":"Max","Class":9,"Subject integration":"Maths, Science, English"},
"student_ID2":{"Name":"Alex","Class":11,"Subject integration":"Maths, Science, English"},
"student_ID3":{"Name":"Alice","Class":8,"Subject integration":"Maths, Science, English"},
"student_ID4":{"Name":"Max","Class":9,"Subject integration":"Maths, Science, English"}}

result={}
seen_keys=[]

for i,j in student_data.items():
    unique_key=(j["Name"],j["Class"],j["Subject integration"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[i]=j
for k, v in result.items():
    print(k,":",v)