from flask import Flask
import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    str_candidates += "<pre>"
    return str_candidates


@app.route("/candidates/<int:_id>")
def profile(_id):
    candidate = candidates[_id]
    str_candidates = "<pre>"
    str_candidates += f"{candidate['picture']}\n\n{candidate['position']}\n{candidate['skills']}\n"
    str_candidates += "<pre>"
    return str_candidates


@app.route("/skills/<skill>")
def skills(skill):
    str_candidate = "<pre>"
    for candidate in candidates.values():
        candidate_skills = candidate["skills"].split(", ")
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidate += f"{candidate['name']}\n\n{candidate['position']}\n{candidate['skills']}\n\n"
    str_candidate += "<pre>"
    return str_candidate


app.run()
