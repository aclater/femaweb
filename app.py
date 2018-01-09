from flask import Flask
from application import application

if __name__ == "__main__":
	application.run(host='0.0.0.0', port=8080)
