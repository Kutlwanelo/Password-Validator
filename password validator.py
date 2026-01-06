import re
import getpass
import hashlib
import os
import secrets  
import string  

# --- MODULE 1: THE DATABASE SIMULATOR (HASHING) ---
def hash_password(password):
    # 1. Generate a random 'Salt' (16 random bytes)
    # This ensures every hash is unique, even for the same password.
    salt = os.urandom(16)
    
    # 2. Combine the Salt and the Password
    password_bytes = password.encode('utf-8')
    combined = salt + password_bytes
    
    # 3. Hash the combination using SHA-256
    hash_object = hashlib.sha256(combined)
    hashed_password = hash_object.hexdigest()
    
    # Return both so we can see them
    return salt.hex(), hashed_password

# --- MODULE 2: THE CREATOR (GENERATOR) ---
def generate_strong_password(length=12):
    # Define our ingredients: a-z, A-Z, 0-9, and symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        # Use 'secrets' to pick random characters
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        
        # Verify it has at least one of each type
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

# --- MODULE 3: THE JUDGE (VALIDATOR) ---
def check_password_strength(password):
    # 0. The Blacklist Check (Defense against common attacks)
    common_passwords = ["password", "123456", "admin", "welcome", "iloveyou", "password123"]
    if password.lower() in common_passwords:
        print("❌ CRITICAL: This is a commonly hacked password. Change immediately!")
        return

    score = 0
    feedback = []
    
    # Criteria Checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password is too short (needs 8+ characters).")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add an uppercase letter.")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add a lowercase letter.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add a number.")
        
    if re.search(r"[ !#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
        score += 1
    else:
        feedback.append("• Add a special character (e.g., !, @, #).")

    # Final Calculation
    print(f"\nPassword Score: {score}/5")
    
    if score == 5:
        print("Strength: STRONG ✅")
    elif score >= 3:
        print("Strength: MEDIUM ⚠️")
    else:
        print("Strength: WEAK ❌")
        
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(item)

# --- MAIN MENU (THE INTERFACE) ---
if __name__ == "__main__":
    print("--- 🛡️ CYBER SECURITY TOOLKIT 🛡️ ---")
    print("1. Check Password Strength")
    print("2. Generate Secure Password")
    
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        # Option 1: Validate User Input
        user_pass = getpass.getpass("Enter a password to test (Hidden): ")
        check_password_strength(user_pass)
        
        # Show how it would be stored
        print("\n--- DATABASE SIMULATION ---")
        salt, my_hash = hash_password(user_pass)
        print(f"Salt (Randomizer): {salt}")
        print(f"Final Stored Hash: {my_hash}")

    elif choice == "2":
        # Option 2: Generate New Password
        print("\nGenerating cryptographically secure password...")
        new_pass = generate_strong_password()
        print(f"Your new password: {new_pass}")
        
        # Show how it would be stored
        print("\n--- DATABASE SIMULATION ---")
        salt, my_hash = hash_password(new_pass)
        print(f"Stored Hash: {my_hash}")
        
    else:
        print("Invalid choice. Exiting.")