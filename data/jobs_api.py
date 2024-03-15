import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('job', 'team_leader', 'worksize', 'start_date')) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_one_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('job', 'team_leader', 'worksize', 'start_date'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'worksize', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    news = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        worksize=request.json['worksize'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'id': news.id})
