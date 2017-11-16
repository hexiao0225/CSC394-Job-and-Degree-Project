import random

from flask import Flask, current_app, render_template, request, jsonify, json

from config import app
from models import db, Keyword, Job, Degree, JobKeywords, DegreeKeywords, KeywordAnswer, KeywordQuestion
from algo import recomend

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
@app.route('/api/questions', methods=['POST'])
def getQuestions():
    """
    GET questions
    """
    data = request.values
    skills = []
    for s in data:
        skills.append(str(data[s]))
    questions = getRandomQuestionList(skills)
    return jsonify(questions)


def getRandomQuestionList(skillList):
    resp = []
    for skill in skillList:
        keyword_obj = Keyword.query.filter_by(key=skill).first()
        question_obj = KeywordQuestion.query.filter_by(keywordID = keyword_obj.id)
        item_count = len(list(question_obj))
        if keyword_obj == None or question_obj == None or item_count == 0:
            continue
        q_num = random.randint(0, item_count-1)
        question_obj = question_obj[q_num]
        response_obj = KeywordAnswer.query.filter_by(questionID=question_obj.id)
        correctAnswer = ""
        answers = []
        for k in response_obj:
            if k.correct == True:
                correctAnswer = str(k.answer)
            answers.append(str(k.answer))
        jsonResponse = {}
        jsonResponse['skill'] = str(skill)
        jsonResponse['question'] = str(question_obj.question)
        jsonResponse['answers'] = answers
        jsonResponse['correctAnswer'] = correctAnswer
        resp.append(jsonResponse)
    return resp

@app.route("/api/results", methods=['POST'])
def getResults():
    print request.values.values()
    return jsonify(recomend(request.values.values(), "job"))


#For testing only, production will need a different server
if __name__ == '__main__':
    app.run(debug=True)
