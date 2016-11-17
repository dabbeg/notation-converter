from flask import Flask, jsonify, request
app = Flask(__name__)

import parser

@app.route('/parse', methods=['POST'])
def parse():
    input = request.form.get('input')
    if input == None:
        return 'key: input not found in body'

    conversionFrom = request.form.get('conversionFrom')
    if conversionFrom == None:
        return 'key: conversionFrom not found in body'

    conversionTo = request.form.get('conversionTo')
    if conversionTo == None:
        return 'key: conversionTo not found in body'

    conversion = conversionFrom + '-' + conversionTo

    try:
        return parser.run(conversion, input)
    except ValueError as e:
        return e.args[0], 400

if __name__ == '__main__':
    app.run()
