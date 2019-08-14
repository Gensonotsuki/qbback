from apps.notebook import creat_notebook

app = creat_notebook()

if __name__ == '__main__':
    app.run(debug=True,port=8090)
