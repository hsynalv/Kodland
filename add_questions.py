from app import app, db
from app.models import Question

questions = [
    Question(
        question_text="Python'da hangi kütüphane makine öğrenimi için en yaygın olarak kullanılır?",
        option_a="TensorFlow", option_b="PyTorch", option_c="scikit-learn", option_d="Keras",
        correct_answer="scikit-learn"
    ),
    Question(
        question_text="Görüntü işleme için en çok kullanılan Python kütüphanesi nedir?",
        option_a="NumPy", option_b="Pandas", option_c="OpenCV", option_d="Matplotlib",
        correct_answer="OpenCV"
    ),
    Question(
        question_text="Doğal Dil İşleme (NLP) için popüler bir Python kütüphanesi hangisidir?",
        option_a="Requests", option_b="NLTK", option_c="Flask", option_d="Django",
        correct_answer="NLTK"
    ),
    Question(
        question_text="Derin öğrenme modelleri oluşturmak için kullanılan bir Python kütüphanesi hangisidir?",
        option_a="scikit-learn", option_b="Keras", option_c="NumPy", option_d="Pandas",
        correct_answer="Keras"
    ),
    Question(
        question_text="Python'da veri analizi için kullanılan popüler bir kütüphane hangisidir?",
        option_a="Flask", option_b="Django", option_c="Pandas", option_d="NumPy",
        correct_answer="Pandas"
    ),
    Question(
        question_text="Makine öğreniminde kullanılan bir regresyon algoritması hangisidir?",
        option_a="Lineer Regresyon", option_b="Logaritmik Regresyon", option_c="Quadratik Regresyon", option_d="Bütünleşik Regresyon",
        correct_answer="Lineer Regresyon"
    )
]

with app.app_context():
    db.session.add_all(questions)
    db.session.commit()
