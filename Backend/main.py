from jobs.server import Server
        
app = Server()

if __name__ == "__main__":
    app.app.run(port=5000,debug=True)
