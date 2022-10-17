from src import app
from meinheld import server # mainheld server

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    server.listen("0.0.0.0")
    server.run(app)