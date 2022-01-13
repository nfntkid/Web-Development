from website import create_app
from os import system
system("clear")



app = create_app()
if __name__== '__main__':
    app.run(host='0.0.0.0', port=8000)
    #app.run(debug=True)
    