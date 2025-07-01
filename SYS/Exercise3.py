import sys

# Writing normal output
sys.stdout.write("✅ This is standard output using sys.stdout\n")

# Writing error message
sys.stderr.write("❌ This is an error message using sys.stderr\n")

# Reading input from stdin (like input())
sys.stdout.write("Enter your name: ")
name = sys.stdin.readline().strip()

sys.stdout.write(f"Hello, {name}!\n")
