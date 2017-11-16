"""

TODO
    - Write Tests
    - Actually Test
    - Find way to combine get___References
    - Write into Class?
    - Change findMax to findTop3
"""

from models import Keyword, Job, Degree, JobKeywords, DegreeKeywords

def recomend(keywords, target="job"):
    key_ids = []
    for k in keywords:
        key_obj = Keyword.query.filter_by(key=k).first() #could be optimized by having the ID's sent back instead of the actual keyword
        key_ids.append(key_obj.id)
    if target == "job":
        store = getJobReferences()
    elif target == "degree":
        store = getDegreeReferences()
    return maxfind(store)


def getJobReferences(keywordIDs):
    store = {}
    for k_id in keywordIDS:
        jobIDs_by_keyword = [q.jobID for q in JobKeywords.query.filter(keywordID=k_id)]
        for job_id in jobIDs_by_keyword:
            if job_id not in store.keys():
                store[job_id] = 1
            else:
                store[job_id]+=1
    return store

def getDegreeReferences(keywordIDs):
    store = {}
    for k_id in keywordIDS:
        degreeIDs_by_keyword = [q.degreeID for q in DegreeKeywords.query.filter(keywordID=k_id)]
        for degree_id in degreeIDs_by_keyword:
            if degree_id not in store.keys():
                store[degree_id] = 1
            else:
                store[degree_id]+=1
    return store


def maxfind(store):
    """
    Returns key and max val from hashmap
    """
    topkey = 0
    topval = None
    for k,v in store.iteritems():
        if v > topval:
            topval = v
            topkey = k
    return topkey
