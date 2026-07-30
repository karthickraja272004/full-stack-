from flask import Flask, jsonify
import logging
from dotenv import load_dotenv
import os
from services import user_service

app = Flask(__name__)

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route("/users")
def get_all_users():

    logging.info("Get All Users API called")

    try:
        users = user_service.get_all_users()

        return jsonify(users)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>")
def get_user_by_id(user_id):

    logging.info("Get User By ID API called")

    try:
        user = user_service.get_user_by_id(user_id)

        return jsonify(user)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>/company")
def get_user_company(user_id):

    logging.info("Get User Company API called")

    try:
        company = user_service.get_user_company(user_id)

        return jsonify(company)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>/address")
def get_user_address(user_id):

    logging.info("Get User Address API called")

    try:
        address = user_service.get_user_address(user_id)

        return jsonify(address)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>/bank")
def get_user_bank(user_id):

    logging.info("Get User Bank API called")

    try:
        bank = user_service.get_user_bank(user_id)

        return jsonify(bank)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>/hair")
def get_user_hair(user_id):

    logging.info("Get User Hair API called")

    try:
        hair = user_service.get_user_hair(user_id)

        return jsonify(hair)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/users/<int:user_id>/crypto")
def get_user_crypto(user_id):

    logging.info("Get User Crypto API called")

    try:
        crypto = user_service.get_user_crypto(user_id)

        return jsonify(crypto)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    print("Before app.run()")
    app.run(host="0.0.0.0", port=8080, debug=True)
    print("After app.run()")