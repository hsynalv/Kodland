from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import UserScore, Question

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = Question.query.order_by(db.func.random()).limit(4).all()
    total_questions = len(questions)
    username = session.get('username', 'guest')
    user = UserScore.query.filter_by(username=username).first()

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.form.get(f'answer{question.id}')
            if user_answer and user_answer == question.correct_answer:
                score += 1

        percentage_score = (score / total_questions) * 100  # Yüzdelik hesaplama

        if user:
            if percentage_score > user.highscore:
                user.highscore = percentage_score
        else:
            user = UserScore(username=username, highscore=percentage_score)
            db.session.add(user)
        db.session.commit()

        session['score'] = percentage_score
        return redirect(url_for('results'))

    # Kullanıcının en iyi puanını yüzde olarak hesapla ve gönder
    best_score = user.highscore if user else 0
    return render_template('quiz.html', questions=questions, username=username, best_score=best_score)


@app.route('/results')
def results():
    percentage_score = session.get('score', 0)
    username = session.get('username', 'guest')
    user = UserScore.query.filter_by(username=username).first()
    highscore = user.highscore if user else 0

    return render_template('results.html', percentage_score=percentage_score, highscore=highscore)

@app.route('/set_username', methods=['POST'])
def set_username():
    session['username'] = request.form.get('username')
    return redirect(url_for('quiz'))
