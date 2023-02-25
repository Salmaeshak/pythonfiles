dict1 = {"Maths":98,"English":90,"Physics":92,"Chemistry":89,"Biology":97}
print("SUBJECTS"'\t\t\t\t\t\t\t'"MARKS"'\n')
for key,value in dict1.items():
    if key =="Maths":
        print(key,'\t\t\t\t\t\t\t\t',value)
    else:
        print(key,'\t\t\t\t\t\t\t',value)