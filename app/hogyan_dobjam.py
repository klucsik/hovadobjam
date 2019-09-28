from app import *
from app.models import *
import logging


def make_hogyan_dobjam(user_id, hull_id, comment):
    new_row = HogyanDobjam(hull_id=hull_id, user_id=user_id, comment=comment,score=0)
    logging.info(f"inserted HogyanDobjam row: {new_row}")
    db.session.add(new_row)
    db.session.flush()
    db.session.commit()
    return new_row.id


def score_hogyan_dobjam(comment_id, user_id, increment):
    # todo increment validáció (csak +1/-1, user nem viheti +2/-2ig, sajátot nem lehet)
    new_row = HogyanDobjamScores(comment_id=comment_id, user_id=user_id, increment=increment)  # rögzítjük hogy ki score-olt
    logging.info(f"inserted HogyanDobjamScores row: {new_row}")
    updated_row = HogyanDobjam.query.filter_by(id=comment_id).first()
    updated_row.score = updated_row.score + increment
    db.session.add(new_row)
    db.session.flush()
    db.session.commit()
    return updated_row.score

def get_hogyan_dobjam(hull_id):
    '''
    :param hull_id: a hulladék id-je melyhez keressük a kommenteket
    :return: csökkenő sorrendben rendezett öszes komment
    '''
    return HogyanDobjam.query.filter_by(hull_id=hull_id).order_by(HogyanDobjam.score.desc()).all()


def test_make_hogyan_dobjam():
    logging.info(make_hogyan_dobjam(user_id=1, hull_id=679, comment="it's a bird!"))

def test_score_hogyan_dobjam():
    logging.info(score_hogyan_dobjam(user_id=1, comment_id=2, increment=3))


def test_get_hogyan_dobjam():
    logging.info(get_hogyan_dobjam(679))