from models import db, Job, Keyword, Degree, JobKeywords, DegreeKeywords



#Add all the titles to the lists, just the titles
jobs = []




degrees = []





keywords = []







#Loading Loops for adding data to the database quickly
for j in jobs:
    tmp = Job(title="%s" % j.lower())
    db.session.add(tmp)
db.session.commit()

for d in degrees:
    tmp = Degree(title="%s" % d.lower())
    db.session.add(tmp)
db.session.commit()

for k in keywords:
    tmp = Keyword(key="%s" % k.lower())
db.session.commit()
