rating_score_of_the_user=int(input('Please enter your rating score: '))
if (rating_score_of_the_user > 94) and (rating_score_of_the_user < 101):
    print('Your rate is excellent')
elif (rating_score_of_the_user > 84) and (rating_score_of_the_user < 95): 
    print('Your rate is very good')
elif (rating_score_of_the_user > 74) and (rating_score_of_the_user < 85):
    print('Your rate is good')
elif (rating_score_of_the_user > 64) and (rating_score_of_the_user < 75):
    print('Your rate is satisfactory')
elif (rating_score_of_the_user > 59) and (rating_score_of_the_user < 65):
    print('Your rate is marginal')
elif (rating_score_of_the_user > -1) and (rating_score_of_the_user < 60):
    print('Your rate is unsatisfactory')
else: 
    print('Error. Please note: You cannot enter negative numbers or numbers greater than 100')