from flask import Flask, render_template, jsonify

app = Flask(__name__)

Items = [
  {
    'id': 1,
    'name': 'Cheesecake',
    'price': '$50',
    'description': 'A delicious cheesecake',
    'stock': 'yes'
  },
  {
    'id': 2,
    'name': 'Cupcake',
    'price': '$30',
    'description': 'A delicious cupcake',
    'stock': 'yes'
  },
   { 'id': 3,
    'name': 'Brownie',
    'price': '$40',
    'description': 'A delicious brownie',
    'stock': 'yes'
   },
  {
    'id': 4,
    'name': 'Cookie',
    'price': '$20',
    'description': 'A delicious cookie',
    'stock': 'yes'
  }
]

@app.route('/')
def Home():
  return render_template("home.html",items=Items)

@app.route('/api/items')
def list_items():
  return jsonify(Items)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)