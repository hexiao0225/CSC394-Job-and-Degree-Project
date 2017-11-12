# coding: utf-8

from models import db, Job, Keyword, Degree, JobKeywords, DegreeKeywords, KeywordQuestion, KeywordAnswer

"""
ALREADY IN PROD. - DO NOT RUN AGAIN


Keeping this file is just in case we need
to reset the db at anytime
"""
db.drop_all()
db.create_all()

print "Adding sample Degrees..."
d_a = Degree(title="computer science")
d_b = Degree(title="data science")
d_c = Degree(title="human computer interaction")
d_d = Degree(title="predictive analytics")
d_e = Degree(title="software engineering")

print "Adding sample Jobs..."
j_a = Job(title="software developer")
j_b = Job(title="web developer")
j_c = Job(title="data scientist")
j_d = Job(title="network engineer")
j_e = Job(title="database administrator")

print "Adding sample Keywords..."
k_a = Keyword(key="algorithms")
k_b = Keyword(key="object-oriented programming")
k_c = Keyword(key="system architecture")
k_d = Keyword(key="creative design")
k_e = Keyword(key="databases")
k_f = Keyword(key="data visualization")
k_g = Keyword(key="uml")
k_h = Keyword(key="front-end")
k_i = Keyword(key="back-end")
k_j = Keyword(key="ui ux")

k_k = Keyword(key="csharp")
k_l = Keyword(key="css")
k_m = Keyword(key="objective-c")
k_n = Keyword(key="perl")
k_o = Keyword(key="r")
k_p = Keyword(key="scala")
k_q = Keyword(key="typescript")


print "Staging sample Degrees, Jobs, and Keywords..."
db.session.add(d_a)
db.session.add(d_b)
db.session.add(d_c)
db.session.add(d_d)
db.session.add(d_e)

db.session.add(j_a)
db.session.add(j_b)
db.session.add(j_c)
db.session.add(j_d)
db.session.add(j_e)

db.session.add(k_a)
db.session.add(k_b)
db.session.add(k_c)
db.session.add(k_d)
db.session.add(k_e)
db.session.add(k_f)
db.session.add(k_g)
db.session.add(k_h)
db.session.add(k_i)
db.session.add(k_j)

db.session.add(k_k)
db.session.add(k_l)
db.session.add(k_m)
db.session.add(k_n)
db.session.add(k_o)
db.session.add(k_p)
db.session.add(k_q)

print "Pushing to database..."
db.session.commit()

print "Adding sample Degree-Keywords..."
dk_1 = DegreeKeywords(keywordID=k_b.id, degreeID=d_a.id)
dk_2 = DegreeKeywords(keywordID=k_e.id, degreeID=d_a.id)
dk_3 = DegreeKeywords(keywordID=k_i.id, degreeID=d_a.id)
dk_4 = DegreeKeywords(keywordID=k_e.id, degreeID=d_b.id)
dk_5 = DegreeKeywords(keywordID=k_a.id, degreeID=d_b.id)
dk_6 = DegreeKeywords(keywordID=k_f.id, degreeID=d_b.id)
dk_7 = DegreeKeywords(keywordID=k_d.id, degreeID=d_c.id)
dk_8 = DegreeKeywords(keywordID=k_h.id, degreeID=d_c.id)
dk_9 = DegreeKeywords(keywordID=k_j.id, degreeID=d_c.id)
dk_10 = DegreeKeywords(keywordID=k_a.id, degreeID=d_d.id)
dk_11 = DegreeKeywords(keywordID=k_b.id, degreeID=d_d.id)
dk_12 = DegreeKeywords(keywordID=k_f.id, degreeID=d_d.id)
dk_13 = DegreeKeywords(keywordID=k_b.id, degreeID=d_e.id)
dk_14 = DegreeKeywords(keywordID=k_c.id, degreeID=d_e.id)
dk_15 = DegreeKeywords(keywordID=k_g.id, degreeID=d_e.id)

print "Adding sample Job-Keywords..."
jk_1 = JobKeywords(keywordID=k_b.id, jobID=j_a.id)
jk_2 = JobKeywords(keywordID=k_c.id, jobID=j_a.id)
jk_3 = JobKeywords(keywordID=k_i.id, jobID=j_a.id)
jk_4 = JobKeywords(keywordID=k_d.id, jobID=j_b.id)
jk_5 = JobKeywords(keywordID=k_h.id, jobID=j_b.id)
jk_6 = JobKeywords(keywordID=k_j.id, jobID=j_b.id)
jk_7 = JobKeywords(keywordID=k_a.id, jobID=j_c.id)
jk_8 = JobKeywords(keywordID=k_i.id, jobID=j_c.id)
jk_9 = JobKeywords(keywordID=k_f.id, jobID=j_c.id)
jk_10 = JobKeywords(keywordID=k_c.id, jobID=j_d.id)
jk_11 = JobKeywords(keywordID=k_i.id, jobID=j_d.id)
jk_12 = JobKeywords(keywordID=k_g.id, jobID=j_d.id)
jk_13 = JobKeywords(keywordID=k_c.id, jobID=j_e.id)
jk_14 = JobKeywords(keywordID=k_e.id, jobID=j_e.id)
jk_15 = JobKeywords(keywordID=k_i.id, jobID=j_e.id)

print "Staging keyword relationships..."
db.session.add(dk_1)
db.session.add(dk_2)
db.session.add(dk_3)
db.session.add(dk_4)
db.session.add(dk_5)
db.session.add(dk_6)
db.session.add(dk_7)
db.session.add(dk_8)
db.session.add(dk_9)
db.session.add(dk_10)
db.session.add(dk_11)
db.session.add(dk_12)
db.session.add(dk_13)
db.session.add(dk_14)
db.session.add(dk_15)

db.session.add(jk_1)
db.session.add(jk_2)
db.session.add(jk_3)
db.session.add(jk_4)
db.session.add(jk_5)
db.session.add(jk_6)
db.session.add(jk_7)
db.session.add(jk_8)
db.session.add(jk_9)
db.session.add(jk_10)
db.session.add(jk_11)
db.session.add(jk_12)
db.session.add(jk_13)
db.session.add(jk_14)
db.session.add(jk_15)

print "Pushing Relationships to database..."
db.session.commit()

print "Adding Question objects..."
q_a = KeywordQuestion(keywordID=k_k.id, question="How many Bytes are stored by 'Long' Datatype in C-sharp .net?")
q_b = KeywordQuestion(keywordID=k_k.id, question="Arrange the following datatype in order of increasing magnitude sbyte, short, long, int")
q_c = KeywordQuestion(keywordID=k_k.id, question="Correct way to assign values to variable ‘c’ when int a = 12, float b = 3.5, int c")

q_d = KeywordQuestion(keywordID=k_l.id, question="______ selectors, which are used to specify a rule to bind to a particular unique element")
q_e = KeywordQuestion(keywordID=k_l.id, question="______ selectors, which are used to specify a group of elements")
q_f = KeywordQuestion(keywordID=k_l.id, question="In css what does h1 can be called as")

q_g = KeywordQuestion(keywordID=k_m.id, question='What does this code produce? [NSString] *myString = @“Hello World”;')
q_h = KeywordQuestion(keywordID=k_m.id, question="What does an Objective-C string literal look like?")
q_i = KeywordQuestion(keywordID=k_m.id, question= "What is the type of @selector(foo)?")

q_j = KeywordQuestion(keywordID=k_n.id, question='The “%” in Perl is used for')
q_k = KeywordQuestion(keywordID=k_n.id, question="Arrays are denoted by _____ in Perl")
q_l = KeywordQuestion(keywordID=k_n.id, question="Which of the following is used in perl?")

q_m = KeywordQuestion(keywordID=k_o.id, question="Numbers in R are generally treated as _____ precision real numbers.")
q_n = KeywordQuestion(keywordID=k_o.id, question="Which of the following can be considered as object attribute?")
q_o = KeywordQuestion(keywordID=k_o.id, question="____ function returns a vector of the same size as x with the elements arranged in increasing order")

q_p = KeywordQuestion(keywordID=k_p.id, question="What type (if any) does the following Scala expression have? List (None, Some (List (Some (1), None, Some (2))))")
q_q = KeywordQuestion(keywordID=k_p.id, question="What is the result of evaluating the following Scala code? List(1,2,3,4,5,6,7,8,9,10).map ((x:Int) => x*2).filter ((x:Int) => (x%2) == 0)")
q_r = KeywordQuestion(keywordID=k_p.id, question="Suppose we evaluate the following Scala expression (1 :: 2 :: 3 :: Nil) ::: (4 :: 5 :: 6 :: Nil) How many cons cells are there in the result?")

q_s = KeywordQuestion(keywordID=k_q.id, question="Typescript is developed under")
q_t = KeywordQuestion(keywordID=k_q.id, question="Typescript provides type checking at")
q_u = KeywordQuestion(keywordID=k_q.id, question="For anonymous functions typescript use")

print "Staging Questions..."
db.session.add(q_a)
db.session.add(q_b)
db.session.add(q_c)
db.session.add(q_d)
db.session.add(q_e)
db.session.add(q_f)
db.session.add(q_g)
db.session.add(q_h)
db.session.add(q_i)
db.session.add(q_j)
db.session.add(q_k)
db.session.add(q_l)
db.session.add(q_m)
db.session.add(q_n)
db.session.add(q_o)
db.session.add(q_p)
db.session.add(q_q)
db.session.add(q_r)
db.session.add(q_s)
db.session.add(q_t)
db.session.add(q_u)

print "Pushing to Databse..."
db.session.commit()

print "Adding all answers..."
a_1 = KeywordAnswer(questionID=q_a.id, answer="8", correct=True)
a_2 = KeywordAnswer(questionID=q_a.id, answer="4")
a_3 = KeywordAnswer(questionID=q_a.id, answer="2")
a_4 = KeywordAnswer(questionID=q_a.id, answer="1")

a_5 = KeywordAnswer(questionID=q_b.id, answer="long < short < int < sbyte", correct=True)
a_6 = KeywordAnswer(questionID=q_b.id, answer="sbyte < short < int < long")
a_7 = KeywordAnswer(questionID=q_b.id, answer="short < int < sbyte < long")
a_8 = KeywordAnswer(questionID=q_b.id, answer="short < sbyte < int < long")

a_9 = KeywordAnswer(questionID=q_c.id, answer="c = a + convert.ToInt32( b )", correct=True)
a_10 = KeywordAnswer(questionID=q_c.id, answer="c = a + int( float( b ) )")
a_11 = KeywordAnswer(questionID=q_c.id, answer="c = a + b")
a_12 = KeywordAnswer(questionID=q_c.id, answer="c = int( a + b )")

a_13 = KeywordAnswer(questionID=q_d.id, answer="id", correct=True)
a_14 = KeywordAnswer(questionID=q_d.id, answer="class") 
a_15 = KeywordAnswer(questionID=q_d.id, answer="tag")
a_16 = KeywordAnswer(questionID=q_d.id, answer="both class and tag") 

a_17 = KeywordAnswer(questionID=q_e.id, answer="class", correct=True)
a_18 = KeywordAnswer(questionID=q_e.id, answer="id")
a_19 = KeywordAnswer(questionID=q_e.id, answer="tag")
a_20 = KeywordAnswer(questionID=q_e.id, answer="class and tag")

a_21 = KeywordAnswer(questionID=q_f.id, answer="Selector", correct=True)
a_22 = KeywordAnswer(questionID=q_f.id, answer="Attribute")
a_23 = KeywordAnswer(questionID=q_f.id, answer="Value")
a_24 = KeywordAnswer(questionID=q_f.id, answer="Tag")

a_25 = KeywordAnswer(questionID=q_g.id, answer="An error during compile", correct=True)
a_26 = KeywordAnswer(questionID=q_g.id, answer="Makes the pointer to myString equal to the pointer of the created object with @"\"Hello World\"")
a_27 = KeywordAnswer(questionID=q_g.id, answer="Gets SIGABRT while executing the application")
a_28 = KeywordAnswer(questionID=q_g.id, answer="It put the value Hello World into a string named myString")

a_29 = KeywordAnswer(questionID=q_h.id, answer="@\"foo\"", correct=True)
a_30 = KeywordAnswer(questionID=q_h.id, answer="foo")
a_31 = KeywordAnswer(questionID=q_h.id, answer="#\"foo\"")
a_32 = KeywordAnswer(questionID=q_h.id, answer="NSString("\"foo\"")

a_33 = KeywordAnswer(questionID=q_i.id, answer="SEL", correct=True)
a_34 = KeywordAnswer(questionID=q_i.id, answer="id")
a_35 = KeywordAnswer(questionID=q_i.id, answer="selector")
a_36 = KeywordAnswer(questionID=q_i.id, answer="None, that is not a valid Objective-C expression")

a_37 = KeywordAnswer(questionID=q_j.id, answer="Hash variable", correct=True)
a_38 = KeywordAnswer(questionID=q_j.id, answer="Scalar variables") 
a_39 = KeywordAnswer(questionID=q_j.id, answer="Arrays") 
a_40 = KeywordAnswer(questionID=q_j.id, answer="Subroutines") 

a_41 = KeywordAnswer(questionID=q_k.id, answer="@", correct=True)
a_42 = KeywordAnswer(questionID=q_k.id, answer="%") 
a_43 = KeywordAnswer(questionID=q_k.id, answer="$") 
a_44 = KeywordAnswer(questionID=q_k.id, answer="#")

a_45 = KeywordAnswer(questionID=q_l.id, answer="elsif", correct=True)
a_46 = KeywordAnswer(questionID=q_l.id, answer="else if") 
a_47 = KeywordAnswer(questionID=q_l.id, answer="elseif") 
a_48 = KeywordAnswer(questionID=q_l.id, answer="elif") 


db.session.add(a_1)
db.session.add(a_2)
db.session.add(a_3)
db.session.add(a_4)
db.session.add(a_5)
db.session.add(a_6)
db.session.add(a_7)
db.session.add(a_8)
db.session.add(a_9)
db.session.add(a_10)
db.session.add(a_11)
db.session.add(a_12)
db.session.add(a_13)
db.session.add(a_14)
db.session.add(a_15)
db.session.add(a_16)
db.session.add(a_17)
db.session.add(a_18)
db.session.add(a_19)
db.session.add(a_20)
db.session.add(a_21)
db.session.add(a_22)
db.session.add(a_23)
db.session.add(a_24)
db.session.add(a_25)
db.session.add(a_26)
db.session.add(a_27)
db.session.add(a_28)
db.session.add(a_29)
db.session.add(a_30)
db.session.add(a_31)
db.session.add(a_32)
db.session.add(a_33)
db.session.add(a_34)
db.session.add(a_35)
db.session.add(a_36)
db.session.add(a_37)
db.session.add(a_38)
db.session.add(a_39)
db.session.add(a_40)
db.session.add(a_41)
db.session.add(a_42)
db.session.add(a_43)
db.session.add(a_44)
db.session.add(a_45)
db.session.add(a_46)
db.session.add(a_47)
db.session.add(a_48)


db.session.commit()

print "Finished"
