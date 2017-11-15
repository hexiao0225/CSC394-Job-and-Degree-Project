import random

from flask import Flask, current_app, render_template, request, jsonify

from config import app
from models import db, Keyword, Job, Degree, JobKeywords, DegreeKeywords, KeywordAnswer, KeywordQuestion

@app.route('/', methods=['GET'])
def index():
    """
    Return Home Page
    """
    return render_template('full.html')

#STEP ONE
@app.route('/api/titles', methods=['GET'])
def getTitles():
    """
    Return JSON list of titles for Jobs or Degrees based on target parameter in URL

    Degree titles
    /api/titles?target=degree

    Job titles
    /api/titles?target=job
    """
    resp = []
    target = request.args.get('target') # 'job' or 'degree'
    if target == 'degree':
        degrees = Degree.query.all()
        for d in degrees:
            resp.append(d.title)
    elif target == 'job':
        jobs = Job.query.all()
        for j in jobs:
            resp.append(j.title)
    return jsonify(resp)

# STEP TWO
@app.route('/api/skills', methods=['GET'])
def getSkills():
    """
    Retrieves all keywords based on target and title parameter
        i.e /api/skills?target=job&title=software%20developer
    Returns all keywords if no target and title is present
    """
    resp = []
    target = request.args.get('target')
    title = request.args.get('title')
    if target == None and title == None:
        skills = Keyword.query.all()
        for s in skills:
            resp.append(s.key)
        return jsonify(resp)
    if target == 'job' and title != None:
        job_object = Job.query.filter_by(title=title).first()
        if job_object:
            keys = JobKeywords.query.filter_by(jobID = job_object.id)
            for k in keys:
                tmp_key_obj = Keyword.query.get(k.keywordID)
                resp.append(tmp_key_obj.key)
            return jsonify(resp)
        return jsonify("Bad Request - title not found %s" % title)
    if target == 'degree' and title != None:
        degree_object = Degree.query.filter_by(title=title).first()
        if degree_object:
            keys = DegreeKeywords.query.filter_by(degreeID = degree_object.id)
            for k in keys:
                tmp_key_obj = Keyword.query.get(k.keywordID)
                resp.append(tmp_key_obj.key)
            return jsonify(resp)
        return jsonify("Bad Request - title not found")
    return jsonify("Bad Request")

# STEP THREE
@app.route('/api-new/questions', methods=['GET'])
def getQuestionsNEW():
    """
    GET questions
    """
    skills = request.args.get('skills') # skills here should be an array of skills

    # implementation

    return jsonify(
        [
            {
                'id': 'some id for internal identification purpose',
                'Question':'Question 1 Text',
                'Options': ['Option 1','Option 2','Option 3','Option 4']
            },
            {
                'id': 'some id for internal identification purpose',
                'Question':'Question 2 Text',
                'Options': ['Option 1','Option 2','Option 3','Option 4']
            },
            {
                'id': 'some id for internal identification purpose',
                'Question':'Question 3 Text',
                'Options': ['Option 1','Option 2','Option 3','Option 4']
            },
            {
                'id': 'some id for internal identification purpose',
                'Question':'Question 4 Text',
                'Options': ['Option 1','Option 2','Option 3','Option 4']
            }
        ]
    )

def getRandomQuestion(skill):
    keyword_obj = Keyword.query.filter_by(key=skill).first()
    question_obj = KeywordQuestion.query.filter_by(keywordID = keyword_obj.id)
    item_count = len(list(question_obj))
    q_num = random.randint(0, item_count-1)
    question_obj = question_obj[q_num]
    response_obj = KeywordAnswer.query.filter_by(questionID=question_obj.id)

@app.route('/api/question', methods=['GET'])
def retrieveQuestion():
    """
    Retrieves question and answer based on skill parameter
        i.e /api/question?skill=csharp
    """
    skill = request.args.get("skill")
    if skill == None:
        return jsonify("Bad Request")
    keyword_obj = Keyword.query.filter_by(key=skill).first()
    question_obj = KeywordQuestion.query.filter_by(keywordID = keyword_obj.id)
    item_count = len(list(question_obj))
    q_num = random.randint(0, item_count-1)
    question_obj = question_obj[q_num]
    response_obj = KeywordAnswer.query.filter_by(questionID=question_obj.id)
    answer = ""
    options = []
    for o in response_obj:
        options.append(o.answer)
        if o.correct == True:
            answer = o.answer
    data = {}
    data['question'] = question_obj.question
    data['options'] = options
    data['answer'] = answer
    return jsonify(data)





#For testing only, production will need a different server
if __name__ == '__main__':
    app.run(debug=True)
