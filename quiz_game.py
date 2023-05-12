# In this mini project you will answer the questions and get a score

print('Ready for the game?')
question = input('First, no forces but Do you wanna play a game? ')

if question.lower() != 'yes':
    quit()

print('YES')
print('Okay! lets play then')
score = 0

q1 = input('What does CPU stand for ? ')
if q1 == 'Central Processing Unit':
    print('Yup! Correct')
    score += 1
else:
    print('Incorrect')

q2 = input('Say one BI tool ')
if q2 == 'Power BI' :
    print('Yup! Correct')
elif q2 == 'Tableau':
    print('Yup! Correct')
elif q2 == 'SAP Business Objects':
    print('Yup! Correct')
elif q2 == 'MicroStrategy':
    print('Yup! Correct')
elif q2 == 'QlikSense':
    print('Yup! Correct')
elif q2 == 'Looker':
    print('Yup! Correct')
elif q2 == 'Cognos':
    print('Yup! Correct')
    score += 1
else:
    print('Incorrect')

q3 = input('What does RAM stand for ? ')
if q3 == 'Random Access Memory':
    print('Yup! Correct')
    score += 1
else:
    print('Incorrect')

q4 = input('What does SQL stand for ? ')
if q4 == 'Structured Query Language':
    print('Yup! Correct')
    score += 1
else:
    print('Incorrect')

print('You got ' + str(score) + ' questions correct')
print('The percentage is ' + str(score/4 *100) + '%.')