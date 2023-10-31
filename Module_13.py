"""
Software 2 - Python Module 13
Setting up a backend service with an interface
"""

# Task 1

from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<num>')
def primer(num):
    flag = True
    num = int(num)
    if num == 1:
        flag = False

    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break

    response = {
        "Num": num, "isPrime": flag
    }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
