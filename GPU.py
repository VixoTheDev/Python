import tensorflow as tf
import random
import string
import threading

# Check if GPU is available
if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

# Function to generate random letters
def generate_random_letters():
    num_letters = 1000
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))
    return letters

# Function to perform matrix multiplication on GPU
def matrix_multiplication():
    matrix_size = 1000
    matrix_a = tf.random.normal((matrix_size, matrix_size))
    matrix_b = tf.random.normal((matrix_size, matrix_size))
    
    with tf.device('/GPU:0'):
        result = tf.matmul(matrix_a, matrix_b)
    
    print("Matrix multiplication result on GPU:", result)

# Function to write random letters to a file
def write_to_file(letters):
    with open("test.txt", "w") as file:
        file.write(letters)
    print("Random letters written to file")

# Generate random letters
random_letters = generate_random_letters()

# Create and start threads
matrix_thread = threading.Thread(target=matrix_multiplication)
write_thread = threading.Thread(target=write_to_file, args=(random_letters,))

matrix_thread.start()
write_thread.start()

matrix_thread.join()
write_thread.join()
