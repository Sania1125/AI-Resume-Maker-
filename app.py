# Simple Resume Builder - No installation needed!

def collect_user_info():
    print("Enter your resume details:")
    name = input("Full Name: ")
    email = input("Email Address: ")
    phone = input("Phone Number: ")
    education = input("Education Details: ")
    experience = input("Work Experience: ")
    skills = input("Skills (comma separated): ")
    return name, email, phone, education, experience, skills

def create_resume_text(name, email, phone, education, experience, skills):
    resume = f"""
    ==========================
            RESUME
    ==========================

    Name: {name}
    Email: {email}
    Phone: {phone}

    --------------------------
    Education:
    {education}

    --------------------------
    Experience:
    {experience}

    --------------------------
    Skills:
    {skills}
    """
    return resume

def save_resume(content, filename="resume.txt"):
    with open(filename, "w") as file:
        file.write(content)
    print(f"Resume saved successfully as {filename}")

def main():
    name, email, phone, education, experience, skills = collect_user_info()
    resume_content = create_resume_text(name, email, phone, education, experience, skills)
    save_resume(resume_content)

if __name__ == "__main__":
    main()
