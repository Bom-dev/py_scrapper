import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
   sys.path.insert(0, path)

from main import app
 
if __name__ == "__main__":
        app.run()