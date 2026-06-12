from flask import Blueprint
from flask import render_template
from flask import request

from database.db import mysql

resource = Blueprint(
'resource',
__name__
)

@resource.route(
'/add_resource',
methods=['GET','POST']
)

def add_resource():

    if request.method=='POST':

        name=request.form[
        'resource_name'
        ]

        quantity=int(
        request.form['quantity']
        )

        resource_type=request.form[
        'resource_type'
        ]

        cursor=mysql.connection.cursor()

        cursor.execute(
        """
        INSERT INTO
        hospital_resources
        (
        resource_name,
        total_quantity,
        available_quantity,
        resource_type
        )

        VALUES
        (%s,%s,%s,%s)
        """,

        (
        name,
        quantity,
        quantity,
        resource_type
        )
        )

        mysql.connection.commit()

    return render_template(
    'resources/add_resource.html'
    )

@resource.route(
'/resource_dashboard'
)

def resource_dashboard():

    cursor=mysql.connection.cursor()

    cursor.execute(
    """
    SELECT COUNT(*)
    FROM hospital_resources
    """
    )

    total=cursor.fetchone()[0]

    return render_template(

    'resources/resource_dashboard.html',

    total=total

    )

