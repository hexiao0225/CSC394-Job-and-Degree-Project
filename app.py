import random

from flask import Flask, current_app, render_template, request, jsonify

from config import app
from models import db, Keyword, Job, Degree, JobKeywords, DegreeKeywords, KeywordAnswer, KeywordQuestion


def dbJSON(obj):
    """
    Returns JSON format of database objects
    """
    json_obj = {'data': []}
    for entry in obj:
        tmp = {}
        for k,v in entry.__dict__.iteritems():
            if k != '_sa_instance_state': tmp[k] = v
        json_obj['data'].append(tmp)
    return jsonify(json_obj)


    """
        hard code the first page with degree titles for now.
    """

degreetitles = [
    {
        'id': 1,
        'degreetitle': u'Computer Science',
    },
    {
        'id': 2,
        'degreetitle': u'Information System',
    },
    {
        'id': 3,
        'degreetitle': u'Design',
    },
    {
        'id': 4,
        'degreetitle': u'Other',
    }
]

@app.route('/api/degreetitles',methods=['GET'])
def getDegreeTitles():
    degrees = Degree.query.all()
    return jsonify({'degreetitles': degreetitles})

@app.route('/api/jobtitles', methods=['GET'])
def getJobTitles():
    jobs = Job.query.all()
    return jsonfiy()

@app.route('/api/skills', methods=['GET'])
def retrieveSkills():
    """
    Retrieves all keywords based on target and title parameter
        i.e /api/skills?target=job&title=software%20developer
    Returns all keywords if no target and title is present
    """
    resp = {}
    target = request.args.get('target')
    title = request.args.get('title')
    if target == None and title == None:
        return dbJSON(Keyword.query.all())
    if target == 'job' and title != None:
        job_object = Job.query.filter_by(title=title).first()
        if job_object:
            resp[job_object.title] = []
            keys = JobKeywords.query.filter_by(jobID = job_object.id)
            for k in keys:
                tmp_key_obj = Keyword.query.get(k.keywordID)
                resp[job_object.title].append(tmp_key_obj.key)
            return jsonify(resp)
        return jsonify("Bad Request - title not found %s" % title)
    if target == 'degree' and title != None:
        degree_object = Degree.query.filter_by(title=title).first()
        if degree_object:
            resp[degree_object.title] = []
            keys = DegreeKeywords.query.filter_by(degreeID = degree_object.id)
            for k in keys:
                tmp_key_obj = Keyword.query.get(k.keywordID)
                resp[degree_object.title].append(tmp_key_obj.key)
            return jsonify(resp)
        return jsonify("Bad Request - title not found")
    return jsonify("Bad Request")

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
    return jsonify({'status':200, 'data': data})

@app.route('/', methods=['GET'])
def index():
    """
    Home Page / Survey View
    """
    return render_template('full.html')

@app.route('/about', methods=['GET'])
def about():
    """
    About Page view
    """
    return render_template('about.html')

@app.route('/calculate-results', methods=['POST'])
def calculateResults():
    """
    POST-only URL that retrieves survey results
    based on POSTed keywords
    """
    pass

@app.route('/email-results', methods=['POST'])
def emailResults():
    """
    POST-only URL for emailing survey results to user
    """
    pass

#For testing only, production will need a different server
if __name__ == '__main__':
    app.run(debug=True)
