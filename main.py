from website import create_app

app = create_app()

if __name__ == '__main__': # we dont want to run web server, unless we run correctly
    app.run(debug=True) # start web server
