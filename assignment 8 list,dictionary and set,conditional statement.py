age_list =[22,25,26,27,28]
name_list =["alice","bob","charlie","yazhini","david"]
name_list.append("yazhini")
age_list.insert(2,30)
name_list.remove("yazhini")
age_list.pop()
age_list.extend([29,30,26])
age_list.sort(reverse=True)
max_age =max(age_list)
min_age =min(age_list)
sum_age =sum(age_list)
print("(max age:", max_age, ", min age:", min_age, ", sum:", sum_age)
print("first element:",name_list[0])
print("last element:",name_list[-1])
print("elements from index 2 to 4:",name_list[2:5])
print("reverse order:",name_list[::-1])
student_marks ={"rahul":85,"ananya":90,"kiran":78,"sneha":92,"arjun":74}
print("marks of ananya:",student_marks["ananya"])
student_marks["janani"] =80
student_marks["kiran"] =82
my_set ={'a','e','i','o','u','a','a','i'}
print("my_set:",my_set)
set1 ={1,3,5,7,9}
set2 ={2,3,5,8,10}
print("union:",set1.union(set2))
print("intersection:",set1.intersection(set2))
score = 7
if score > 7 and score <=10:
    


    print ("above average: excellent work! you have mastered the concepts.")
elif score >=4 and score <= 7:
    print("average:good effort! keep practicing there's room for improvement.")
elif score >=0 and score <4:
    print("below average: need to improve your performance, consistant practice will lead  to better results.")
else:
    print("invalid score ! please enter a value between 0 and 10.")