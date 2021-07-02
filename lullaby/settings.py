import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORT = config('PORT', 5000)
DB_URI = config('DATABASE_URL', 'postgresql://postgres:postgres@localhost/lullaby')
API_KEY = config('API_KEY', '1234')
PRODUCT_URI = 'http://challenge-api.luizalabs.com/api/product'
REDIS_HOST = config('REDIS_HOST', 'localhost')
