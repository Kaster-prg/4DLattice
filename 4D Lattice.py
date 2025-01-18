import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #https://tenpy.readthedocs.io/en/v0.8.1/notebooks/10_visualize_lattice.html

# Key Parameters
np.random.seed(42)
lattice_size = 10  # Size of each dimension in the lattice
num_dimensions = 4  # Number of dimensions

# Generate a 4D Lattice
def generate_4d_lattice(size):
    lattice_points = []
    for x in range(size):
        for y in range(size):
            for z in range(size):
                for w in range(size):
                    lattice_points.append((x, y, z, w))
    return np.array(lattice_points)

# Simple Encryption: Map message to 4D lattice coordinates
def encrypt_message_4d(message, lattice_size):
    encrypted_points = []
    for char in message:
        x = (ord(char) % lattice_size)
        y = (ord(char) // lattice_size) % lattice_size
        z = (ord(char) // (lattice_size ** 2)) % lattice_size
        w = (ord(char) // (lattice_size ** 3)) % lattice_size
        encrypted_points.append((x, y, z, w))
    return np.array(encrypted_points)

# Simple Decryption: Map 4D coordinates back to message
def decrypt_message_4d(encrypted_points, lattice_size):
    message = ''
    for (x, y, z, w) in encrypted_points:
        char_code = x + y * lattice_size + z * (lattice_size ** 2) + w * (lattice_size ** 3)
        message += chr(char_code)
    return message

# Generate random 4D vectors for demonstration
def generate_random_4d_vectors(num_vectors, max_length):
    vectors = []
    for _ in range(num_vectors):
        vector = np.random.randint(-max_length, max_length, size=4)
        vectors.append(vector)
    return np.array(vectors)

# Visualize 4D Lattice (projected to 3D) with vectors -- https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
def plot_4d_lattice_projection(lattice_points, encrypted_points, vectors):
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d')

    # Project lattice points to 3D by selecting only x, y, z
    ax.scatter(lattice_points[:, 0], lattice_points[:, 1], lattice_points[:, 2], color='gray', alpha=0.1)

    # Project encrypted points to 3D and plot them
    ax.scatter(encrypted_points[:, 0], encrypted_points[:, 1], encrypted_points[:, 2], color='red', s=50)

    # Plot vectors in 3D projection
    for i, point in enumerate(encrypted_points):
        vector = vectors[i % len(vectors)]  # Cycle through vectors if fewer than points
        endpoint = point + vector
        ax.quiver(point[0], point[1], point[2], vector[0], vector[1], vector[2], color='blue', arrow_length_ratio=0.1)

    ax.set_title("4D Lattice (Projected to 3D) with Encrypted Points and Vectors")
    plt.show()

# Generate Private and Public Keys
def generate_keys_4d(max_length):
    # Private key is a random 4D vector
    private_key = np.random.randint(-max_length, max_length, size=4)

    # Public key is the private key with added noise
    noise = np.random.randint(-max_length // 2, max_length // 2, size=4)
    public_key = private_key + noise

    return private_key, public_key

# Main Program
lattice_points = generate_4d_lattice(lattice_size)

# Message to encrypt
message = input("Please enter a message to encrypt: ")
print(f"Original Message: {message}")

# Encrypt and display the encrypted message
encrypted_points = encrypt_message_4d(message, lattice_size)
print(f"Encrypted 4D Lattice Coordinates: {encrypted_points}")

# Convert encrypted points into a string representation
encrypted_message = ' '.join(f"{tuple(point)}" for point in encrypted_points)
print(f"Encrypted Message (4D Coordinates): {encrypted_message}")

# Generate random 4D vectors for visualization
num_vectors = len(encrypted_points)
max_vector_length = 3
vectors = generate_random_4d_vectors(num_vectors, max_vector_length)

# Plotting the 4D lattice projection to 3D with vectors
plot_4d_lattice_projection(lattice_points, encrypted_points, vectors)

# Generate keys
private_key, public_key = generate_keys_4d(max_vector_length)
print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")

# Decrypt and display the decrypted message
decrypted_message = decrypt_message_4d(encrypted_points, lattice_size)
print(f"Decrypted Message: {decrypted_message}")
