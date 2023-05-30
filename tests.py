import unittest
from app import app


class TestSquareEquation(unittest.TestCase):
    def test_custom(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': 1, 'b': 4, 'c': 3})
        self.assertIn('x₁=-1.0', response.data.decode()) # Проверка первого корня
        self.assertIn('x₂=-3.0', response.data.decode()) # Проверка второго корня


    def test_string(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': "Всем", 'b': "hello", 'c': "!!!"})
        self.assertIn("Введите корректные значения(2, 20, 3.53,...)", response.data.decode())

    def test_a_zero(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': 0, 'b': -5, 'c': 10})
        self.assertIn("Введите корректные значения(2, 20, 3.53,...)", response.data.decode())

    def test_c_zero(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': 25, 'b': 5, 'c': 0})
        self.assertIn('x₁=0.0', response.data.decode())  # Проверка первого корня
        self.assertIn('x₂=-0.2', response.data.decode())  # Проверка второго корня

    def test_bc_zero(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': 25, 'b': 0, 'c': 0})
        self.assertIn('x₁=0.0', response.data.decode())  # Проверка первого корня
        self.assertIn('x₂=-0.0', response.data.decode())  # Проверка второго корня

    def test_complex(self):
        fake_user = app.test_client(self)
        response = fake_user.post('/', content_type='multipart/form-data', data={'a': 2, 'b': 10, 'c': 20.5})
        self.assertIn('x₁=(-2.5+2j)', response.data.decode())  # Проверка первого корня
        self.assertIn('x₂=(-2.5-2j)', response.data.decode())  # Проверка второго корня


if __name__ == '__main__':
    unittest.main()
