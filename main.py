#m4rc3lo - 04/01/2019
from load_csv import Load_csv 

enrollments_filename = '../../enrollments.csv'
engagement_filename  = '../../daily_engagement.csv'
submissions_filename = '../../project_submissions.csv'

file = Load_csv(enrollments_filename, 'rb')
enrollments = file.open() 

file = Load_csv (engagement_filename, 'rb')
daily_engagement = file.open() 

file = Lsoad_csv (enrollments_filename, 'rb')
project_submissions = file.open() 

#print (enrollments)