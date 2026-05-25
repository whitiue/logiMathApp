import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models import SessionLocal, Base, Question, User, Quiz

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependencia para obtener la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============ MODELOS PYDANTIC ============

class UserResponse(BaseModel):
    id: int
    name: str
    email: str


class QuizResponse(BaseModel):
    id: int
    title: str
    subject: str
    difficulty: str


class QuestionResponse(BaseModel):
    id: int
    question_text: str
    correct_answer: str


class ScoreResponse(BaseModel):
    id: int
    user_id: int
    quiz_id: int
    score: float


# ============ USUARIOS ============

@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """Obtener todos los usuarios"""
    users = db.query(User).all()
    return users


@app.post("/users", response_model=UserResponse)
def create_user(
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    """Crear un nuevo usuario"""
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ============ QUIZZES ============

@app.get("/quizzes", response_model=list[QuizResponse])
def get_quizzes(db: Session = Depends(get_db)):
    """Obtener todos los quizzes"""
    quizzes = db.query(Quiz).all()
    return quizzes


@app.post("/quizzes", response_model=QuizResponse)
def create_quiz(
    title: str,
    subject: str,
    difficulty: str,
    db: Session = Depends(get_db)
):
    """Crear un nuevo quiz"""
    quiz = Quiz(
        title=title,
        subject=subject,
        difficulty=difficulty
    )
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz


# ============ QUESTIONS ============

@app.get(
    "/quizzes/{quiz_id}/questions",
    response_model=list[QuestionResponse]
)
def get_questions(
    quiz_id: int,
    db: Session = Depends(get_db)
):
    """Obtener preguntas de un quiz"""
    questions = db.query(Question).filter(
        Question.quiz_id == quiz_id
    ).all()
    return questions


@app.post(
    "/quizzes/{quiz_id}/questions",
    response_model=QuestionResponse
)
def create_question(
    quiz_id: int,
    question_text: str,
    correct_answer: str,
    difficulty: str,
    db: Session = Depends(get_db)
):
    """Crear una pregunta en un quiz"""
    question = Question(
        quiz_id=quiz_id,
        question_text=question_text,
        correct_answer=correct_answer,
        difficulty=difficulty,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


# ============ HEALTH CHECK ============

@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"message": "LogiMath API running! 🚀"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)