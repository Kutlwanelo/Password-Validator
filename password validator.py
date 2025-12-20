import re
import getpass

def check_password_strength(password):
  common_passwords = ["password", "123456","admin", "welcome", "iloveyou", "password123"]
  if password.lower() in common_passwords:
    print("❌ CRITICAL: This is a commonly hacked password. Change immediately!")
    return
  score = 0
  feedback = []
  
  # Criteria 1: Length
  if len(password) >= 8:
    score += 1
  else:
    feedback.append("• Password is too short (needs 8+ characters).")
    
  #Criteria 2: Uppercase
  if re.search(r"[A-Z]", password):
    score +=1
  else:
    feedback.append("• Add an uppercase letter.")
  
  #Criteria 3: Lowercase
  if re.search(r"[a-z]", password):
    score += 1
  else:
    feedback.append("• Add a lowercase letter.")
    
  #Criteria 4: Numbers
  if re.search(r"\d", password):
    score += 1
  else:
    feedback.append("• Add a number.")
    
  #Criteria 5: Special Characters
  if re.search(r"[ !#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
    score += 1
  else:
    feedback.append("• Add a special character (e.g , !, @, #).")
    
  #Final Calculation
  print(f"\nPassword Score: {score}/5")
  
  if score == 5:
    print("Strength: STRONG ✅")
  elif score >= 3:
    print("Strength: MEDIUM ⚠️")
  else:
    print("Strength: WEAK ❌ ")
    
  if feedback:
    print("Suggesions to improve:")
    for item in feedback:
      print(item)
  
#Main execution
if __name__ == "__main__":
  user_pass = input("Enter a password to test: ")
  check_password_strength(user_pass)