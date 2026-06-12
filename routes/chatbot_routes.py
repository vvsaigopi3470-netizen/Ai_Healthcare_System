from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

from chatbot.intent_classifier \
import detect_intent

from chatbot.chatbot_engine \
import generate_response

chatbot = Blueprint(
'chatbot',
__name__
)

@chatbot.route(
'/chatbot',
methods=['GET','POST']
)

def chat():

    response = ""

    if request.method == 'POST':

        patient_id = request.form[
        'patient_id'
        ]

        message = request.form[
        'message'
        ]

        intent = detect_intent(
        message
        )

        response = generate_response(
        intent
        )

        cursor = mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO
        chatbot_history
        (
        patient_id,
        user_message,
        bot_response
        )

        VALUES
        (%s,%s,%s)
        """,

        (
        patient_id,
        message,
        response
        )
        )

        mysql.connection.commit()

    return render_template(

    'chatbot/chatbot.html',

    response=response

    )

@chatbot.route(
'/chat_history'
)

def history():

    cursor = mysql.connection.cursor()

    cursor.execute(
    """
    SELECT *
    FROM chatbot_history
    ORDER BY created_at DESC
    """
    )

    data = cursor.fetchall()

    return render_template(
    'chatbot/chat_history.html',
    chats=data
    )

@chatbot.route(
'/chatbot_dashboard'
)

def dashboard():

    cursor = mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM chatbot_history
    """
    )

    total = cursor.fetchone()[0]

    return render_template(
    'chatbot/chatbot_dashboard.html',
    total=total
    )
