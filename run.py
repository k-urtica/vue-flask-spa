from app import create_app


app = create_app()

# 開発用
if __name__ == "__main__":
    app.run()
