feedback_data = {
     's_no' : [1,2,3,4,5,6,7,8,9,10],
     'name' :['Ravi','meera','sam','anu','raj','divya','arjun','kiran','loris','nisha'] ,
     'feedback':[
          'very good service!!!',
          'poor support,not happy',
          'great experience! will come again.'
          'okay okay...',
          'not bad',
          'excellent care ,excellent staff!' ,
          'good food and good ambiance!',
          'poor response and poor handling of issue',
          'satisfied. butcould be better.',
          'good support...quick service,'
     ],
        'rating':[5,2,5,3,2,5,4,1,3,4]
}
print(feedback_data)
n = int(input("how many more feed backs do you want to add?"))
for i in range(n) :
    name =input("enter customer name:")
    feedback =input("enter feed back:")
    rating =int(input("enter rating(1-5):"))
    feedback_data['s_no']. append(len(feedback_data['s_no']) + 1)
    feedback_data['name'].append(name)
    feedback_data['feedback'].append(feedback)
    feedback_data['rating'].append(rating)
    print(feedback_data)   
cleaned_feedback =[]
for feedback in feedback_data['feedback']:
   feedback_cleaned = feedback .strip().lower ()
   cleaned_feedback .append(feedback_cleaned)
print("cleaned feed back :")  
print(cleaned_feedback) 
positive = 0
negative = 0
neutral  = 0
for rating in feedback_data['rating']:
    if rating >= 4:
        positive += 1
    elif rating <= 2:
        negative += 1
    else :
          neutral += 1
print("positive feedback:", positive)
print("negative feedback:", negative)
print("neutral feedback:" ,  neutral)
search_name =input("enter customer name to search:")
found = False
for i in range(len(feedback_data['name'])):
    if feedback_data['name'] [i].lower() == search_name.lower():
       print("feedback:" , feedback_data['feedback'] [i])
       print("rating:" , feedback_data['rating'] [i])
       found =True
if not found :
    print("customer not found")
highest_rating = max (feedback_data['rating'])
lowest_rating  = min (feedback_data['rating'])
print("highest rating:", highest_rating)
print("lowest rating:",lowest_rating)
cleaned_feedback =[]
for fb in feedback_data['feedback']:
  for char in["."," ," ,"!"," ?"]:
       fb = fb.replace (char,"")
       fb_cleaned = ' ' .join(fb.lower().split())
       cleaned_feedback.append(fb_cleaned)
       feedback_data['feedback'] = cleaned_feedback
       print("--- cleaned feedbacks ---")
       print(feedback_data['feedback'])
       def count_word_in_feedbacks(word):
           count =0
           for fb in feedback_data['feedback']:
               if word.lower() in fb.lower():
                   count += 1
               return  count
           print("number of feedbacks containing'good':",count_word_in_feedbacks("good"))
           print("number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
           print("number of feedbacks containing 'excellent'" ,count_word_in_feedbacks("excellent"))
           print("--- final cleaned feedback data ---")
           print(feedback_data)
           print("\n--- final cleaned feedback data---")  
           print(feedback_data) 
           total_rating = sum(feedback_data['rating'])
           total_feedback = len(feedback_data['rating'])
           average_rating = total_rating / total_feedback
           print("\noverall average rating:" ,round(average_rating,2))
           longest_feedback = max(feedback_data['feedback'], key=lambda x: len(x.split()))
           print("\nlongest feedback comment:", longest_feedback)
           unique_words = set
           for fb in feedback_data['feedback']:
               for word in fb.split():
                   unique_words.add(word)
               print("\nlist of unique words:")
               print(list(unique_words))
     
                 
    